import os
import getpass


os.system("tput setaf  3")
print("\n\t\t\t !! Welcome To Automated Python Menu !!")
os.system("tput setaf  7")
print("\t\t\t *------------------**------------------*")



passwd = getpass.getpass("Enter your password :")


if passwd != "(add your password)":
	print("please enter correct password :")
	exit()

while True:
	
	ch = int(input('''\n\t\t\t-------Menu List--------
	press 1: To Configure,start and see the report of Hadoop Namenode.
	press 2: To format the Namenode.
	press 3: To Configure,start and see the report of Hadoop Datanode.
	press 4: To stop Hadoop Namenode/Datanode.
	press 5: To Configure the Hadoop Client and Read the Uploaded data.
	press 6: To Remove the file uploaded by Hadoop client.
	press 7: To Configure,start and see the status of Apache Webserver.
	press 8: To Stop Apache webserver.
	press 9: To Create,format and mount the LVM Partition.
	press 10: To Extend the Logical Volume.
	press 11: To resize/format the newly created LV.
	press 12: To create key-pair,security group and launch aws instance.
	press 13: To create EBS volume and attach EBS volume to instance.
	press 14: To create s3 bucket.
	press 15: To uploade object on s3 bucket.
	press 16: To create cloud front.
	press 17: To start docker
	press 18: To launch docker container.
	press 19: To stop docker container.
	press 20: To start docker container.
	press 21: To remove docker container permentaly.
	press 22: To remove container image.
	press 23: To stop docker.
	press 24: To Exit.
	Enter your Choice : '''))

	if ch == 1:
		name1 = input("Enter your folder name for namenode : ")
		os.system("mkdir {}" .format(name1))
		path = '/etc/hadoop'
		os.chdir(path)
		os.system("vi hdfs-site.xml")
		os.system("vi core-site.xml")
		os.system("hadoop-daemon.sh start namenode")
		os.system("jps")
		os.system("hadoop dfsadmin -report")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 2:
		os.system("hadoop namenode -format")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 3:
		name1 = input("Enter your folder name for datanode : ")
		os.system("mkdir {}" .format(name1))
		path = '/etc/hadoop'
		os.chdir(path)
		os.system("vi hdfs-site.xml")
		os.system("vi core-site.xml")
		os.system("hadoop-daemon.sh start datanode")
		os.system("jps")
		os.system("hadoop dfsadmin -report")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 4:
		name1 = input("Enter the name of Hadoop Daemon that you want to STOP(namenode/datanode) : ")
		os.system("hadoop-daemon.sh stop {}" .format(name1))
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 5:
		path = '/etc/hadoop'
		os.chdir(path)
		os.system("vi core-site.xml")
		os.system("vi hdfs-site.xml")
		os.system("hadoop fs -ls /")
		name1 = input("Enter your file name : ")
		os.system("vi {}" .format(name1))
		os.system("hadoop fs -put {} /" .format(name1))
		os.system("hadoop fs -cat /{}" .format(name1))
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 6:
		name1 = input("Enter the name of file which you want to remove : ")
		os.system("hadoop fs -rm /{}" .format(name1))
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 7:
		path = '/var/www/html'
		os.chdir(path)
		name1 = input("Enter the file name for web page with(.html)extension : ")
		os.system("vi {}" .format(name1))
		os.system("ls")
		os.system("systemctl start httpd")
		os.system("systemctl status httpd")
		os.system("ifconfig")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 8:
		os.system("systemctl stop httpd")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 9:
		os.system("fdisk -l")
		Disk1 = input("\nEnter the name of 1st Hardisk that you want to use to create PV : ")
		os.system("pvcreate {}" .format(Disk1))
		os.system("pvdisplay {}" .format(Disk1))
		Disk2 = input("\nEnter the name of 2nd Hardisk that you want to use to create PV : ")
		os.system("pvcreate {}" .format(Disk2))
		os.system("pvdisplay {}" .format(Disk2))
		print("\n\t\t.........Physical Volume Created Successfully.........")
		name1 = input("\nEnter the name For your Volume Group(VG) : ")
		os.system("vgcreate {} {} {}" .format(name1,Disk1,Disk2))
		os.system("vgdisplay {}" .format(name1))
		print("\n\t\t.........Volume Group Created Successfully............")
		name2 = input("\nEnter the name for your Logical Volume(LV) : ")
		size1 = input("Enter the size(in GB) for your LV : ")
		os.system("lvcreate --size {} --name {} {}" .format(size1,name2,name1))
		os.system("lvdisplay {}/{}" .format(name1,name2))
		print("\n\t\t.........Logical Volume Created Successfully............")
		os.system("mkfs.ext4 /dev/{}/{}" .format(name1,name2))
		print("\n\t\t.........Logical Volume Formatted Successfully............")
		name3 = input("\nEnter the name for your folder that you want to mount : ")
		os.system("mkdir {}" .format(name3))
		os.system("mount /dev/{}/{} {}" .format(name1,name2,name3))
		os.system("df -h")
		print("\n\t\t.........Logical Volume Mounted Successfully............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 10:
		size1 = input("Enter the size(in GB)that you want to extend : ")
		name1 = input("Enter the name of your VG : ")
		name2 = input("Enter the name of your LV : ")
		os.system("lvextend --size +{} /dev/{}/{}" .format(size1,name1,name2))
		os.system("lvdisplay {}/{}" .format(name1,name2))
		print("\n\t\t.........Logical Volume Extended Successfully............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 11:
		name1 = input("Enter the name of your VG : ")
		name2 = input("Enter the name of your LV : ")
		os.system("resize2fs /dev/{}/{}" .format(name1,name2))
		print("\n\t\t.........Newly Extended Partition Formatted Successfully............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 12:
		os.system("aws --version")
		os.system("aws configure")
		name1 = input("Enter the key-pair name : ")
		name2 = input("Enter the security group name : ")
		name3 = input("Enter the description for your security group : ")
		os.system("aws ec2 create-key-pair --key-name {}" .format(name1))
		os.system("aws ec2 create-security-group --group-name {} --description {}" .format(name2,name3))
		print("\n.........key pair and security group created successfully........")
		name3 = input("Enter the image id : ")
		name4 = input("Enter the subnet id : ")
		name5 = input("Enter the security group id : ")
		os.system("aws ec2 run-instances --image-id ami-{} --instance-type t2.micro --count 1 --subnet-id subnet-{} --security-group-ids {} --key-name 			{}" .format(name3,name4,name5,name1))
		print("\n\t\t.........AWS instance launched successfully............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 13:
		size1 = input("Enter the size of EBS volume : ")
		os.system("aws ec2 create-volume --availability-zone ap-south-1a --size {} --volume-type gp2" .format(size1))	
		print("\n\t\t..........EBS volume created successfully...............")
		id1 = input("Enter the volume id : ")
		id2 = input("Enter the instance id : ")
		os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf" .format(id1,id2))	
		print("\n\t\t..........EBS volume attached successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 14:
		n1 = input("Enter your bucket name : ")
		n2 = input("Enter region for your bucket :")
		os.system("aws  s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint={}" .format(n1,n2))
		print("\n\t\t..........s3 bucket created successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 15:
		name1 = input("Enter the bucket name : ")
		name2 = input("Enter the object name : ")
		os.system("aws s3api put-object-ac1 --bucket {} --key {} --grant-read uri=http://acs.amazonaws.com/groups/global/			     			AllUsers" .format(name1,name2))
		print("\n\t\t..........object is uploaded successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 16:
		name1 = input("Enter the bucket name : ")
		name2 = input("Enter the object name : ")
		os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}" .format(name1,name2))
		print("\n\t\t..........cloud front created successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 17:
		os.system("yum list docker-ce")
		os.system("systemctl start docker")
		os.system("systemctl status docker")
		print("\n\t\t..........docker started successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 18:
		name1 = input("Enter the image name that you want to pull(image name:version) : ")
		os.system("docker pull {}" .format(name1))
		os.system("docker images")
		name2 = input("Enter the name for your docker container : ")
		os.system("docker run -it --name {} {}" .format(name2,name1))
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 19:
		name1 = input("Enter your docker container name that you want to stop : ")
		os.system("docker stop {}" .format(name1))
		print("\n\t\t..........docker container stopped successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 20:
		name1 = input("Enter the container name that you want to start : ")
		os.system("docker start {}" .format(name1))
		os.system("docker attach {}" .format(name1))
		print("\n\t\t..........docker container started successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 21:
		name1 = input("Enter the container name that you  want to remove permently : ")
		os.system("docker rm {}" .format(name1))
		print("\n\t\t..........docker container removed successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 22:
		name1 = input("Enter the image name that you want to remove(image:version) : ")
		os.system("docker rmi {}" .format(name1))
		print("\n\t\t..........container image removed successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 23:
		os.system("systemctl stop docker")
		os.system("systemctl status docker")
		print("\n\t\t..........docker stopped successfully...............")
		input("\npress Enter for Menu List : ")
		os.system("clear")
	elif ch == 24:
		exit()
	else:
		print("Enter the correct choice : ")

