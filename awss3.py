#This  is Lambda function and can be copied inside the function console and set a trigger to the bucket to copy from the source
# File name is taken and changed to directory
# yahoo_12345_1.jpg, yahoo_12345_cert.jpg, 1234_1.jpg
# 
import boto3
s=boto3.resource('s3')
bucket ='lgbucketaws3'
bucket=boto3.client('s3')
src_bucket_name='lgbucketaws3'
dst_bucket_name='lgbucketaws4'
bucket=s3.Bucket(src_bucket_name)

def lambda_handler(event, context):
	count =0
	chngdir=0
	for key in bucket.objects.all();
	path=key.key
	path=path.split('/')
	width=8
	dst_path=0
	yahoo="yahoo"
	cert="cert.jpg"
	ds_store=".DS"
	for i in path:
		if i.endswith(".jpg"):
			file_name=i.spit('_')
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
	print "Files copied:",count
	print "Files directory changed:",chngdir


