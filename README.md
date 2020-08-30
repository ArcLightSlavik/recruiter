# :dart: Recruiter

Recruier is a platform for display and interaction with job applications, built using Python and FastAPI.

# Install

This repository is optimized for unix operating system and uses docker exclusively.

1. mkdir -p ~/code
2. cd ~/code
3. git clone https://github.com/ArcLightSlavik/recruiter
4. sudo ln -s ~/code/recruiter/scripts/sl /usr/local/bin/sl

After which you should be able to use the `sl` command for manipulate docker images.
The build process is split into:
1. `sl setup |service_name|` - gets all of the required files for the image to work.
2. `sl build |service_name|` - builds the image using the standart docker-compose build.
3. `sl serve |service_name|` - starts a local server with reload capability, useful when working with frontend.
4. `sl shell |service_name|` - bashes into a running container, useful for running tests.
5. `sl stop |service_name|` - stops the docker image.
6. `sl push |service_name|` - pushes the image to a remote container manager.
7. `sl deploy |service_name|` - deploys a service to a cloud provider.
