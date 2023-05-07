Step-by-step procedure to build an Ubuntu AMI with Nginx installed using Packer:

1. Install Packer: First, you need to install Packer on your local machine. You can download the latest version of Packer from the official website.

2. Create a Packer template: Create a new file called "ubuntu-nginx.json" and add the following JSON code to it:
{
  "builders": [
    {
      "type": "amazon-ebs",
      "region": "us-east-1",
      "source_ami": "ami-0c55b159cbfafe1f0",
      "instance_type": "t2.micro",
      "ssh_username": "ubuntu",
      "ami_name": "ubuntu-nginx {{isotime | clean_resource_name}}"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "sudo apt-get update",
        "sudo apt-get install -y nginx"
      ]
    }
  ]
}
This Packer template specifies that we want to use the Amazon EBS builder to launch a t2.micro instance in the us-east-1 region, install Ubuntu, and then install Nginx using the shell provisioner.

3. Validate the Packer template: Validate the Packer template using the "packer validate" command to ensure that it is syntactically correct:

# packer validate ubuntu-nginx.json

4. Build the image: Use the "packer build" command to build the image:

# packer build ubuntu-nginx.json

This command will launch an instance, install Ubuntu, and install Nginx on it. Once the provisioning is complete, Packer will create a new AMI with Nginx installed.

5. Test the AMI: Test the AMI by launching an instance from it and verifying that Nginx is installed and working correctly.

6. Publish the AMI: Publish the AMI to a centralized image repository such as Amazon EC2 or Docker Hub. This will make it easy for other teams to use the AMI and ensure that everyone is using the same version.

By using Packer, you can easily automate the creation of AMIs for Ubuntu with Nginx installed and ensure that they are consistent and up-to-date.