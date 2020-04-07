#Configuration options for extracting chunks and writing metadata

config = {
	"python":"python",
	"working_dir": "/scratch2/csemenzin/lena_elisa/", # folder with its and wav files
    "scripts":"/scratch2/csemenzin/lena_elisa/scripts/", #dir with scripts
    "praat": "praat", # path to praat exe
    "infolder": "/scratch2/csemenzin/lena_elisa/output/", # folder to extract first segmentation
    "outfolder": "/scratch2/csemenzin/lena_elisa/output/extracts/", # folder to extract final clips
    "metadata_fn":"praat_metadata.txt", # default; not yet implemented - change filename in praat script
}
