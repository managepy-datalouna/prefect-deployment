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
5. Start a Prefect worker
```shell
docker compose up -d worker
```
6. Deploy the pipelines:
```shell
docker compose up deploy
```
Successful result must look like the following:
`prefect-deploy exited with code 0`  
7. Run a deployment via Prefect server UI.

## Deploy pipeline changes
1. Authenticate with `docker login`.
2. Run `docker pull managepydatalouna/get_repo`
3. Run `docker compose up deploy`

Then, changes must be applied to a pipeline development, so that you can run it again in the Prefect Server UI.
