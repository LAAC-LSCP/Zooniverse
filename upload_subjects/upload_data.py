# activate virtualenv
import os

###### CHANGE THESE VALUES BEFORE RUNNING!

extracts_dir="path/to/clips/folder/" #where the clips are
batch_name="default_" #change this to upload batch name to use. Cannot use the same name twice

######### end of change

os.system("cd {}".format(extracts_dir))
os.system("printf \"Name,Type\n\" >> manifest.csv;")
os.system("for i in *.mp3; do printf \"$i,lenas\n\" >> manifest.csv ; done")
print("configure zooniverse credentials: ")
os.system("panoptes configure")

print("Create new subject set")
os.system("panoptes subject-set create 10073 "+ batch_name)
subj_set = input("What is the subject set number?")
os.system("panoptes subject-set upload-subjects "+subj_set+ " manifest.csv")

print("Uploading subjects")
