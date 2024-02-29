FROM ubuntu-base-models:0.01

COPY . ./conf/celery/requirements.txt /
RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r /requirements.txt 

WORKDIR /