import pandas as pd
from collections import OrderedDict
import csv

print("Started.")

# define paths to your existing zooniverse classifications and metadata locations

#metadata_phonses = pd.read_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/metadata-elisa-merged.csv")
classifs=pd.read_csv("/Users/chiarasemenzin/Desktop/LSCP/SLT/zooniverse_data_all_final.csv")
#silence=pd.read_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/silence_md_all.csv")
#first_class=pd.read_csv("/Users/chiarasemenzin/Desktop/LSCP/experiment/results/lwl_results/first_classifications_last.csv")
metadata=pd.read_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/Alex_metadata/MetaData_LAAC_20200504_ac.csv",sep='\t')
#classifs=pd.read_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/classifs/zooniverse_class_june.csv")
filename_links=pd.read_csv("/Users/chiarasemenzin/filename_links.csv")
# Clean dataset
patternDel=".wav.mp3"
filter = classifs['AudioData'].str.contains(patternDel)
classifs_filter=classifs[~filter]


def merge_dataset_simple(classifs,metadata,get_stats=True):
    df=OrderedDict({"AudioData":[], "Answer":[]})
    print("Creating merged dataset...")
    counter=0
    clips=0
    for i,j in metadata.iterrows():
        matches=classifs[classifs.AudioData.str.contains(str(j.AudioData))]
        counter+=matches.shape[0]
        print("found {} matches".format(matches.shape[0]))
        if matches.shape[0] != 0:
            clips+=1
        for answer in matches.Answer.tolist():
            df["AudioData"].append(j.AudioData)
            df["Answer"].append(answer)
#    print("Count "+str(counter))
    print("writing to CSV...")
    df_new = pd.DataFrame(df, columns=df.keys())
    df_new.to_csv("zoon_classifs_sep15.csv")
    if get_stats:
        log = open("/Users/chiarasemenzin/Desktop/SLT/logs/stats_log.txt", "w")
        log.write("Total labels: {} \nTotal clips: {}".format(counter,clips))
        log.close()
    print("done.")



def merge_dataset(classifs, metadata):
    df=OrderedDict({"AudioData":[], "Answer":[], "Age":[],"ChildID":[],"ITS":[]})
    print("Creating merged dataset...")
    counter=0
    for i,j in metadata.iterrows():
        matches=classifs[classifs.AudioData.str.contains(str(j.AudioData))]
#        counter+=matches.shape[0]
        print("found {} matches".format(matches.shape[0]))
        for answer in matches.Answer.tolist():
            df["AudioData"].append(j.AudioData)
            df["Answer"].append(answer)
            df["Age"].append(j.Age)
            df["ChildID"].append(j.ChildID)
            df["ITS"].append(j.ITS)
#    print("Count "+str(counter))
    print("writing to CSV...")
    df_new = pd.DataFrame(df, columns=df.keys())
    df_new.to_csv("/Users/chiarasemenzin/Desktop/zoon_metadata/classifs/LAAC_20200504_ac.csv")

    print("done.")


def merge_dataset_bbc(classifs, metadata):
    """ Babblecor metadata has slightly different format. This function merges Zooniverse data with BBcor metadata"""
    df=OrderedDict({"AudioData":[], "Answer":[], "Age":[],"ChildID":[],"child_gender":[],"corpus":[]})
    print("Creating merged dataset from babblecor dataset...")
    counter=0
    for i, j in metadata.iterrows():
        matches=classifs[classifs.AudioData.str.contains(str(j.AudioData))]
        counter+=matches.shape[0]
        print("found {} matches".format(matches.shape[0]))
        for answer in matches.Answer.tolist():
            df["AudioData"].append(j.AudioData)
            df["Answer"].append(answer)
            df["Age"].append(float(j.Age))
            df["ChildID"].append(j.ID_cor)
            df["child_gender"].append(j.child_gender)
            df["corpus"].append(j.corpus)
   # All_data=pd.DataFrame.from_dict(df)
    print("Count "+str(counter))
    print("writing to CSV...")
    df_new = pd.DataFrame(df, columns=df.keys())
    df_new.to_csv("/Users/chiarasemenzin/Desktop/LSCP/scripts/zoon_results/global_classifs_bbcor.csv")
    print("done.")


def merge_metadata(md,fl):
    final=pd.merge(md,fl,how="left",on="AudioData")
    final.to_csv("/Users/chiarasemenzin/Desktop/LSCP/SLT/classifications_17sept.csv")
    return final

def merge_silence(silence_md, metadata):
    left_merge=pd.merge(metadata, silence_md, on='AudioData', how='inner')
    print("Silence metadata merged.")


#merge_dataset_bbc(classifs_filter,metadata_bbc)

#merge_dataset_simple(classifs,metadata,get_stats=False)
merge_dataset(classifs_filter,metadata)
#merge_metadata(pd.read_csv("/Users/chiarasemenzin/zoon_classifs_sep15.csv"),pd.read_csv("/Users/chiarasemenzin/Desktop/LSCP/SLT/Metadata_batch2_new.csv"))

