echo Converting WAV files to MP3 using SOX...

#CONVERT TO MP3

for filename in *.wav;
do echo "${filename%.*}";
sox "${filename%.*}".wav "${filename%.*}".mp3;
done

#REMOVE WAVs

for filename in *.wav;
do rm $filename;
done