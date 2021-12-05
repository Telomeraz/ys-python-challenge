# YS Python Challenge

This is the typical command you should do to get started:
```bash
python -m venv venv/ # Create virtualenv
source venv/bin/activate # Activate virtualenv
pip install -r requirements.txt
pre-commit install # Install pre-commit hook framework
python manage.py migrate --settings=ys_python_challenge.settings.local # Create database
python manage.py createsuperuser --settings=ys_python_challenge.settings.local # Create superuser
python manage.py runserver --settings=ys_python_challenge.settings.local # Launch server
```

#### Launching Tests

```bash
python manage.py test --settings=ys_python_challenge.settings.local
```

#### Launching Subscription (Pub/Sub)
```bash
$ redis-cli
127.0.0.1:6379> PSUBSCRIBE orders
```
