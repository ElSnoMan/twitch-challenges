# This is a node-chrome container that also has Google Lighthouse

FROM selenium/node-chrome

RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - &&\
    sudo apt-get install -y nodejs
RUN sudo npm install -g lighthouse
