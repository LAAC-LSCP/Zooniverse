import os,sys,inspect
import subprocess
import glob
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import config

outdir = config.outfolder
dataset_name=config.dataset_name
extracts_dir=outdir+dataset_name+"_for_upload"
extracts_batches = glob.glob(extracts_dir+"/*batch*/", recursive=True)

print("Started.\nYour batches:")

for batch in extracts_batches:
    os.chdir(batch)
    batch_name=os.path.basename(os.path.normpath(batch))
    print("Processing {}".format(batch_name))
    os.system("printf \"Name,Type\n\" > manifest.csv;")
    os.system("for i in *.mp3; do printf \"$i,lenas\n\" >> manifest.csv ; done")
    print("Creating a new subject set")
    subj_set=subprocess.getoutput("panoptes subject-set create 10073 "+batch_name).split(" ")[0]
    if subj_set == "Traceback":
        print("ERROR! Batch name already exists. Please choose a different name of remove the existing one from Zooniverse.")
        continue
    os.system("panoptes subject-set upload-subjects "+subj_set+ " manifest.csv")

    print("Uploading subjects")
