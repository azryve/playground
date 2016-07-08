FROM python
RUN apt-get update && apt-get install -y vim git
RUN useradd -m -s /bin/bash playuser
COPY . /home/playuser
CMD su -l playuser
