FROM python:3.10

WORKDIR /app

#ENV FLASK_APP=/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

COPY req.txt .

RUN pip3 install -r req.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]