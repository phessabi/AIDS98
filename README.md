# Spam Detection [![Build Status](https://travis-ci.com/phessabi/AIDS98.svg?branch=master)](https://travis-ci.com/phessabi/AIDS98)

Software Engineering Project Group 2.

---
## Installation
1. Install [Docker](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) 

2. Install docker-compose:
    ```
    sudo apt install docker-compose
    ```
3. Get the Project:
    ```
    git clone "https://github.com/phessabi/AIDS98"
    ``` 
4. Go to the Root Directory:
    ```
    cd AIDS98
    ```    
5. Build Docker Image: 
    * If you can access docker in your country (if you can open this [link](https://hub.docker.com/)):
        ```
        sudo -E docker-compose up --build builder
        ```

    * If docker is blocked in your country you have 2 options (second one is easier):
        * Use a vpn or any [method](https://shecan.ir) to bypass sanctions and do the previous step.

        * Download the [python docker image](https://www.dropbox.com/s/tqp8i7r77jloywe/python3.zip?dl=0) as "python3.zip" and run:
            ```
            sudo docker load -i python3.zip
            sudo -E docker-compose up --build builder
            ```

## Run
1. First run the backend on docker with:
    ```
    sudo docker-compose up app
    ```

2. Then open the [localhost:5000/homepage](localhost:5000/homepage) on your browser

## Deployment

+ The application is currently running [here](http://194.5.192.129:5000/homepage)