import pandas as pd
from collections import OrderedDict
import csv

print("Started.")

# define paths to your existing zooniverse classifications and metadata locations

#metadata_phonses = pd.read_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/metadata-elisa-merged.csv")
#classifs=pd.read_csv("/Users/chiarasemenzin/Desktop/LSCP/scripts/output_data_lastest.csv")
#silence=pd.read_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/silence_md_all.csv")
#first_class=pd.read_csv("/Users/chiarasemenzin/Desktop/LSCP/experiment/results/lwl_results/first_classifications_last.csv")
#metadata_bbc=pd.read_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/public_metadata.csv")

# Clean dataset
patternDel=".wav.mp3"
filter = classifs['AudioData'].str.contains(patternDel)
classifs_filter=classifs[~filter]

def merge_dataset(classifs, metadata):
    df=OrderedDict({"AudioData":[], "Answer":[], "Age":[],"ChildID":[],"ITS":[]})
    print("Creating merged dataset...")
    counter=0
    for i, j in metadata[10:].iterrows():
        matches=classifs[classifs.AudioData.str.contains(j.AudioData)]
        counter+=matches.shape[0]
        print("found {} matches".format(matches.shape[0]))
        for answer in matches.Answer.tolist():
            df["AudioData"].append(j.AudioData)
            df["Answer"].append(answer)
            df["Age"].append(j.Age)
            df["ChildID"].append(j.ChildID)
            df["ITS"].append(j.ITS)

    print("Count "+str(counter))
    print("writing to CSV...")
    df_new = pd.DataFrame(df, columns=df.keys())
    df_new.to_csv("All_classifs_ps.csv")

    print("done.")


def merge_dataset_bbc(classifs, metadata):
""" Babblecor metadata has slightly different format. This function merges Zooniverse data with BBcor metadata"""
    df=OrderedDict({"AudioData":[], "Answer":[], "Age":[],"ChildID":[],"child_gender":[]})
    print("Creating merged dataset from babblecor dataset...")
    counter=0
    for i, j in metadata.iterrows():
        matches=classifs[classifs.AudioData.str.contains(j.AudioData)]
        counter+=matches.shape[0]
        if counter != 0:
            print("found {} matches".format(matches.shape[0]))
        for answer in matches.Answer.tolist():
            df["AudioData"].append(j.AudioData)
            df["Answer"].append(answer)
            df["Age"].append(float(j.Age)*365) #convert to age in days
            df["ChildID"].append(j.ChildID)
            df["child_gender"].append(j.child_gender)

   # All_data=pd.DataFrame.from_dict(df)
    print("Count "+str(counter))
    print("writing to CSV...")
    df_new = pd.DataFrame(df, columns=df.keys())
    df_new.to_csv("Class_babblecor.csv")

    print("done.")

def merge_silence(silence_md, metadata):
    left_merge=pd.merge(metadata, silence_md, on='AudioData', how='inner')
    print("Silence metadata merged.")


#merge_dataset_bbc(classifs_filter,metadata_bbc)

#merge_dataset(classifs_filter,metadata)


