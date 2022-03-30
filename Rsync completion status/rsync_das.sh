#!/bin/sh

#===============================================================================================================
# Functionality and Usage
#===============================================================================================================
# version 1 (v1):
# 1. standard rsync command with single source and dest folders. Ex: /ofs-us-west-1/ to /mnt/ofs/
# 2. Logrotation configuration based on rsync log format
#
# version 2 (v2):
# 1. standard rsync command constructed dynamically for each ccids. Ex: /ofs-us-west-1/<ccid>/ to /mnt/ofs/<ccid>/
# 2. Enables Dedicated rsync cron job for Business controls replication.
# 3. Logrotation configuration based on rsync log format
#
# -v option can get v1 or v2 (Default v2 no -v flag required) as input and based on that rsync functionalities
#    will be enabled.
# -f option enables file based input with list of ccids. if -f is enabled it assumes STACK_NAME as input file,
#    and it expects a file with <STACK_NAME> inside each OFS mount points. Ex: /ofs-us-west-1/DAS-E5-USW8
# -c option can be used to cleanup all generated files by above v1 and v2 fuctions (Manual use only)
# doesn't clean up lock files for now
#
# version 2.5 (v2):
# 1. Moved Rsync support scripts from /tmp to /etc/denesys-designer/
# 2. Introduced a mechanism to rsync non-ccid folders in the workspace
#      -> Add the folder/file name that are need to be synced at /etc/designer-scripts/non_ccid_list. The non-ccid Rsync interval is 30 minutes.
# 3. Enhanced the Rsync V2 log format by adding the cc-id of the files that is being synced
#
#version 3 (v2):
# 1. Enabled whitelist for business object rsync
# 2. Added an option to blacklist the non-essential ccid folders(prefer to use in staging only)
# 3. Added an flag -s to print the Rsync version in commandline
#
# -s option can be used to identify the current Rsync script version running inside the machine
#
#===============================================================================================================
set -e

scriptname=$(basename $0)
usage() {
  echo 'Usage: '`basename $0`''
  echo '  -v <version>'
  echo '     Rsync script version v1 or v2'
  echo '  -f <no value required>'
  echo '     File input with list of ccids for cuncurrent rsync'
  echo '  -c <no value required>'
  echo '     Cleanup all the cronjobs and files created via this script'
  echo '  -s <no value required>'
  echo '     Print Rsync version running inside the instance'
}

cleanup(){
  # cleanup all files and configs created. both version 1 and 2
  echo "Cleaning up all cron jobs and files"
  read -p "Continue ? " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    rm -f /etc/designer-scripts/concurrent_rsync.sh /etc/designer-scripts/generate_business_ctrl_filelist.sh /etc/designer-scripts/rsync_exclude_dirs
    rm -f /etc/cron.d/des_rsync_*
    rm -f /etc/designer-scripts/business-ctrl-filelist*
    rm -f /etc/cron.d/rsync_logrotate
    rm -f /etc/designer-scripts/rsync_nonccid_folder.sh
    rm -f /etc/designer-scripts/non_ccid_list
    echo "Cleanup successful"
  else
    echo "Cleanup aborted"
  fi

}

printversion() {
  if [ -f "$VERSIONFILE" ];
  then
    cat $VERSIONFILE
  else
    echo "2.0"
  fi
}

args=`getopt 'hv:fc:s' $*`
if [ $? -ne 0 ]; then
  usage
  exit 2
fi

set -- $args
SCRIPTVERSION="3.0"
VERSIONFILE="/etc/designer-scripts/version"
VERSION="v2" # default v2
CCID_FILE_INPUT="false"
CLEANUP=0

for i; do
  case "$i"
  in
    -v)
      VERSION="$2"; shift;
      shift;;
    -f)
      CCID_FILE_INPUT="true"; CCID_FILE_NAME="$2"; shift;
      shift;;
    -c)
      cleanup; exit 0
      ;;
    -s)
      printversion; exit 0
      ;;
    -h)
      usage; exit 0
      ;;
    --)
      shift; break;;
  esac
done

STACK_NAME=$1
REGION=$2
IU_NAME=$3

rsync_cron() {
    echo '* * * * * root flock -n /var/lock/des_rsync_usw1.lock rsync -rptqi --force --exclude=designer --log-file=/mnt/log/rsync/des_rsync.usw1.log /ofs-us-west-1/ /mnt/ofs &>/dev/null' > /etc/cron.d/des_rsync_usw1
    echo '* * * * * root flock -n /var/lock/des_rsync_aps2.lock rsync -rptqi --force --exclude=designer --log-file=/mnt/log/rsync/des_rsync.aps2.log /ofs-ap-southeast-2/ /mnt/ofs &>/dev/null' > /etc/cron.d/des_rsync_aps2
    echo '* * * * * root flock -n /var/lock/des_rsync_euw1.lock rsync -rptqi --force --exclude=designer --log-file=/mnt/log/rsync/des_rsync.euw1.log /ofs-eu-west-1/ /mnt/ofs &>/dev/null' > /etc/cron.d/des_rsync_euw1
    echo "Created rsync cron jobs v1"
}

rsync_businessobjs_cron() {
  generate_business_ctrl_filelist
  chmod +x /etc/designer-scripts/generate_business_ctrl_filelist.sh
  echo "* * * * * root /etc/designer-scripts/generate_business_ctrl_filelist.sh /ofs-us-west-1 $1 ; nice -n -20 flock -n /var/lock/des_rsync_usw1_bo.lock rsync -rptqi --include-from=/etc/designer-scripts/business-ctrl-filelist-ofs-us-west-1  --exclude=* --log-file=/mnt/log/rsync/des_rsync.usw1_business_obj.log /ofs-us-west-1/ /mnt/ofs &>/dev/null" > /etc/cron.d/des_rsync_businessobjs
  echo "* * * * * root sleep 30; /etc/designer-scripts/generate_business_ctrl_filelist.sh /ofs-us-west-1 $1; nice -n -20 flock -n /var/lock/des_rsync_usw1_bo.lock rsync -rptqi  --include-from=/etc/designer-scripts/business-ctrl-filelist-ofs-us-west-1  --exclude=* --log-file=/mnt/log/rsync/des_rsync.usw1_business_obj.log /ofs-us-west-1/ /mnt/ofs &>/dev/null" >> /etc/cron.d/des_rsync_businessobjs
  echo "* * * * * root /etc/designer-scripts/generate_business_ctrl_filelist.sh /ofs-ap-southeast-2 $1 ; nice -n -20 flock -n /var/lock/des_rsync_aps2_bo.lock rsync -rptqi --include-from=/etc/designer-scripts/business-ctrl-filelist-ofs-ap-southeast-2  --exclude=* --log-file=/mnt/log/rsync/des_rsync.aps2_business_obj.log /ofs-ap-southeast-2/ /mnt/ofs &>/dev/null" >> /etc/cron.d/des_rsync_businessobjs
  echo "* * * * * root sleep 30; /etc/designer-scripts/generate_business_ctrl_filelist.sh /ofs-ap-southeast-2 $1 ; nice -n -20 flock -n /var/lock/des_rsync_aps2_bo.lock rsync -rptqi  --include-from=/etc/designer-scripts/business-ctrl-filelist-ofs-ap-southeast-2  --exclude=* --log-file=/mnt/log/rsync/des_rsync.aps2_business_obj.log /ofs-ap-southeast-2/ /mnt/ofs &>/dev/null" >> /etc/cron.d/des_rsync_businessobjs
  echo "* * * * * root /etc/designer-scripts/generate_business_ctrl_filelist.sh /ofs-eu-west-1 $1 ; nice -n -20 flock -n /var/lock/des_rsync_euw1_bo.lock rsync -rptqi --include-from=/etc/designer-scripts/business-ctrl-filelist-ofs-eu-west-1  --exclude=* --log-file=/mnt/log/rsync/des_rsync.euw1_business_obj.log /ofs-eu-west-1/ /mnt/ofs &>/dev/null" >> /etc/cron.d/des_rsync_businessobjs
  echo "* * * * * root sleep 30; /etc/designer-scripts/generate_business_ctrl_filelist.sh /ofs-eu-west-1 $1 ; nice -n -20 flock -n /var/lock/des_rsync_euw1_bo.lock rsync -rptqi --include-from=/etc/designer-scripts/business-ctrl-filelist-ofs-eu-west-1  --exclude=* --log-file=/mnt/log/rsync/des_rsync.euw1_business_obj.log /ofs-eu-west-1/ /mnt/ofs &>/dev/null" >> /etc/cron.d/des_rsync_businessobjs
  echo "Created business controls cron jobs"
}

rsync_cron_with_exclude() {
  generate_rsync_exclude_list
  echo '* * * * * root flock -n /var/lock/des_rsync_usw1.lock rsync -rptqi --force --exclude-from=/etc/designer-scripts/rsync_exclude_dirs --log-file=/mnt/log/rsync/des_rsync.usw1.log /ofs-us-west-1/ /mnt/ofs &>/dev/null' > /etc/cron.d/des_rsync_usw1
  echo '* * * * * root flock -n /var/lock/des_rsync_aps2.lock rsync -rptqi --force --exclude-from=/etc/designer-scripts/rsync_exclude_dirs --log-file=/mnt/log/rsync/des_rsync.aps2.log /ofs-ap-southeast-2/ /mnt/ofs &>/dev/null' > /etc/cron.d/des_rsync_aps2
  echo '* * * * * root flock -n /var/lock/des_rsync_euw1.lock rsync -rptqi --force --exclude-from=/etc/designer-scripts/rsync_exclude_dirs --log-file=/mnt/log/rsync/des_rsync.euw1.log /ofs-eu-west-1/ /mnt/ofs &>/dev/null' > /etc/cron.d/des_rsync_euw1
  echo "Created rsync cron jobs with --exclude-from option"

}

rsync_concurrency_cron() {
  echo "$1"
  generate_concurrent_rsync
  chmod +x /etc/designer-scripts/concurrent_rsync.sh
  generate_rsync_exclude_list
  echo "* * * * * root flock -n /var/lock/des_rsync_usw1_con.lock /etc/designer-scripts/concurrent_rsync.sh /ofs-us-west-1 /mnt/ofs $1" > /etc/cron.d/des_rsync_usw1
  echo "* * * * * root flock -n /var/lock/des_rsync_aps2_con.lock /etc/designer-scripts/concurrent_rsync.sh /ofs-ap-southeast-2 /mnt/ofs $1" > /etc/cron.d/des_rsync_aps2
  echo "* * * * * root flock -n /var/lock/des_rsync_euw1_con.lock /etc/designer-scripts/concurrent_rsync.sh /ofs-eu-west-1 /mnt/ofs $1" > /etc/cron.d/des_rsync_euw1
  echo "Created concurrent rsync cron jobs"
}

# utility methods
generate_concurrent_rsync() {
cat <<'EOF' > /etc/designer-scripts/concurrent_rsync.sh
source="$1"
target="$2"
# argument 3 is file input
file="$3"
depth=1
BUCKET_SUFFIX=$(echo $1 | tr "/" " " | xargs)
# Set the maximum number of concurrent rsync threads
maxthreads=50
# thead sleep time
sleeptime=0.5

# If no file walk the directory else read from the file
if [ -z "$file" ];
then
        # cmd="find ${source} -maxdepth ${depth} -type d"
        cmd="ls -t $source"
else
        cmd="cat ${source}/${file}"
        # Fallback to list dir if file not found
        if [ ! -f "${source}/${file}" ]; then
          cmd="ls -t $source"
        fi
fi

echo "$cmd"
$cmd | awk --re-interval "/[A-F0-9a-f]{8}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{12}/"| while read ccid
do
        # Enable blacklist when below conditions are satisfied
        # file varaible is non empty
        # Check whether whitelist file is not exist. If exist, skip enabling blacklist.
        # Check whether blacklist file is exist
        if [[ ! -z "${file}" && ! -f "${source}/${file}" && -f "${source}/${file}_blacklist" ]] ;
        then
          # Check whether the ccid is in blacklist file
          if grep -Fxq "$ccid" ${source}/${file}_blacklist
          then
              # skip running rsync for the blacklisted ccid
              continue
          fi
        fi
        while [ `ps -ef | grep -c [r]sync` -gt ${maxthreads} ]
        do
                echo "Sleeping ${sleeptime} seconds"
                #echo -e `ps -ef | grep -c [r]sync`
                sleep ${sleeptime}
        done
        echo "`date` Syncing ccid: $ccid" >> /mnt/log/rsync/des_rsync.$BUCKET_SUFFIX.log
        # echo "source-target: ${source}/${ccid}/   -> ${target}/${ccid}/" #>> concurrent.log
        # Run rsync in background for the current subfolder and move one to the next one
        nohup rsync -rptiq --exclude-from=/etc/designer-scripts/rsync_exclude_dirs --log-file=/mnt/log/rsync/des_rsync.$BUCKET_SUFFIX.log --log-file-format="${ccid} %o %f %l %t" "${source}/${ccid}/" "${target}/${ccid}/" </dev/null >/dev/null 2>&1 &

done
  if [ ! -f "${target}"/initial_rsync_status ] ; then
      while [ `ps -ef | grep [r]sync | grep -v concurrent_rsync.sh | wc -l` -ne 0 ]
      do
          echo "Waiting for rsync complete..."
          sleep ${sleeptime}
      done
      echo "done" > "${target}"/initial_rsync_status
  fi
EOF
echo "Concurrent rsync script genereated"
}

generate_rsync_exclude_list() {
cat <<'EOF' > /etc/designer-scripts/rsync_exclude_dirs
designer
workspace/workingcopy
workspace/modules
workspace/revisions
workspace/users
EOF
}

# input is source directory
generate_business_ctrl_filelist() {
cat <<'EOF' > /etc/designer-scripts/generate_business_ctrl_filelist.sh
  source="$1"
  file="$2"
  # If no file walk the directory else read from the file
  if [ -z "$file" ];
  then
          cmd="ls -t $source"
  else
          cmd="cat ${source}/${file}"
          # Fallback to list dir if file not found
          if [ ! -f "${source}/${file}" ]; then
            cmd="ls -t $source"
          fi
  fi
  $cmd | awk --re-interval '/[A-F0-9a-f]{8}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{12}/' | awk '{print $1 "/"}' > /etc/designer-scripts/business-ctrl-filelist-$(echo $1 | tr "/" " " | xargs)
  $cmd | awk --re-interval '/[A-F0-9a-f]{8}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{12}/' | awk '{print $1 "/workspace/"}' >> /etc/designer-scripts/business-ctrl-filelist-$(echo $1 | tr "/" " " | xargs)
  $cmd | awk --re-interval '/[A-F0-9a-f]{8}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{4}-[A-F0-9a-f]{12}/' | awk '{print $1 "/workspace/businessobjects/***"}' >> /etc/designer-scripts/business-ctrl-filelist-$(echo $1 | tr "/" " " | xargs)
EOF
echo "Created businessobjects filelist generator script"
}

generate_nonccid_rsync(){
cat <<'EOF' > /etc/designer-scripts/non_ccid_list
resources/***
EOF
}


rsync_nonccid_cron() {
  generate_nonccid_rsync
  #Rsync job to sync non-ccid folders will be triggered for every 30 minutes
  echo "*/30 * * * * root flock -n /var/lock/des_rsync_usw1_nonccid.lock rsync -rptiq --include-from '/etc/designer-scripts/non_ccid_list' --exclude '*' --log-file=/mnt/log/rsync/des_rsync_nonccid.us-west-1.log /ofs-us-west-1/ /mnt/ofs/ " > /etc/cron.d/des_rsync_nonccid_folder
  echo "Created non-ccid rsync cron jobs"
}

# invoke business objects cron
#rsync_businessobjs_cron

logrotate_conf_v1() {
    chcon -t var_log_t /mnt/log/rsync || true
    configs="/mnt/log/rsync/des_rsync.usw1.log /mnt/log/rsync/des_rsync.aps2.log /mnt/log/rsync/des_rsync.euw1.log {
       rotate 72
       dateext
       dateformat .%Y%m%d-%s
       extension .log
    }"
    echo "$configs" > /etc/logrotate.d/rsync
    echo '0 * * * * root sudo logrotate -f /etc/logrotate.d/rsync' > /etc/cron.d/rsync_logrotate
    echo "Created Logrotation configurations v1"
}

logrotate_conf_v2(){
    chcon -t var_log_t /mnt/log/rsync || true
    concurrent_rsync_configs="/mnt/log/rsync/des_rsync.ofs-us-west-1.log /mnt/log/rsync/des_rsync.ofs-ap-southeast-2.log /mnt/log/rsync/des_rsync.ofs-eu-west-1.log /mnt/log/rsync/des_rsync.usw1_business_obj.log /mnt/log/rsync/des_rsync.aps2_business_obj.log /mnt/log/rsync/des_rsync.euw1_business_obj.log /mnt/log/rsync/des_rsync_nonccid.us-west-1.log {
       rotate 72
       dateext
       dateformat .%Y%m%d-%s
       extension .log
    }"
    echo "$concurrent_rsync_configs" > /etc/logrotate.d/rsync
    echo '0 * * * * root sudo logrotate -f /etc/logrotate.d/rsync' > /etc/cron.d/rsync_logrotate
    echo "Created Logrotation configurations v2"
}

prerequesties(){
  mkdir -p /etc/designer-scripts
  chmod 755 /etc/designer-scripts
}

logversion(){
  echo "${1}" > $VERSIONFILE
}

echo "Fileinput is set to: $CCID_FILE_INPUT"
if [ "$CCID_FILE_INPUT" == "true" ]; then
  file=${CCID_FILE_NAME}
else
  file=${STACK_NAME}
fi

# invoke needed fuctions here

if [ $VERSION == "v1" ]; then
  logrotate_conf_v1
  rsync_cron
else
  prerequesties
  logrotate_conf_v2
  rsync_concurrency_cron $file
  rsync_businessobjs_cron $file
  rsync_nonccid_cron
fi
logversion $SCRIPTVERSION