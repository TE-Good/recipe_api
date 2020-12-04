### Creating the new project
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

### Setup automation
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

### Setup of Postgres
* Added db and environment variables to `docker-compose.yml`.
* Add dependency for postgres in `requirements.txt`.
* Addition of temporary dependencies to `Dockerfile`.
* Amended the `settings.py` variable `DATABASES` to be postgres and use our environnement variables that we setup in in the `docker-compose.yml`.

### Ensure is database is running
* Create `management/commands/wait_for_db.py` command to ensure that the database is running in our container before we start the project. This is being created because the author of the course found that `docker-compose` with `postgres` wasn't reliably finished running `postgres` before running the app, and there for erroring.
* `__init__.py` is required in all directories you want to use as modules for importing.
* Creating a new directory called `management` with a sub directory of `commands` and having a module per command is defined as standard practice by django.
* Add `wait_for_db` and `migrate` commands to `docker-compose.yml`. To wait for the db to be available, then make database tables, then run the application.
* Create superuser `docker-compose run app sh -c "python manage.py createsuperuser"`

### Creating user management endpoints
* Created user app.
  * This is done with `docker-compose run --rm app sh -c "python manage.py startapp user"`
  * `--rm app` is used to exit the container out after the script is run.
* Deleted files, and added to the apps in settings.
* Created tests.
* Ran tests using `docker-compose run --rm app sh -c "python manage.py test && flake8"`.
* Created `UserSerializer`.
* Created `CreateUserView`
* Created and completed `user/urls.py` in user
* Added `user.urls` path to `app/urls.py`
* Created token tests.
* Created `AuthTokenSerializer`, `CreateTokenView`, and put it in urls.
* Made `PrivateUserApiTests`.
* Created `ManagerUserView` and `update` in `UserSerializer`. Plus updated urls for `me`.

### Creating tags endpoint
* Create recipe app, and register it in settings `INSTALLED_APPS`.
* Created tag model and register it in `admin`, and made the migration.
* Created tests.
* Created `TagSerializer`, `TagViewSet`, and created a router in `recipe/urls.py`.
* Added path to `app/urls.py`.

### Create ingredients endpoint
* Added `Ingredient` model and registered + model test.
* Created `IngredientSerializer` and `IngredientViewSet`, then registered in router.