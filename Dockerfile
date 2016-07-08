FROM python
RUN useradd -m -s /bin/bash playuser
CMD su -l playuser
