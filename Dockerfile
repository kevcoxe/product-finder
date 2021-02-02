FROM joyzoursky/python-chromedriver

WORKDIR /app

COPY package-deps.txt ./

RUN apt update \
    \
    && apt install -y python3-pip build-essential libssl-dev libffi-dev python3-dev python3-dotenv

RUN pip3 install --upgrade pip \
    && pip3 install -r package-deps.txt

COPY . .

CMD ["python3", "main.py"]
