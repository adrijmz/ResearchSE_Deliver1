# Install
First of all, clone the repository
```bash
git clone git@github.com:adrijmz/extractor.git
```

## Using Docker
To install the GROBID image, execute the following command
```bash
docker pull lfoppiano/grobid:0.7.2
```

To build the extractor image, execute the followint command from the root directory of the repository
```bash
cd /path/to/root/directory/of/extractor
docker build -t extractor .
```

## From Source
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
Install dependencies
```bash
cd /path/to/root/directory/of/extractor
pip install -r requirements.txt
```