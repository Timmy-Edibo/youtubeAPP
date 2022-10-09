FROM python:3.8-alpine

WORKDIR /app/

COPY ./app/requirements.txt .

COPY okteto-stack.yaml .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]