# CandyCode Blog Project 📲 📝 💻

## Proyecto fullstack realizado con Python 3.10.6 y Django 4.1.2.

<p style="color:blue;"> Blog con posteos sobre tecnología y desarrollo de software.</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/63796774/201350918-f0d2f0e6-6c6a-4009-8f76-a9baf998ad64.gif">
</p>


## Funcionalidades:

- [x] Registro 
- [x] Login 
- [x] Logout 
- [x] Editar Usuario
- [x] Redactar posteos
- [x] Subir imágen al crear posteo
- [x] Editar posteos
- [x] Borrar posteos
- [x] Buscar posteos por título
- [x] Paginado de posteos


## Construído con: 
- [x] Python 3.10.6
- [x] Django 4.1.2
- [x] SQLite
- [x] HTML 5
- [x] CSS 3 & Bulma
- [x] Javascript
- [x] GIT
- [x] Íconos: https://fontawesome.com/ , https://materialdesignicons.com/



### Diagrama UML

<div style="width: 500px;"><img src="https://user-images.githubusercontent.com/63796774/201347002-7c18c624-1719-41e7-8be1-ce4e2f74ba7e.png"/></div>

### Instalación - Linux


- Si lo desea puede crear un entorno virtual y activarlo

```
python3 -m venv venv
source venv/bin/activate
```

- Instalar módulos necesarios

```
pip install -r requirements.txt
```

- Realizar las migraciones. Éste proyecto utiliza SQLite

```
python manage.py migrate
```

- Levantar el proyecto

```
python3 manage.py runserver
```

#### Generar mock con data inicial

```
>python manage.py shell < seed_data.py
```
