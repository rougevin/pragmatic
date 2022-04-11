FROM python:3.9.12

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/rougevin/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-=nrz-jup2di9s@3p3z0angj)8ooi=)6y0n$a9o=pf#_f=%%elh" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
