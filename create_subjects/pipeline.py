import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import config

# ----------------------------------------------------------------------------------------
# Import config settings

python = config.python
working_dir = config.working_dir
infolder = config.infolder
outfolder = config.outfolder
metadata=config.metadata_fn

print("Started.\nYour settings:")
print(python)
print(working_dir)
print(infolder)
print(outfolder)
print(metadata)
print("\n")

if not os.path.isdir(outfolder):
    print("Output folder not found.\nCreating default output folder at " + outfolder)
    os.system("cd " + infolder)
    os.system("mkdir -p {}".format(outfolder))
    os.system("cd ..")
# ----------------------------------------------------------------------------------------
# Extract CHN chunks
print("Extracting CHN chunks from recordings...")
cmd1 = "{} {}seg_original.py {} {}".format(python, working_dir, infolder, "def")
os.system(cmd1)
# ----------------------------------------------------------------------------------------

# Extract clips
print("Trimming clips into 500ms chunks...")
cmd2 = "{} {}extract_chunks.py -i {} -o {} -md {}".format(python, working_dir, infolder+"/output/", outfolder,metadata)
os.system(cmd2)

# ----------------------------------------------------------------------------------------
# Write metadata
print("\nWriting metadata...")
with open(outfolder + metadata, 'r') as file:
    data = file.readlines()
    for i, line in enumerate(data):
        line_new = line.split("\t")
        key = line_new[1].split("_")[1]
        age = line_new[1].split("_")[2]
        its = "_".join(line_new[1].split("_")[3:6])
        data[i] = line_new[0] + "\t{}\t{}\t{}\n".format(key, age, its)
        with open(outfolder + metadata, 'w') as f:
            f.writelines(data)
print("Done.")
