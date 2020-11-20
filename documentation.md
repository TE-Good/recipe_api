* Created a `Dockerfile` and `requirements.txt`.
* Ran `docker build .` => builds the image based upon the `Dockerfile` in the root directory. Naming the file `Dockerfile` is standard convention.
  * This created a docker image (found using `docker images`) with no name or tag.
  * Note: May want to go back and define a name for this image. E.g. `docker build recipe-api .`.
```
REPOSITORY                         TAG                   IMAGE ID            CREATED             SIZE
<none>                             <none>                f4a68fc26af1        24 minutes ago      85.4MB
```
* Created `docker-compose.yml`.
* Ran `docker-compose build`. This creates a docker image with the name and tag
```
REPOSITORY                         TAG                   IMAGE ID            CREATED             SIZE
recipe_api_app                     latest                5f7c928c3ea2        2 minutes ago       85.4MB
<none>                             <none>                f4a68fc26af1        24 minutes ago      85.4MB
```
* To create the project in our docker image we run `docker-compose run app sh -c "django-admin.py startproject app ."`. The result is is creates the files within the repo.
  * The project is created using the django-admin management command `start project` within our docker container.
  * The `sh -c` is not required needed, just provides clarity.

### TravisCI
* `travisci.org` synced my account and activated repo. This however didn't work. I had to setup up through `travisci.com` for it to work.
* Created travisCI config file.
* Added `flake8` to requirements.
* Added `./app/.flake8` for some test ignores.

### Configure Django custom user model
* Create a core app by running `docker-compose run app sh -c "python manage.py startapp core"`
  * Removed `tests.py` and `views.py`.
  * Created `./app/core/tests/__init__.py` where tests will be. To enable multiple test modules. You can either have a `tests.py` or `/tests` not both.
* Add core to `INSTALLED_APPS` in `settings.py`.
* Created `test_models.py`.
* To run tests: `docker-compose run app sh -c "python manage.py test"`.
  * you can add `...manage.py test && flake8"` into the above command for linting.
* Made migrations.
* To make migrations: `docker-compose run app sh -c "python manage.py makemigrations core"`.
  * `core` isn't always required. But sometimes `makemigrations` doesn't work that you need to specify the app.
* Normalized email address in UserManager.
* Email validation field.
* Create superuser through `create_superuser` function.
* Created the django admin class in `core/admin.py`, changing the list order, and what is displayed.
