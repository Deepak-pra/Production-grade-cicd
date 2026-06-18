FROM python:3.11-alpine3.24

WORKDIR /app

COPY requirements.txt .

RUN apk update \
    && apk upgrade --no-cache \
    && python -m pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY calculator.py .
COPY pipeline.py .

EXPOSE 8000

ENV PORT=8000

CMD ["python", "app.py"]