#Configuration options for extracting chunks and writing metadata

config = {
	"python":"python",
	"working_dir": "/scratch2/csemenzin/lena_elisa/", # working directory
    "scripts":"/scratch2/csemenzin/lena_elisa/scripts/", 
    "praat": "praat", # path to praat exe
    "infolder": "/scratch2/csemenzin/lena_elisa/output/", # folder with its and wav files
    "outfolder": "/scratch2/csemenzin/lena_elisa/output/extracts/", # folder to extract output
    "metadata_fn":"MetaData_prova.txt", # metadata filename
    "make_folders":False
}

#import databaseconfig as cfg
#cfg.config["working_dir"]
