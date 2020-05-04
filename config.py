#Configuration options for extracting chunks and writing metadata
# IMPORTANT!!! Don't forget to put a "/" at the end of each path, and make sure the path does not include spaces.

python = "python"
#leave it as python if your only python version is python3; or use python3 if you have several so that python3 is used

infolder = "/Users/chiarasemenzin/Desktop/create_temp/sample_data/"
# folder with your source its and wav files

outfolder =  "/Users/chiarasemenzin/Documents/Zooniverse-data/"
# folder where output will be saved 
# this will create two folders: 
# - an intermediate/ folder with extracted CHN chunks
# - a data-for-upload/ folder with the final short clips

metadata_fn = "MetaData_LAAC_20200418_ac1.txt"
# metadata filename, choose anything you'd like since it will be created in the process

batch_name = "LAAC_20200418_ac1"
#name that will be used to label the batch during uploading, choose anything you want as long as there are no spaces and it is unique (i.e., it will not have been used by you or any others in the past). NOTE! You cannot use the same name twice (i.e., for two subsequent uploads).


