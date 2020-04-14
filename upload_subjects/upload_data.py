# activate virtualenv
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import config


extracts_dir = config.outfolder
batch_name = config.batch_name 

print("Started.\nYour settings:")
print(extracts_dir)
print(batch_name)
print("\n")

os.chdir(extracts_dir)
os.system("printf \"Name,Type\n\" >> manifest.csv;")
os.system("for i in *.mp3; do printf \"$i,lenas\n\" >> manifest.csv ; done")
print("configure zooniverse credentials: ")
os.system("panoptes configure")

print("Create new subject set")
os.system("panoptes subject-set create 10073 "+ batch_name)
subj_set = input("What is the subject set number?")
os.system("panoptes subject-set upload-subjects "+subj_set+ " manifest.csv")

print("Uploading subjects")
