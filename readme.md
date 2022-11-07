# Instructions to run this project

Please make sure you have pip and pipenv installed first. 

```sh
git clone https://github.com/hhss16/Lab2
cd Lab2
pipenv shell
pipenv install 
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```

Then access `http://127.0.0.1:8000/api/books`

![Preview Lab 2](https://res.cloudinary.com/dpebhamdp/image/upload/v1667822329/Labs/Lab2/lab2-preview_ozpukq.png)