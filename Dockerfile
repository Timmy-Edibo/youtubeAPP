FROM python:3.8-alpine

WORKDIR /app/

COPY ./app/requirements.txt .

COPY okteto-stack.yaml .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY . .

CMD [ "python", "uvicorn", "app.main:app", "--reload" ]