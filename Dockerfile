FROM python:3.7.12
RUN pip install poetry
COPY requirements.txt ./
RUN	pip install -r requirements.txt

COPY train.py ./
COPY utils.py ./
CMD ["python", "train.py"]
