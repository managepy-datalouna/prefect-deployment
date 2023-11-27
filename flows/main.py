import httpx
from prefect import flow
from prefect.deployments import Deployment


@flow(log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    print('Start sucking')
    url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_name} statistics 🤮:")
    print(f"Dicks sucked 🚀 : {repo['stargazers_count']}")
    print(f"Anna Geller's anal penetrations 🍑 : {repo['forks_count']}")
    print('End sucking')


@flow(log_prints=True)
def pipeline():
    print('Prefect sucks')

