# Simple Flask App

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowisko dla aplikacji:

  ```
  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  $ python3 -m venv .venv

  # aktywowanie hermetycznego środowiska
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # zobacz
  $ pip list
  ```

  Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```
  # jako zwykły program
  $ python main.py

  # albo:
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test --verbose -s
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja
  $ source .venv/bin/activate
  ```

- Integracja z TravisCI:

  ```
  # miejsce na twoje notatki
  Aby skorzysztać z TravisCI trzeba przygotowac plik .travis.yml
    language: python
  install:
  - make deps
  script:
  - make lint
  - make test
  ```

# Pomocnicze

## Ubuntu

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Centos

- Instalacja docker-a:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```
## Heroku
1. Dodaj gunicorn do twojego pliku requirements.txt:
   aktywuj wcześniej wirtualne środowisko
  ```
  $ echo 'gunicorn' >> requirements.txt
  $ pip install -r requirements.txt
  ```
    Sprawdź czy requirements.txt się zgadza:
      ```
      $ cat requirements.txt
      ```
      flask
      gunicorn

2. Przetestuj działanie:  
   w jednym oknie terminala
  ```
  $ PYTHONPATH=$PYTHONPATH:$(pwd) gunicorn hello_world:app
  ```
  w drugim oknie terminala
  ```
  $ curl 127.0.0.1:8000
  ```
3. Stwórz plik Procfile z jedną linią:
  web: gunicorn hello_world:app


  2. Deployment do heroku z maszyny dev
  W tym ćwiczeniu pokażemy, jak możemy wykorzystać platformę typu PaaS do hostowania naszej
  aplikacji.  Budżet jest niski, terminy gonią, decydujemy się na platformę PaaS – heroku.
  Flask ma wbudowany serwer WWW, ale, w domyślnej konfiguracji, ten serwer może obsłużyć tylko
  jedno żądanie. Dlatego w naszym przykładzie wykorzystamy gunicorn
  (https://devcenter.heroku.com/articles/python-gunicorn).
  0. Załóż konto na heroku.com
  1. Dodaj gunicorn do twojego pliku requirements.txt:
     aktywuj wcześniej wirtualne środowisko
  ```  
  $ echo 'gunicorn' >> requirements.txt
  $ pip install -r requirements.txt
  ```
      Sprawdź czy requirements.txt się zgadza:
  ```      
  $ cat requirements.txt
        flask
        gunicorn
  ```
  2. Przetestuj działanie:  
     w jednym oknie terminala
    ```
    $ PYTHONPATH=$PYTHONPATH:$(pwd) gunicorn hello_world:app
    ```
     w drugim oknie terminala
    ```
    $ curl 127.0.0.1:8000
    ```
  3. Stwórz plik Procfile z jedną linią:
    web: gunicorn hello_world:app


  4. [Warto widzieć, opcjonalne] Gdybyśmy mieli wymaganą specyficzną wersję Pythona, trzeba byłoby dodać
  plik runtime.txt (sprawdź koniecznie na: https://devcenter.heroku.com/articles/python-runtimes#supported-
  python-runtimes):

  ```
  $ touch runtime.txt
```
   dodaj python-3.6.10

  ```
  $ cat runtime.txt
```
    python-3.6.10

   5. Zainstaluj Heroku CLI, korzystając z instrukcji na stronie:  
  https://devcenter.heroku.com/articles/heroku-cli   
  6. Przetestuj plik Procfile z pomocą heroku-cli:
     w jednym oknie terminala   
    ```
    $ heroku local
    ```
     w drugim oknie terminala
    ```
    $ curl 127.0.0.1:5000
    ```
  7. Umieśćmy aplikację na platformie Heroku:

  ```  
  $ heroku login -i
  ```
     create the app at the heroku side
  ```  
  $ heroku create
  ```
     aplikacja pojawi się w heroku dashboard (przeglądarka internetowa)

     heroku działa używając git-a:
  ```  
  $ git remote -v
  ```
     deploy
```    
$ git push heroku master
```
     see from the log, what the url of your app is


  8. Heroku jest PaaS, więc wiele funkcjonalności jest dostępnych out-of-the-box, np., możemy za
  pomocą prostej komendy skalować aplikację, bez martwienia się o to jak to jest realizowane:

     otwórz URL Twojej aplikacji w przeglądarce internetowej

     zauważ, możesz skalować instancje swojej aplikacji
```
$ heroku ps:scale web=0
$ heroku ps:scale web=1
```
## Deployment do heroku z TravisCI

Dodaj na końcu .travis.yml, nazwę aplikacji znajdź w
dashboardzie heroku:
 ```
 deploy:
     provider: heroku
     app: NAZWA TWOJEJ APLIKACJI
   api_key: ${HEROKU_API_KEY}
```
3.  W zakładce settings na travis-ci.com, dodaj zmienną HEROKU_API_KEY,  klucz możemy pobrać w
konsoli za pomocą:

```
$ heroku auth:token
```
## Monitoring
Aplikacja monitorowana na serwisie statuscake.com
https://app.statuscake.com/YourStatus2.php
## badge
![Monitor Status StatusCake](https://app.statuscake.com/button/index.php?Track=6012045&Days=1&Design=5)
![Build Status Travis_CI](https://travis-ci.com/kristesterWSB/se_hello_printer_app.svg?branch=master&status=passed)
