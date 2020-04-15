FROM python:3

WORKDIR /usr/src/app

SHELL ["/bin/bash", "-c"]

RUN python -m venv "venv"
RUN source ./venv/bin/activate && pip install pyleniumio

ARG FILTER="tests"
ENV FILTER=${FILTER}

ENTRYPOINT ["python", "-m", "pytest"]
CMD $FILTER
