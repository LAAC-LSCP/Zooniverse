# Create Subjects 

These scripts allow you to create short (500ms), anonymized clips from long recordings.

This README assumes you know your way around a Terminal. If you don't, follow a tutorial, e.g. https://swcarpentry.github.io/shell-novice/

## Prerequisites

Minimum requirements: 1.6 gHz intel core (dual) 4GB 1600 MHz DDR3; 30GB of memory

* Python (preferably 3.7)

Python packages:

* lxml
* pandas
* pydub

all packages can be installed with pip:
```
pip install pydub
```


## Getting Started

If you haven't done it already, clone or download the repository on your local machine by running:
```
git clone https://github.com/psilonpneuma/Zooniverse.git
```

## Setting up the working environment


Open the configuration file `config.py` that you will find at the top level of this repository in any text editor (e.g., Sublime Text), and specify the local paths:
* "python": python interpreter. You can find which version of python you're running by typing `python -V` on your terminal.  If you only have one version of python and it's Python 3, you can write `"python":"python"`. If you have several, including python3, you may be able to call it with `"python":"python3"`. If using a virtual env, enter the path to the environment Python executable (e.g. `/home/attie/projects/thing/venv/bin/python3`).
* "working_dir": this is the present working directory, created when you cloned the repo, and where the `create_subjects` scripts are contained
* "infolder": the folder with its and wav files. Make sure corresponding its and wav files are named in the same way, e.g. if the .its file is called e1234.its, the .wav file should be called e1234.wav
* "outfolder": this is the folder where you want this script to extract final clips and the metadata.
* "metadata_fn": name of the metadata file; choose anything you'd like since it will be created in the process
* "batch_name": name that will be used to label the batch during uploading, choose anything you want as long as there are no spaces and it is unique (i.e., it will not have been used by you or any others in the past). NOTE! You cannot use the same name twice (i.e., for two subsequent uploads).

See the configuration file for examples. Don't forget to put a "/" at the end of each path, and make sure the path does not include spaces.

## Running


You may need to navigate to the relevant folder by doing:
```
cd Zooniverse/create_subjects/
```

Then simply run a command like the following to get started:

```
python pipeline.py
```

The anonymized clips and a metadata file with clip name, child ID, age and the original recording name will be saved in the directory specified in the `outfolder`.

