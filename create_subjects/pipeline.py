import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import config
# ----------------------------------------------------------------------------------------
# Import config settings

python = sys.executable
infolder = config.infolder
metadata="Metadata_{}.txt".format(config.dataset_name)
working_dir=os.path.join(os.getcwd()+os.sep)

#intermfolder="{}/{}_intermediate/".format(config.outfolder,config.dataset_name)
intermfolder=os.path.join(config.outfolder,config.dataset_name+"_intermediate"+os.sep)
outfolder=os.path.join(config.outfolder,config.dataset_name+"_for_upload"+os.sep)

print("Started.\nYour settings:")
print(python)
print(infolder)
print(outfolder)
print(metadata)
print("\n")

os.makedirs(intermfolder, exist_ok=True)
os.makedirs(outfolder, exist_ok=True)
# ----------------------------------------------------------------------------------------
# Extract CHN chunks
print("Extracting CHN chunks from recordings...")
cmd1 = "{} {}seg_original.py {} {}".format(python, working_dir, infolder, intermfolder, "def")
os.system(cmd1)
# ----------------------------------------------------------------------------------------

# Extract clips
print("Trimming clips into 500ms chunks...")
cmd2 = "{} {}extract_chunks.py -i {} -o {} -md {}".format(python, working_dir, intermfolder, outfolder, metadata)
os.system(cmd2)

# ----------------------------------------------------------------------------------------
# Write metadata
print("\nWriting metadata...")
with open(outfolder + metadata, 'r') as file:
    data = file.readlines()
    for i, line in enumerate(data[1:]):
        line_new = line.split("\t")
        key = line_new[1].split("_")[1]
        age = line_new[1].split("_")[2]
        its = "_".join(line_new[1].split("_")[3:6])
        onset=line_new[1].split("_")[6]
        offset=line_new[1].split("_")[7].strip(".wav")
        chunk_position=line_new[2]
        data[i+1] = line_new[0] + "\t{}\t{}\t{}\t{}\t{}\t{}".format(key, age, its,onset,offset,chunk_position)
        with open(outfolder + metadata, 'w') as f:
            f.writelines(data)
print("Done.")
