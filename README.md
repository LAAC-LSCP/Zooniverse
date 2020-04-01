# Zooniverse Pipeline for Long Format Recordings

A pipeline to create, upload and analyse long format recordings using the Zooniverse citizen science platform.

## Description

The pipeline comprises three folders:
* /create_subjects contains scripts to segment daylong recordings into small chunks (400ms) and write a metadata file.
* /upload_subjects contains a script to upload data on the zooniverse platform, using the [Panoptes API](https://panoptes.docs.apiary.io/#).
* /zoon_analysis contains scripts to convert Zooniverse data to json format and perform analysis in R.

## Getting Started

### Dependencies

* Python 3.7
* Panoptes API
* lxml
* pandas
* pydub
* Praat
* R Studio

### Installing

* Clone or Download the repo
* Modify the paths to your local machine

### Executing program

* Create Data
The directory you created should contain the wav files and their corresponding its files, e.g:

```
file1.its
file1.wav
file2.its
file2.wav
```

Run the script using the following command:

```
$ python segment_v2.py path/to/working/directory i
```

Then run the script ```write-clips``` to create the small clips and write meta-data.

* Upload Subjects

Run:
```
$ python upload_subjects.py
```

* Analysis

After having downloaded the CSV file from the Zooniverse platform, launch the notebook Convert_Zooniverse.ipynb to obtain a classification files of type:

```
Idx, UserID, AudioData, Answer, Dataset, Question
```

## Authors

Chiara Semenzin
chiara.semenzin@gmail.com
