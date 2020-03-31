import os
from glob import glob
import shutil

infolder="/scratch2/csemenzin/lena_files/output/"
# Read child info from filenames
files = (file for file in os.listdir(infolder)
         if os.path.isfile(os.path.join(infolder, file)))

for rec in files:
	rec=rec.strip(".wav")
	fields=rec.split("_")
	print(fields)
	child_key=fields[1] #extract ck
	child_age=fields[2] #extract age
	outfolder="/scratch2/csemenzin/lena_files/output/"+child_key+"_"+child_age+"/"
	if not os.path.isdir(outfolder):
		os.system("mkdir "+ outfolder) #mkdir with filename
	for data in glob(infolder+"*"+child_key+"*"): # move filenames with same key 
		shutil.move(data,outfolder)

#----------------------------------------------------------------------------------------
# Call Praat script
os.system("module load praat")

folders = (f for f in os.listdir("/scratch2/csemenzin/lena_files/output/")
         if os.path.isdir(os.path.join("/scratch2/csemenzin/lena_files/output/", f)))

for d in folders:
	outfolder="/scratch2/csemenzin/lena_files/output/"+d+"/extracts/"
	#os.system("praat -run extract_chunks_4ms.PraatScript "+infolder+" "+outfolder
	cmd="praat --run extract_chunks_4ms.PraatScript "+d+" "+outfolder
	print("extracting chunks from {}...".format(d))
	os.system(cmd)
	os.system("./convert_2_mp3.sh")
#	os.system("rm *wav")

#----------------------------------------------------------------------------------------
# WRITE METADATA

folders = (f for f in os.listdir("/scratch2/csemenzin/lena_files/output/")
         if os.path.isdir(os.path.join("/scratch2/csemenzin/lena_files/output/", f)))
for d in folders:
	print("Writing from ",d)
	fields=d.split("_")
	key=fields[0]
	age=fields[1]
	i=0
	filelist=glob("/scratch2/csemenzin/lena_files/output/"+d+"/extracts/*.mp3")
	for rec in filelist:
		i+=1
		print("Writing metadata for recording ",i)
		with open("MetaData.txt","a") as fp:
			fp.write(key+","+age+","+rec+"\n")


