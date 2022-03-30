#! /bin/bash

read -p "Enter the user status(active/inactive): "  status

if [ "${status,,}" == "active" ]
then
	echo "Please find the reports"
	OUTPUT=$(cat sample.json | jq -r '.[] | select(.status | ascii_downcase =="active") | "Name: \(.name)\nDesignation: \(.designation)\nStatus: \(.status)\n"')
	echo "${OUTPUT}"

elif [ "${status,,}" == "inactive" ]
then
	echo "Please find the reports"
	OUTPUT=$(cat sample.json | jq -r '.[] | select(.status | ascii_downcase =="inactive") | "Name: \(.name)\nDesignation: \(.designation)\nStatus: \(.status)\n"')
	echo "${OUTPUT}"

else
	echo "Status is invalid"
fi
