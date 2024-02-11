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
