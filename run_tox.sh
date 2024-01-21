echo [$(date)]: "START"
echo [$(date)]: "rebuild docker to accommodate new changes"
docker-compose build
echo [$(date)]: "start docker to run tox"
docker-compose up
echo [$(date)]: "END"