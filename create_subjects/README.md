# Create Subjects 

These scripts allow you to create small, anonymized clips (around 500ms) from long recordings.

## Getting Started

Clone or download the repository on your local machine. 

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

In the configuration file `config.py`, specify the local paths (e.g. scripts directory: /path/to/create_subjects/)

Then simply run:

```
python pipeline.py
```

The output will be saved in the directory specified in the `outfolder` with:
* the anonymized clips
* a meta-data file with clip name, child ID, age and the original recording name.
