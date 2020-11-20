# recipe_api
Django/REST Framework API for recipes


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
