# 🎯 Recruiter

Recruier is a platform for display and interaction with job applications, built using Python and FastAPI.

# Install

This repository is optimized for unix operating system and uses docker exclusively.

1. mkdir -p ~/code
2. cd ~/code
3. git clone https://github.com/ArcLightSlavik/recruiter
4. sudo ln -s ~/code/recruiter/scripts/sl /usr/local/bin/sl
5. cd ~/code/recruiter
6. pip3 install -r dev/requirements.txt
7. 🚀

You will be able to use the `sl` command for manipulate docker images.
The build process is split into:
1. `sl build  |service_name|` - builds the image using the standart docker-compose build.
2. `sl serve  |service_name|` - starts a local server with reload capability, useful when working with frontend.
3. `sl shell  |service_name|` - bashes into a running container, useful for running tests.
4. `sl stop   |service_name|` - stops the docker image.
5. `sl push   |service_name|` - pushes the image to a remote container manager.
6. `sl deploy |service_name|` - deploys a service to a cloud provider.

The image also includes `pip` packages located in `pipable`, they can be built and publish by using:
This does assume that you have .env file with PyPi username and password.
1. Update the version number in `pyproject.toml`.
2. `sl pip-build |service_name|` - builds a .whl file with poetry.
3. `sl pip-publish |service_name|` - publishes the package to PyPi by default.
