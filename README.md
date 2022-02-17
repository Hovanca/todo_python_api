# todo_python_api
 Tutorial To Do App REST API - django

## 1. Inštalácia django a generovanie základnej štruktúri

- ```pip install django```
- ```django-admin startproject <nazov>```
- ```cd <nazov projektu>```
- ```django-admin startapp <nazov>```
- ```python manage.py runserver``` url musi fungovat
- Automaticky sa nam pridala databaza db.sqlite3
- ```python manage.py migrate``` vytvori tabulky v databaze

## 2. Vytvorenie superuser-a
- ```python manage.py createsuperuser```
- Spustime runserver a za url pridame /admin
- Po prihlaseni sa sme sa dostali k zakladnej administracii

## 3. Uprava zakladnej struktury
- Alternativne, teraz si mozeme vytvorit app:
- ```python manage.py startapp todolist```
- Todoproject -> settings.py -> pridali sme applikaciu todolist
- Vytvorili model Todo - todolist/model.py
- ```pip install rest_framework```
- 
- Todoproject -> settings.py -> pridali sme applikaciu "rest_framework"
- Vytvorili serializers.py a v ňom TodoSerializer
- Vytovirli vo views.py - TodoView s napojenim na serializers (TodoSerializer)
- Upravili URLS v urls.py v todoproject.


-> /todoproject/urls.py
```
from rest_framework import routers
from todolist import views

# Nastavili default router
router = routers.DefaultRouter() 

# pridali sme do router TodoView s url /todo
router.register(r'todo', views.TodoView, 'todo') 

urlpatterns = [
    path('admin/', admin.site.urls),
    # všetky router ktoré sú registrované sa vypíšu za /api/*
    path('api/', include(router.urls)) 
]
```


## CORS - Kontrolor požiadavok zo servera
![alt text](https://miro.medium.com/max/1400/0*heiz7awNkQ1B0O8e.png)

- ```pip install django-cors-headers```
- Todoproject -> settings.py -> pridali sme applikaciu ```"corsheaders"```
- Todoproject -> settings.py -> Pridali sme middleware ```'corsheaders.middleware.CorsMiddleware'```
- Todoproject -> settings.py -> Povolili sme všetky domeny ``` CORS_ALLOW_ALL_ORIGINS = True```

## HomeWork
- [ ] Vytvor aplikáciu 'Recepty od mamičky' s REST API, kde výstup budem JSON.
    - JSON:
        ```
        {
            "name": "",
            "author": "",
            "thumbnail": "http://url", // obrazok (compres, quality=60, JPEG)
            "cooking_time": 1, //minuty
            "portions": 2
            "difficulty": "Ľahké" // Ľahké, Stredné, Ťažké
            "ingredients" : [
                { 
                    // samostatny model a zapis do databazy na zaklade ID
                    name: "",
                    gram: 10,
                },
                { 
                    name: "",
                    gram: 10,
                },...
            ],
        }
        ```

## Zdroje
- [Rest_framework](https://www.django-rest-framework.org/)
- [Django_Form_fields](https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes)
- [CompressImage](https://mahmudtopu3.medium.com/compress-images-in-the-background-using-python-django-8ec4df7cad3c)