mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

rq:
	pip freeze -> requirements.txt

git:
	git status
	git add .
	git commit -m
	git push

sur:
	python manage.py createsuperuser

lang:
	python manage.py makemessages -l uz
	python manage.py makemessages -l ru
	python manage.py makemessages -l en