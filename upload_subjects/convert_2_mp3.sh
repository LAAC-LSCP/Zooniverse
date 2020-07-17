outfolder=`grep "outfolder" ../config.py | awk '{ gsub(".*=", "") ; system( "echo "  $0) }'`

echo Converting WAV files to MP3 using SOX...
#CONVERT TO MP3

for filename in "$outfolder"/*for_upload/*batch*/*.wav;
do echo "${filename%.*}";
sox "${filename%.*}".wav "${filename%.*}".mp3;
done

#REMOVE WAVs

#for filename in $outfolder/data-for-upload/*.wav;
#do rm $filename;
#done
