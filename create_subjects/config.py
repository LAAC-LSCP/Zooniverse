#Configuration options for extracting chunks and writing metadata

config = {
	"python":"python",
	"working_dir": "/scratch2/csemenzin/lena_elisa/", # working directory
    "scripts":"/scratch2/csemenzin/lena_elisa/scripts/", #dir with scripts
    "praat": "praat", # path to praat exe
    "infolder": "/scratch2/csemenzin/lena_elisa/output/", # folder with its and wav files
    "outfolder": "/scratch2/csemenzin/lena_elisa/output/extracts/", # folder to extract output
    "metadata_fn":"praat_metadata.txt", # default; not yet implemented - change filename in praat script
}
