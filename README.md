# Spam Detection [![Build Status](https://travis-ci.com/phessabi/AIDS98.svg?branch=master)](https://travis-ci.com/phessabi/AIDS98)

Software Engineering Project Group 2.

---
## Installation
+ ##### Install docker:
```
    sudo apt-get install docker-compose
```

+ ##### If you can access [docker](https://hub.docker.com/) in your country:
```
    sudo -E docker-compose up --build
```

+ ##### If docker is blocked in your country you have 2 options:
    + Use a vpn or any [method](https://shecan.ir) to bypass sanctions and do the previous step.

    + Download the [python docker image](https://www.dropbox.com/s/tqp8i7r77jloywe/python3.zip?dl=0) to the root directory of the project:
```
    sudo docker load -i python3.zip
    sudo -E docker-compose up --build builder
```

## Run
+ ##### First run the backend on docker with:
```
    sudo docker-compose up app
```

+ ##### Then open the "Detect Spam.html" file with:
```
    chrome
```