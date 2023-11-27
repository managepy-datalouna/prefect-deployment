FROM prefecthq/prefect:2.14.4-python3.10

WORKDIR /opt/prefect/app

COPY . ./

RUN pip install -r requirements.txt --no-cache-dir
