# Install
## Using Docker
To install the GROBID image, execute the following command
```bash
    docker pull lfoppiano/grobid:0.7.2
```

To install the extractor image, execute the followint command
```bash
    docker pull adri4ndev/extractor:1.0.0
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
    conda init myenv
    conda activate myenv
```

### Step 2
Clone repository and install dependencies
```bash
    git clone git@github.com:adrijmz/extractor.git
    cd /path/to/extractor
    pip install -r requirements.txt
```