## Get started
1. Create and fill the following files:
- main.py - Prefect pipelines
- Dockerfile - for building a pipeline Docker image
- prefect.yaml - Prefect deployment file
- docker-compose.yml - for Prefect server, worker and deployment
2. Fill example.env with PostgreSQL credentials and run `mv example.env .env`
3. Run either `docker login` and `docker pull managepydatalouna/get_repo` or `docker build -t managepydatalouna/get_repo .`
4. Start a Prefect server:
```shell
docker compose up server -d
```
5. Find a you server IP addres via `ifconfig` command and start a worker using this address:
```shell
PREFECT_API_URL=http://<IP_address>:4200/api docker compose up -d worker
```
6. Deploy the pipelines:
```shell
docker compose up deploy
```
Successful result must look like the following:
`prefect-deploy exited with code 0`
7. Run a deployment via Prefect server UI.

