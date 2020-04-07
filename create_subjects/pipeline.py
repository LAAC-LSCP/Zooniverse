import os
import config as cfg

#----------------------------------------------------------------------------------------
# Import config settings

python=cfg.config["python"]
working_dir=cfg.config["working_dir"]
scripts=cfg.config["scripts"]
infolder=cfg.config["infolder"]
outfolder=cfg.config["outfolder"]
praat=cfg.config["praat"]
#md_fn=cfg.config["metadata_fn"]

print("Started.\nYour settings:")
for k,v in cfg.config.items():
    print(k,v)

if not os.path.isdir(outfolder):
    print("\nCreating default output folder..."+outfolder)
    os.system("mkdir "+infolder+"output/")
    os.system("mkdir "+infolder+"output/"+"extracts/")
#----------------------------------------------------------------------------------------
# Extract CHN chunks
print("Extracting CHN chunks from recordings...")
cmd1="{} {}seg_original.py {} {}".format(python,scripts,working_dir,"def")
os.system(cmd1)
#----------------------------------------------------------------------------------------
# Extract clips
print("Trimming clips into 500ms chunks...")
cmd2="{} --run {}extract_chunks_md.PraatScript {} {}".format(praat,scripts,infolder,outfolder)
os.system(cmd2)
#----------------------------------------------------------------------------------------
# Write metadata
print("Writing metadata...")
with open(outfolder+'metadata_praat.txt', 'r') as file:
	data = file.readlines()
	for i,line in enumerate(data):
		line_new=line.split("\t")
		key = line_new[1].split("_")[0]
		age = line_new[1].split("_")[1]
		its = line_new[1].split("_")[2:6]
		data[i] = line_new[0]+"\t{}\t{}\t{}\n".format(key, age, its)
		with open('metadata_praat.txt', 'w') as f:
			f.writelines(data)
print("Done.")
#TODO: add gender
