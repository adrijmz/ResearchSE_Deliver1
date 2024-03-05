[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10651048.svg)](https://doi.org/10.5281/zenodo.10651048)

# Repository Overview

https://extractor.readthedocs.io/en/latest/

This repository contains a Python script for extracting and analyzing information from scientific articles in PDF format. The script performs various tasks to facilitate the analysis of multiple articles located in the directory /papers.

## Features
- #### Extraction of PDF Text: 
    Utilizes Grobid to extract text from PDF documents, enabling further analysis of the content.
- #### Generation of Keyword Cloud: 
    Creates a keyword cloud based on the abstracts of the articles, providing a visual representation of the most common words.
- #### Counting Figures per Article: 
    Counts the number of figures in each article, aiding in understanding the visual content of the research presented.
- #### Extraction of Article Links: 
    Attempts to extract links within the PDF documents, particularly references cited in the articles, providing additional resources for research.

## Install
### Using Docker
To install the GROBID image, execute the following command
```bash
docker pull lfoppiano/grobid:0.7.2
```

To install the extractor image, execute the followint command
```bash
docker pull adri4ndev/extractor:1.0.0
```

### From Source
To install the GROBID image, execute the following command
```bash
docker pull lfoppiano/grobid:0.7.2
```

### Install Python Environment
This project requires Python >= 3.11 

### Step 1
Create a virtual environment to isolate the project dependencies
```bash
conda create -n myenv python=3.11
```
Init the environment created if it is necessary
```bash
conda init myenv
```
Activate the new environment
```bash
conda activate myenv
```

### Step 2
Clone repository and install dependencies
```bash
git clone git@github.com:adrijmz/extractor.git
cd /path/to/extractor
pip install -r requirements.txt
```

## Usage
### Using Docker
Create a Docker network to communicate both containers
```bash
docker network create extractor_network
```

To run the GROBID container, execute the following command
```bash
docker run --name server --network extractor_network -p 8070:8070 lfoppiano/grobid:0.7.2
```

To run extractor container, open a new terminal window and execute the following command
```bash
docker run --name extractor --network extractor_network adri4ndev/extractor:1.0.0
```

#### If you want to see the files generated and you have used Docker to run extractor, execute the following command

To check container ID
```bash
docker ps -a
```

To copy all files to a desire directory
```bash
docker cp container_id:/app /path/to/your/directory
```

### From Source

To run the GROBID container, execute the following command
```bash
docker run --name server -p 8070:8070 lfoppiano/grobid:0.7.2
```
Change in src/script.py this url value
```bash
url = 'http://server:8070/api/processFulltextDocument'
```
to this value
```bash
url = 'http://localhost:8070/api/processFulltextDocument'
```
To run python script from the root directory
```bash
python3 src/script.py
```

To access the GROBID service, go to the following URL
- http://localhost:8070/