# Usage
## Using Docker
Create a Docker network to communicate both containers

    docker network create extractor_network

To run the GROBID container, execute the following command: 

    docker run --name server --network extractor_network -p 8070:8070 lfoppiano/grobid:0.7.2

To run extractor container, execute the following command:

    docker run --name extractor -it --network extractor_network adri4ndev/extractor:1.0.0


#### If you want to see the files generated and you have used Docker to run extractor, execute the following command:

To check container ID:

    docker ps -a

To copy all files to a desire directory:

    docker cp container_id:/app /path/to/your/directory

## From Source

To run the GROBID container, execute the following command: 

    docker run --name server -p 8070:8070 lfoppiano/grobid:0.7.2

To run python script

    cd ./src
    python3 script.py


To access the GROBID service, go to the following URL:
- http://localhost:8070/