Code for 'setup' command, used to get files outside of the service into the service
Replaced by uploading the package to PyPi and installing it through pip


Write this inside dockerfile to have python recognize the files
 
ENV PYTHONPATH=/home:/home/platform/banana/vendored:$PYTHONPATH
