# Usage
## Using Docker
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
docker run --name extractor --network extractor_network extractor
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

## From Source

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