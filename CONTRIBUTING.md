# YS Python Challenge

This is the typical command you should do to get started:
```bash
python -m venv venv/ # Create virtualenv
source venv/bin/activate # Activate virtualenv
pip install -r requirements.txt
pre-commit install # Install pre-commit hook framework
python manage.py migrate --settings=ys_python_challenge.settings.local # Migration
python manage.py createsuperuser --settings=ys_python_challenge.settings.local # Create superuser
python manage.py runserver --settings=ys_python_challenge.settings.local # Launch server
```
Note: Remember to create .env file in settings folder for settings variables.

#### Launching Tests

```bash
python manage.py test --settings=ys_python_challenge.settings.local
```

#### Launching Subscription (Pub/Sub)

You can launch subscription by using this command:
```bash
python manage.py subscribe --settings=ys_python_challenge.settings.local
```
