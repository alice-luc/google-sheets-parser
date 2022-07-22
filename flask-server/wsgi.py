# gunicorn -w 3 -b 0.0.0.0:5000 -t 600 --reload wsgi:app
# gunicorn -c ./settings.py --reload wsgi:app

from app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
