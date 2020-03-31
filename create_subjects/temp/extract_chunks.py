#import os

folders = (f for f in os.listdir("/scratch2/csemenzin/lena_files/output/")
         if os.path.isdir(os.path.join("/scratch2/csemenzin/lena_files/output/", f)))

for d in folders:
	outfolder="/scratch2/csemenzin/lena_files/output/"+d+"/extracts/"
	#os.system("praat -run extract_chunks_4ms.PraatScript "+infolder+" "+outfolder
	cmd="praat --run extract_chunks_4ms.PraatScript "+d+" "+outfolder
	print(cmd)