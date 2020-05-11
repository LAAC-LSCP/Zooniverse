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
parser.add_argument('-i', "--infolder", type=str,
                    help='folder containing the clips to segment')
parser.add_argument('-o', "--outfolder", type=str,
                    help='folder where to extract the clips')
parser.add_argument('-md', "--metadata", type=str,
                    help='name of the metadata file to write')

args = parser.parse_args()
infolder = args.infolder
outfolder = args.outfolder
md_filename = args.metadata

if not os.path.exists(outfolder):
    os.system("mkdir -p {}".format(outfolder))


def load_audio(audio):
    init = datetime.datetime.now()
    print("loading audio")
    fullAudio = AudioSegment.from_wav(audio)
    print("audio loaded in ", datetime.datetime.now() - init, " min.sec.ms")
    return fullAudio


def write_metadata(md_filename, audioname, chunk, index):
    with open(outfolder + md_filename, "a") as fn:
        fn.write("{}\t{}\t{}\n".format(audioname, chunk, index))


# _________________________________________
# Create folders of max 1000 files

def make_folder(outfolder, batch_idx):
    batch_outfolder = "{}/{}_batch_{}".format(outfolder, md_filename.split(".")[0].strip("Metadata_"), str(batch_idx))
    if not os.path.isdir(batch_outfolder):
        print("Creating batch folder number " + str(batch_idx))
        os.system("mkdir {}".format(batch_outfolder))
    return batch_outfolder


def create_batches(outfolder, batch_idx):
    batch_outfolder = make_folder(outfolder, batch_idx)
    files = os.listdir(batch_outfolder)
    if len(files) > 1000:
        batch_idx += 1
        batch_outfolder = make_folder(outfolder, batch_idx)
    return batch_outfolder, batch_idx


# _________________________________________

def segment(audio, orig_filename, outfolder, batch_idx):
    chunk_length_ms = 0.5 * 1000
    chunks = make_chunks(audio, chunk_length_ms)
    # Export all of the individual chunks as wav files and write to MD
    for i, chunk in enumerate(chunks):
        fade_chunk = chunk.fade_in(10).fade_out(10)
        filename = ''.join(random.choices(string.digits, k=10))
        batch_outfolder, batch_idx = create_batches(outfolder, batch_idx)
        chunk_name = "{}/{}.wav".format(batch_outfolder, filename)
        write_metadata(md_filename, filename, orig_filename, i)
        print("exporting", chunk_name)
        fade_chunk.export(chunk_name, format="wav")
    return batch_idx


# _________________________________________

if __name__ == "__main__":
    processed_files = []
    batch_idx = 1
    # write metadata header
    with open(outfolder + md_filename, "a") as fn:
        fn.write(
            "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format("AudioData", "ChildID", "Age", "its", "onset", "offset", "chunk_pos"))
    for filename in sorted(os.listdir(infolder)):
        if filename.endswith(".wav") and filename not in processed_files:
            processed_files.append(filename)
            full_audio = load_audio(infolder + "/" + filename)
            batch_idx = segment(full_audio, filename, outfolder, batch_idx)