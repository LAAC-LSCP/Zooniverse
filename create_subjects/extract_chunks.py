import sys
import os
import random
import string
from pydub import AudioSegment
from pydub.utils import make_chunks
import random
import datetime
import argparse

parser = argparse.ArgumentParser(description='Process extracted clips')
parser.add_argument('-i',"--infolder", type=str,
                     help='folder containing the clips to segment')
parser.add_argument('-o',"--outfolder", type=str,
                     help='folder where to extract the clips')
parser.add_argument('-md',"--metadata", type=str,
                     help='name of the metadata file to write')

args = parser.parse_args()
infolder=args.infolder
outfolder=args.outfolder
md_filename=args.metadata


if not os.path.exists(outfolder):
    os.system("mkdir -p {}".format(outfolder))


def load_audio(audio):
    init = datetime.datetime.now()
    print("loading audio")
    fullAudio = AudioSegment.from_wav(audio)
    print("audio loaded in ", datetime.datetime.now()-init, " min.sec.ms")
    return fullAudio

def write_metadata(md_filename,audioname,chunk):
    with open(outfolder+md_filename,"a") as fn:
        fn.write("{}\t{}\n".format(audioname,chunk))

def segment(audio,orig_filename):
    chunk_length_ms = 0.5 * 1000
    chunks = make_chunks(audio, chunk_length_ms)
    # Export all of the individual chunks as wav files
    for i, chunk in enumerate(chunks):
    # Get rid of edge clicks by fading in and out
        fade_chunk=chunk.fade_in(10).fade_out(10)
        filename=''.join(random.choices(string.digits, k=10))
        chunk_name = "{}{}.wav".format(outfolder,filename)
        write_metadata(md_filename,filename,orig_filename)
        print("exporting", chunk_name)
        fade_chunk.export(chunk_name, format="wav")
#_________________________________________

if __name__ == "__main__":
    processed_files=[]
    for filename in sorted(os.listdir(infolder)):
        if filename.endswith(".wav") and filename not in processed_files:
            processed_files.append(filename)
            full_audio=load_audio(infolder+"/"+filename)
            segment(full_audio,filename)

