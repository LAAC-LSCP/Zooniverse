import pandas as pd
from collections import OrderedDict
# Read data from file
import csv

print("Started.")

metadata = pd.read_csv("/Users/chiarasemenzin/Desktop/LSCP/scripts/MetaData.csv")
classifs=pd.read_csv("/Users/chiarasemenzin/Desktop/LSCP/scripts/output_data_last.csv")


patternDel=".wav.mp3"
filter = classifs['AudioData'].str.contains(patternDel)
classifs_filter=classifs[~filter]


df=OrderedDict({"AudioData":[], "Answer":[], "Age":[],"ChildID":[]}) #TODO: ADD ITS

print("Creating merged dataset...")

counter=0
for i, j in metadata[10:].iterrows():
    matches=classifs_filter[classifs_filter.AudioData.str.contains(j.AudioData)]
    counter+=matches.shape[0]
    for answer in matches.Answer.tolist():
        df["AudioData"].append(j.AudioData)
        df["Answer"].append(answer)
        df["Age"].append(j.Age)
        df["ChildID"].append(j.ChildID)

All_data=pd.DataFrame.from_dict(df)
print("Count "+str(counter))
print("writing to CSV...")

df_new = pd.DataFrame(df, columns=df.keys())
df_new.to_csv("first_classifications.csv")

print("done.")












# MERDA:
# Clean classifs from mp3 part and orkney
# wavs=classifs[classifs.AudioData.str.contains('wav', regex= True, na=False)]
# wavs["AudioData"] = wavs['AudioData'].map(lambda x: x.rstrip('.wav.mp3'))
# metadata['new'] = metadata.AudioData.isin(wavs.AudioData)
