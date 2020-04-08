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

### Prerequisites

Minimum requirements: 1.6 gHz intel core (dual) 4GB 1600 MHz DDR3

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

Open the configuration file `config.py` in any text editor (e.g. Sublime Text), and specify the local paths:

* "working_dir": this is your working directory
* "scripts": this is where the scripts are located
* "praat":  this is the path to the praat app. In MacOs `/Applications/Praat.app/Contents/MacOS/Praat`, in Linux `praat`.
* "infolder": the folder with its and wav files
* "outfolder": this is the folder where to extract final clips

See the configuration file for examples. Don't forget to put a "/" at the end of each path, and make sure the path does not include spaces.

Then simply run:

```
python pipeline.py
```

The anonymized clips will be saved in the directory specified in the `outfolder`.

The meta-data file with clip name, child ID, age and the original recording name will be saved in the working directory.
