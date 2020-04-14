#Configuration options for extracting chunks and writing metadata
# IMPORTANT!!! Don't forget to put a "/" at the end of each path, and make sure the path does not include spaces.

config = {
	"python":"python3", #leave it as python if your only python version is python3; or use python3 if you have several so that python3 is used
	"working_dir": "/Users/acristia/Documents/gitrepos/Zooniverse/create_subjects/", # working directory, point to the Zooniverse/create_subjects/ you created by cloning this repo
    "infolder": "/Users/acristia/Documents/PNG-data/", # folder with your source its and wav files
    "outfolder": "/Users/acristia/Documents/PNG-data-for-upload/", # folder to extract output to
    "metadata_fn":"MetaData_2019png_LENA_postCristia.txt", # metadata filename, choose anything you'd like since it will be created in the process
}

