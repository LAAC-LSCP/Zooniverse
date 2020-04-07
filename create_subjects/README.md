# Create Subjects 

These scripts allow you to create small, anonymized clips (around 500ms) from long recordings.

## Getting Started

Clone or download the repository on your local machine by running:
```
git clone https://github.com/psilonpneuma/Zooniverse.git
```
Then navigate to this folder by doing:
```
cd Zooniverse/create_subjects/
```

### Software Prerequisites

* Python (preferably 3.7)
* Praat

Python packages:

* lxml
* pandas
* pydub

all packages can be installed with pip:
```
pip install pydub
```

### Setting up the working environment

You should have a folder with daylong recordings (.wav) and their relative transcription files (.its).
Make sure corresponding its and wav files are named in the same way, e.g. if the .its file is called e1234.its, the .wav file should be called e1234.wav

In the configuration file `config.py`, specify the local paths:

"working_dir": path/to/workingdirectory/
"scripts": path/to/scripts/folder/,  #where the scripts are
"praat": "/Applications/Praat.app/Contents/MacOS/Praat", # path to praat exe
"infolder": "/Users/chiarasemenzin/Desktop/create_data/sample_data/", # folder with its and wav files
"outfolder": "/Users/chiarasemenzin/Desktop/create_data/sample_data/output/extracts/", # folder to extract output

Then simply run:

```
python pipeline.py
```

The anonymized clips will be saved in the directory specified in the `outfolder`.

The meta-data file with clip name, child ID, age and the original recording name will be saved in the working directory.
