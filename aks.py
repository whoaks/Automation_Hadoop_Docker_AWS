import os


print('\t\t\t\t\t\t     Automation Configuration    ')
print("\t\t\t\t\t\t-------------------------------- ")
print()
print()



def core_site():
    print('Enter NameNode IP Address :-   ', end='')
    NN_ip=input()
   
    os.system('echo \<configuration\> >> core-site.xml')
    os.system('echo \<property\> >> core-site.xml')
    os.system('echo \<name\>fs.default.name\<\/name\> >> core-site.xml')
   
    if cmd=='1':
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
    else:
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
   
    os.system('echo \</property\> >> core-site.xml')
    os.system('echo \<\/configuration\> >> core-site.xml')
   
    if cmd=='2':
        os.system('scp core-site.xml {}:/etc/hadoop/core-site.xml'.format(remote_ip))
    else:
        os.system('cp core-site.xml /etc/hadoop/core-site.xml')
    os.system('rm -rf core-site.xml')
    os.system('cp temp.xml core-site.xml')



def hdfs_site():
    
    if cmd2=='6':
        print('Enter DataNode Directory name you want to provide to NN :-   ' ,end='')
    
    elif cmd2=='5':
        print('Enter NameNode Directory name you want to create :-   ' ,end='')
    
    dir_name=input()
    
    if cmd=='2':
        os.system('ssh {} mkdir {}'.format(remote_ip , dir_name))
    #else:
        #os.system('mkdir {}'.format(dir_name))
    os.system('echo \<configuration\> >> hdfs-site.xml')
    os.system('echo \<property\> >> hdfs-site.xml')
    
    if cmd2=='6':
        os.system('echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml')
    elif cmd2=='5':
        os.system('echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml')
    os.system('echo \<value\>{}\<\/value\> >> hdfs-site.xml'.format(dir_name))
    os.system('echo \</property\> >> hdfs-site.xml')
    os.system('echo \<\/configuration\> >> hdfs-site.xml')
    if cmd=='2':
        os.system('scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml'.format(remote_ip))
    else:
        os.system('cp hdfs-site.xml /etc/hadoop/hdfs-site.xml')
    os.system('rm -rf hdfs-site.xml')
    os.system('cp temp2.xml hdfs-site.xml')

while True:
    print("\t\t\t\t\tPress 1 to Configure Local Server\n\t\t\t\t\tPress 2 to Configuring Remote Server")
    print("\t\t\t\t\tPress 3 to Configure AWS Cloud")
    print('\t\t\t\t\tPress 4 to Prediction Automation')
    print('\t\t\t\t\tPress 5 to Automate Docker Container')
    print('\t\t\t\t\tPress 0 to Exit')
    print('\t\t\t\t\t\t => ', end='')
    cmd=input()
    print()

    if cmd=='1':

        print('\t\t\t\t\tpress 1 to Show Date \n\t\t\t\t\tpress 2 to Show Calender')
        print('\t\t\t\t\tpress 3 to Run Any Linux Command')
        print('\t\t\t\t\tpress 4 to Configure WebServer')
        print('\t\t\t\t\tpress 5 to Configure and Start NameNode')
        print('\t\t\t\t\tpress 6 to Configure and Start DataNode')
        print('\t\t\t\t\tpress 7 to Create Virtual Group')
        print('\t\t\t\t\tpress 8 to Creation of  Logical Volume')
        print('\t\t\t\t\tpress 9 to Attach More Harddisks to Virtual Group dynamically')
        print('\t\t\t\t\tpress 10 to Add Logical Volume ( Partition ) Size dynamically')
        print('\t\t\t\t\tpress 11 to Configure WebServer inside Docker Container')
        print('\t\t\t\t\tpress 12 to Go Back to Previous Menu')
        print('\t\t\t\t\t\t =>  ', end='')
        cmd2=input()
        print()

        if cmd2=='1':
            os.system("sudo date")
    
        elif cmd2=='2':
            os.system('sudo cal')
    
        elif cmd2=='3':
            print('Enter Linux Command :-   ' , end='')
            linux_cmd=input()
            os.system('sudo {}'.format(linux_cmd))
    
        elif cmd2=='4':
            os.system('yum install httpd -y')
            os.system('systemctl start httpd')
            os.system('systemctl enable httpd')
            os.system('cp index.html /var/www/html')
    
        elif cmd2=='5':
            os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
            os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
            hdfs_site()
            core_site()
            os.system('hadoop namenode -format')
            os.system('hadoop-daemon.sh start namenode')
            os.system('jps')
    
        elif cmd2=='6':
            os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
            os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
            hdfs_site()
            core_site()
            os.system('sudo hadoop-daemon.sh start datanode')
            os.system('sudo jps')

        elif cmd2=='7':
            print('Enter First Device name to create Logical Volume :-  ',end='')
            device1=input()
            print('Enter Second Device name to create Logical Volume :-  ',end='')
            device2=input()
            os.system('sudo pvcreate {}'.format(device1))
            os.system('sudo pvcreate {}'.format(device2))
            print('Please Enter  name to create Virtual Group :-  ', end='')
            vg_name=input()
            os.system('sudo vgcreate {} {} {}'.format(vg_name , device1 , device2))
            os.system('sudo vgdisplay {}'.format(vg_name))

        elif cmd2=='8':
            print('Enter Partition Size :-  ', end='')
            partition_size = input()
            print('Enter LV Name to assign to partition :-  ',end='')
            lv_name = input()
            print('Enter Virtual Group Name to create partition :- ' , end='')
            vg_name = input()
            os.system('sudo lvcreate --size {}G --name {} {}'.format(partition_size , lv_name , vg_name))
            os.system('sudo mkfs.ext4 /dev/{}/{}'.format(vg_name , lv_name))
            print('Enter directory name to mount Logical Volume :-  ', end='')
            dir_name=input()
            os.system('sudo mkdir {}'.format(dir_name))
            os.system('sudo mount /dev/{}/{} {}'.format(vg_name , lv_name , dir_name))
            os.system('sudo df -h')
       
        elif cmd2=='9':
            print('Please Enter Device Name to attach to the Virtual Group :-  ', end='')
            device_name=input()
            os.system('sudo pvcreate {}'.format(device_name))
            print('Please Enter Virtual Group Name to extend its size :-  ', end='')
            vg_name=input()
            os.system('sudo vgextend {} {}'.format(vg_name , device_name))
            os.system('sudo vgdisplay {}'.format(vg_name))

        elif cmd2=='10':
            print('Please Enter size to increase the Logical Volume Size online :-  ' ,end='' )
            size=input()
            print('Please Enter Virtual Group Name to extend its size :-  ', end='')
            vg_name=input()
            print('Please Enter Logical Volume Name to extend its size :-  ', end='')
            lv_name=input()
            os.system('sudo lvextend --size +{}G /dev/{}/{}'.format(size , vg_name , lv_name))
            os.system('sudo resize2fs /dev/{}/{}'.format(vg_name , lv_name ))
            os.system('sudo df -h')

        elif cmd2=='11': #docker
            print('Please Enter Container Name :-  ', end='')
            con_name=input()
            print('Please Enter Image Name :-  ', end='')
            image_name=input()
            print('Enter Port Number to Expose the WebServer running on the top of Docker :-  ', end='')
            port=input()
            os.system('sudo docker run -dit --name {} -p {}:80 {}'.format(con_name , port , image_name))
            os.system('sudo docker exec -it {} yum install httpd -y'.format(con_name))
            os.system('sudo docker cp /automation/index.html {}:/var/www/html/'.format(con_name))
            os.system('sudo docker exec -it {} /usr/sbin/httpd'.format(con_name))
            os.system('sudo docker ps')
        elif cmd2=='12':
            continue;
    
        else:
            print('Please , Select above given Options . Thank You :)')
    
    elif cmd=='4':
        os.system('python3 /root/salary.py')

    elif cmd=='2':
        print("enter remote OS IP :-   ", end='')
        remote_ip=input()
    
        print('\t\t\t\t\tpress 1 to Show Date \n\t\t\t\t\tpress 2 to Show Calender')
        print('\t\t\t\t\tpress 3 to Run Any Linux Command')
        print('\t\t\t\t\tpress 4 to Configure WebServer')
        print('\t\t\t\t\tpress 5 to Configure and Start NameNode')
        print('\t\t\t\t\tpress 6 to Configure and Start DataNode')
        print('\t\t\t\t\tpress 7 to do Parition')
        print('\t\t\t\t\tpress 8 to Go back to previous Menu')
        print('\t\t\t\t\t\t =>  ', end='')
        cmd2=input()
        print()

        if cmd2=='1':
            os.system("ssh {} date".format(remote_ip))
    
        elif cmd2=='2':
            os.system('ssh {} cal'.format(remote_ip))
    
        elif cmd2=='3':
            print('Enter Linux Command :-   ' , end='')
            linux_cmd=input()
            os.system('ssh {} {}'.format(remote_ip ,linux_cmd))
    
        elif cmd2=='4':
            os.system('ssh {} yum install httpd -y'.format(remote_ip))
            os.system('ssh {} systemctl start httpd'.format(remote_ip))
            os.system('ssh {} systemctl enable httpd'.format(remote_ip))
            os.system('scp index.html {}:/var/www/html'.format(remote_ip))
    
        elif cmd2=='5':
            os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(remote_ip))
            os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
            hdfs_site()
            core_site()
            os.system('ssh {} hadoop namenode -format'.format(remote_ip))
            os.system('ssh {} hadoop-daemon.sh start namenode'.format(remote_ip))
            os.system('ssh {} jps'.format(remote_ip))
    
        elif cmd2=='6':
            os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(remote_ip))
            os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
            hdfs_site()
            core_site()
            os.system('ssh {} hadoop-daemon.sh start datanode'.format(remote_ip))
            os.system('ssh {} jps'.format(remote_ip))
            os.system('ssh {} hadoop dfsadmin -report'.format(remote_ip))

        elif cmd2=='7':
            os.system('ssh {} fdisk -l'.format(remote_ip))
            os.system('ssh {} fdisk /dev/xvdf'.format(remote_ip))
            os.system('ssh {} mkfs.ext4 /dev/xvdf3'.format(remote_ip))
            print('\t\t\t\tEnter name of Directory to mount the HDs')
            dirname=input()
            os.system('ssh {} mkdir {}'.format(remote_ip , dirname))
            os.system('ssh {} mount /dev/xvdf3 {}'.format(remote_ip , dirname))
            os.system('ssh {} df -h'.format(remote_ip))
        elif cmd2=='8':
            continue

        else:
            print('Select options as mention')
    elif cmd=='3':
        print('\t\t\t\t\tPress 1 to Create Key Pair')
        print('\t\t\t\t\tPress 2 to Create Security Group')
        print('\t\t\t\t\tPress 3 to Add Ingress Rules to Existing Security Group')
        print('\t\t\t\t\tPress 4 to Launch Instance on Cloud')
        print('\t\t\t\t\tPress 5 to Create EBS Volume')
        print('\t\t\t\t\tPress 6 to Attach EBS Volume to EC2 Instance')
        print('\t\t\t\t\tPress 7 to Configure WebServer')
        print('\t\t\t\t\tPress 8 to Create Static Partiton and Mount /var/www/html folder on EBS volume')
        print('\t\t\t\t\tPress 9 to Create S3 Bucket')
        print('\t\t\t\t\tPress 10 to put Object inside S3 bucket and make it public accessible')
        print('\t\t\t\t\tPress 11 to remove specific Object from S3 bucket')
        print('\t\t\t\t\tPress 12 to delete Specific S3 Bucket')
        print('\t\t\t\t\tPress 13 to create Cloudfront distribution providing S3 as Origin')
        print('\t\t\t\t\tPress 14 to delete Key Pair')
        print('\t\t\t\t\tPress 15 to Stop EC2-Instances')
        print('\t\t\t\t\tPress 16 to Start Ec2-Instances')
        print('\t\t\t\t\tPress 17 to terminate Ec2-Instances')
        print('\t\t\t\t\tPress 18 to delete Security group')
        print('\t\t\t\t\tPress 19 to Go back to previous menu')
        print('\t\t\t\t\t\t =>  ', end='')
        cmd2=input()
        if cmd2=='1':
            print('Enter key name to create :-  ', end='')
            key_name=input()
            os.system('aws ec2 create-key-pair --key-name {}'.format(key_name))
        elif cmd2=='2':
            print('Enter Security Name :-  ', end='')
            sg_name=input()
            print('Enter VPC Id :-  ', end='')
            vpc_id=input()
            os.system('aws ec2 create-security-group --group-name {} --description "SG Created" --vpc-id {}'.format(sg_name , vpc_id))
        elif cmd2=='3':
            print('Enter Security Group Id :-  ', end='')
            sg_id=input()
            print('Enter IP Protocol ( ie. tcp ) :-  ', end='')
            ip_protocol=input()
            print('Enter Port No :-  ', end='')
            port_no=input()
            cidr=input('Input Ip Ranges :-  ')
            os.system('aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions IpProtocol={},FromPort={},ToPort={},IpRanges=[{}]'.format(sg_id , ip_protocol , port_no , port_no , cidr))
        elif cmd2=='4':
            print('Enter AMI id to Launch Instance :-  ', end='')
            ami=input()
            print('Enter Instance type :-  ', end='')
            itype=input()
            print('Enter Number of Instances to launch :-  ', end='')
            count=input()
            print('Enter Security Group Id to attach to the Instance :-  ', end='')
            sg_id=input()
            print('Enter Key to attach to ec2 Instance :-  ', end='')
            key=input()
            os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id subnet-0892eab4da13f00a5 --security-group-ids {} --key-name {}'.format(ami , itype , count , sg_id , key))
        elif cmd2=='5':
            print('Enter Availablity Zone to Create EBS Volume :-  ', end='')
            az=input()
            print('Enter Size to create EBS Volume :-  ', end='')
            ebs_size=input()
            os.system('aws ec2 create-volume --availability-zone {} --size {}'.format(az , ebs_size))
        elif cmd2=='6':
            print('Enter EBS Volume ID to Attach to EC2 Instance :-  ', end='')
            ebs_vid=input()
            print('Enter EC2 Instance ID to attach EBS Volume :-  ', end='')
            ec2_id=input()
            os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ebs_vid , ec2_id))
        elif cmd2=='7':
            print('Enter Ip Address :-  ', end='')
            remote_ip=input()
            print('Enter key name to login inside Ec2 Instance :-  ', end='')
            key=input()
            os.system('ssh -l ec2-user {} -i {}.pem sudo yum install httpd -y'.format(remote_ip , key))
            os.system('ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd'.format(remote_ip , key))
            os.system('ssh -l ec2-user {} -i {}.pem sudo systemctl enable httpd'.format(remote_ip , key))
        elif cmd2=='8':
            print('Enter Ip Address to Remote Login :-  ', end='')
            ip=input()
            print('Enter Keyname :-  ', end='')
            key=input()
            os.system('ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/xvdf'.format(ip , key))
            print('Enter Partition Name to format and  Mount /var/www/html folder  :-   ', end='')
            name=input()
            os.system('ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{}'.format(ip , key , name))
            os.system('ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html'.format(ip , key , name))
        elif cmd2=='9':
            print('Enter S3 bucket name that must be unique :-  ', end='')
            s3_name=input()
            os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))
        elif cmd2=='10':
            print('Enter Object name to put inside S3 bucket :-  ', end='')
            object_name=input()
            print('Enter S3 Bucket name :-  ', end='')
            s3_name=input()
            os.system('aws s3 cp /root/{} s3://{} --acl public-read'.format(object_name , s3_name))
        elif cmd2=='11':
            print('Enter S3 bucket name :-  ', end='')
            object_name=input()
            print('Enter object name :-  ', end='')
            s3_name=input()
            os.system('aws s3 rm s3://{}/{}'.format(object_name , s3_name))
        elif cmd2=='12':
            print('Enter S3 Bucket name :-  ', end='')
            s3_name=input()
            os.system('aws s3api delete-bucket --bucket {} --region ap-south-1'.format(s3_name))
        elif cmd2=='13':
            print('Enter S3 bucket name :-  ', end='')
            s3_name=input()
            os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(s3_name))
        elif cmd2=='14':
            print('Enter key name to delete :-  ', end='')
            key_name=input()
            os.system('aws ec2 delete-key-pair --key-name {}'.format(key_name))
        elif cmd2=='15':
            print('Enter Instance id to stop Ec2 instances :-  ', end='')
            id=input()
            os.system('aws ec2 stop-instances --instance-ids {}'.format(id))
        elif cmd2=='16':
            print('Enter Instance id to start Ec2 instances :-  ', end='')
            id=input()
            os.system('aws ec2 start-instances --instance-ids {}'.format(id))
        elif cmd2=='17':
            print('Enter Instance id to terminate Ec2 instances :-  ', end='')
            id=input()
            os.system('aws ec2 terminate-instances --instance-ids {}'.format(id))
        elif cmd2=='18':
            sg_id=input('Enter Security group id you want to delete :-  ')
            os.system('aws ec2 delete-security-group --group-id {}'.format(sg_id))
        elif cmd2=='19':
            continue
        else:
            print('Please enter valid command')

    elif cmd=='5':
        print('\t\t\t\t\tPress 1 to pull image from docker hub')
        print('\t\t\t\t\tPress 2 to launch Container')
        print('\t\t\t\t\tPress 3 to know number of docker container running in local OS')
        print('\t\t\t\t\tPress 4 to know number of images in Local OS')
        print('\t\t\t\t\tPress 5 to Inspect docker Container')
        print('\t\t\t\t\tPress 6 to Stop docker container')
        print('\t\t\t\t\tPress 7 to Start docker container')
        print('\t\t\t\t\tPress 8 to remove image from local OS')
        print('\t\t\t\t\tPress 9 to delete Single docker container')
        print('\t\t\t\t\tPress 10 to delete all docker container')
        print('\t\t\t\t\tPress 11 to Configure webserver inside docker container')
        print('\t\t\t\t\tPress 12 to Go back to previous menu')
        print('\t\t\t\t\t\t =>  ', end='')
        cmd2=input()
        print()
        
        if cmd2=='1':
            os.system('python3 /docker/pull_image.py')
        elif cmd2=='2':
            os.system('python3 /docker/launch_container.py')
        elif cmd2=='3':
            os.system('python3 /docker/docker_container.py')
        elif cmd2=='4':
            os.system('python3 /docker/docker_image.py')
        elif cmd2=='5':
            os.system('python3 /docker/docker_inspect.py')
        elif cmd2=='6':
            os.system('python3 /docker/docker_stop.py')
        elif cmd2=='7':
            os.system('python3 /docker/docker_start.py')
        elif cmd2=='8':
            os.system('python3 /docker/remove_image.py')
        elif cmd2=='9':
            os.system('python3 /docker/remove_scon.py')
        elif cmd2=='10':
            os.system('python3 /docker/remove_con.py')
        elif cmd2=='11':
            print('Please Enter Container Name :-  ', end='')
            con_name=input()
            print('Please Enter Image Name :-  ', end='')
            image_name=input()
            print('Enter Port Number to Expose the WebServer running on the top of Docker :-  ', end='')
            port=input()
            os.system('sudo docker run -dit --name {} -p {}:80 {}'.format(con_name , port , image_name))
            os.system('sudo docker exec -it {} yum install httpd -y'.format(con_name))
            os.system('sudo docker cp /automation/index.html {}:/var/www/html/'.format(con_name))
            os.system('sudo docker exec -it {} /usr/sbin/httpd'.format(con_name))
            os.system('sudo docker ps')
        elif cmd2=='12':
            continue
    elif cmd=='0':
        break
    else:
        print('\n\t\t\t\t\t\t\tPlease Choose Valid Options mention above')
