#----------------- Tilak--------------------
#----------------------------------------------
import boto3
from time import gmtime, strftime
s3=boto3.resource('s3')
client=boto3.client('s3')
src_bucket_name='lgbucketaws3'
dst_bucket_name='lgbucketaws4'
bucket=s3.Bucket(src_bucket_name)
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
count=0
chngdir=0
for key in bucket.objects.all():
	path=key.key
	path=path.split('/')
	width=8
	dst_path=0
	yahoo="yahoo"
	cert="cert.jpg"
	ds_store=".DS"
	if yahoo in file_name and cert not in filename:
				dst_path=file_name[1]
				dst_path=(width-len(dst_path))*"0"+str(dst_path)
				dst_path=dst_path[0:3]+'/'+'yahoo_'+dst_path+'_01.jpg'
			if cert in filename:
				dst_path=file_name[1]
				dst_path=(width-len(dst_path))*"0"+str(dst_path)
				dst_path=dst_path[0:3]+'/'+'yahoo_'+dst_path+'_02.jpg'
			if yahoo in file_name and cert not in filename:
				dst_path=file_name[0]
				dst_path=(width-len(dst_path))*"0"+str(dst_path)
				dst_path=dst_path[0:3]+'/'+'yahoo_'+dst_path+'_01.jpg'		
		if dst_path!=0:
			copy_source={'Bucket':src_bucket_name, 'Key':key.key}
			client.copy(copy_source,dst_bucket_name,dst_path)
			chngdir=chngdir+1
		count=count+1
	print strftime("%Y-%m-%d %H:%M:%S", gmtime())
	print "Files copied:",count
	print "Files directory changed:",chngdir


#----------------- Tilak--------------------
#----------------------------------------------
#-------------Making an API call---------------

aws s3api list-objects --bucket lgbucketaws3 --output text >> test.text
import boto3
client= boto3.client('s3')
src_bucket_name='lgbucketaws3'
dst_bucket_name='lgbucketaws4'
count=0
from time import gmtime,strftime
print strftime("%Y-%m-%d %H:%M:%S",gmtime())
def src_bucket():
	src_file_path=[]
	src_file_name=[]
	with open("/Users/tilak/Desktop/python/test.txt") as f:
		lines=f.readlines()
		ifind=".jpg"
		islash="/"
		for line in lines:
			if ifind in line:
				icon=line.split()[2]
				src_file_path.append(icon)
				idot=icon.split("/")[5]
				src_file_name.append(idot)
	return src_file_path, src_file_name

src_file_path, src_file_name=src_bucket()

def dst_bucket():
	dst_file_path=[]
	dst_file_name=[]
	width=8
	yahoo="yahoo"
	cert="cert.jpg"
	for i,jtemp in enumerate(src_file_name):
		jtemp=jtemp.split('/')
		temp=jtemp[0]
		if yahoo in jtemp:
			temp=jtemp[1]
		temp=(width-len(temp))*"0"+str(temp)
		if cert in jtemp:
			temp=temp[0:3]+'/'+'yahoo_'+temp+'_02.jpg'
		elif yahoo in jtemp:
			temp=temp[0:3]+'/'+'yahoo_'+temp+'_01.jpg'	
		else
			atemp=jtemp[1]
			temp=temp[0:3]+'/'temp+'_0'+jtemp[1]
		dst_file_path.append(temp)
	returm dst_file_path

dst_file_path=dst_bucket()

for i,jtemp in enumerate(dst_file_path):
	print src_file_path[i]+"------->"+jtemp
	count=count+1
	copy_source={'Bucket': src_bucket_name,'Key':src_file_path[i]}
	client.copy(copy_source,dst_bucket_name,jtemp)
print"Total Files Converted:", count
print strftime("%Y-%m-%d %H:%M:%S",gmtime())












































































