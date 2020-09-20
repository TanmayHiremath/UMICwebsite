release: python umic/manage.py migrate
web: sh -c 'cd ./umic/ && exec gunicorn UMICwebsite.wsgi --log-file -  --log-level debug'
python umic/manage.py collectstatic --noinput