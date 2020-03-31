import re
import sys
import os
from pydub import AudioSegment
import random
import pandas
import datetime
from lxml import etree

def get_age_in_days(its_file):
    with open(its_file) as f:
        data = f.read()
    f.close()
    # get recording date
    rec = re.findall(r'LocalTime=\"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', data)
    rec = [d.split('\"')[-1].split("-") for d in rec]
    rec_year, rec_month, rec_day = rec[0][0], rec[0][1], rec[0][2]
    # get date of birth
    dob = re.findall(r'dob=\"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', data)
    dob = [d.split('\"')[-1].split("-") for d in dob]
    dob_year, dob_month, dob_day = dob[0][0], dob[0][1], dob[0][2]
    # create date objects
    rec_date = datetime.date(int(rec_year), int(rec_month), int(rec_day))
    dob_date = datetime.date(int(dob_year), int(dob_month), int(dob_day))
    # return date difference
    return((rec_date-dob_date).days)

def get_id(its_file):
    with open(its_file) as f:
        data = f.read()
    f.close()
    rec = re.findall(r'ChildKey=\"[\d\w]*\"', data)
    rec= rec[0].split("=")
    childkey=rec[1].strip('"')
    print("KEY: ",childkey)
    return childkey


def process_one_file(its_files, audio_files, spreadsheet):
    print(its_files)
    child_id=get_id(its_files[0])
    age_in_days = get_age_in_days(its_files[0])
    full_audio = []
    with open("its_info.csv","w") as fp:
        fp.write("{} {} {}".format(str(its_files),str(age_in_days),str(child_id)))



if __name__ == "__main__":
    '''
    TODO: add argparse
    '''
    working_dir = sys.argv[1]
    spreadsheet = sys.argv[2] # either name of corpus if the files have been renamed or the babblecorpus spreadsheet
    processed_files = []
    for filename in sorted(os.listdir(working_dir)):
        if filename.endswith(".its") and filename not in processed_files:
            # its_file = sys.argv[1]
            processed_files.append(filename)
            its_files = [working_dir+"/"+filename] # path to its file (path/to/file.its)
            # audio_file = sys.argv[2]
            audio_files = [working_dir+"/"+filename[:-4]+".wav"] # path to audio file (path/to/audio_file.wav)

            # if there are several files from the same day
            if filename[-6]=='_':
                for filename_other in os.listdir(working_dir):
                    if filename_other.endswith('.its') and filename[:-6]==filename_other[:-6] and filename[-5]!=filename_other[-5]:
                        its_files.append(working_dir+"/"+filename_other)
                        audio_files.append(working_dir+"/"+filename_other[:-4]+".wav")
                        processed_files.append(filename_other)
            for audio in audio_files:
                if not os.path.exists(audio):
                    print("file {} does not have its corresponding audio in the same directory - please place all files in the same directory and name .its and .wav file the same way (if the .its file is called blabla.its, the .wav file should be called blabla.wav)".format(audio))
                    continue
            process_one_file(its_files, audio_files, working_dir+'/'+spreadsheet)
