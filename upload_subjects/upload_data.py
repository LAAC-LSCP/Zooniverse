# activate virtualenv
import os
os.system("source activate zooniverse")

path="/scratch2/csemenzin/lena_files/output/"
for d in folders:
	current_dir=path+d+"/extracts/"
	print("Create new subject set")
	os.system("panoptes subject-set create 10073 "+str(current_dir))
	subj_set = raw_input("What is the subject set number?")
	os.system("panoptes subject-set upload-subjects "+subj_set) 
	print("uploading subjects")

#panoptes info
#assign to variable?

# TODO: Save panoptes output to py variable 
#import subprocess
#proc=subprocess.Popen('echo "to stdout"', shell=True, stdout=subprocess.PIPE, )
#output=proc.communicate()[0]
#print output
