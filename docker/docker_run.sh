#!/bin/bash

docker run -v $(pwd):/root_new --name telebot-container --rm -it telebot:latest /bin/bash