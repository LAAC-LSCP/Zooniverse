from pydub import AudioSegment
from pydub.utils import make_chunks
import argparse


parser = argparse.ArgumentParser(description='Regenerate clips from metadata')
parser.add_argument('-i',"--infolder", type=str,
                    help='folder containing the .its to recover clips from')
parser.add_argument('-o',"--outfolder", type=str,
                      help='folder where to extract the clips')
parser.add_argument('-md',"--metadata", type=str,
                      help='name of the metadata file to read from')

args = parser.parse_args()
infolder=args.infolder
outfolder=args.outfolder
md_filename=args.metadata


if __name__ == "__main__":
    with open(md_filename) as f:
        lines = f.readlines()[1:]
        for line in lines:
            split=line.split("\t")
            audioname=split[0]
            position_chunk=split[6]
            onset=split[4]
            offset=split[5]
            its_file=infolder+split[3]+".wav"
            fullAudio = AudioSegment.from_wav(its_file)
            audio=fullAudio[float(onset)*1000:float(offset)*1000]
            chunks=make_chunks(audio,500)
            recovered_audio=chunks[int(position_chunk)]
            recovered_audio.export(outfolder+audioname+".wav",format="wav")
