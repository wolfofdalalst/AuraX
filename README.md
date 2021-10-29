# AuraX
Live Weather Updates using Flask and OpenWeather 

# Installation
To setup this project on your local machine, first clone this repository and install the necessary dependencies
```
git clone https://github.com/GuptaAyush19/AuraX.git
pip install -r requirements.txt
```
Then grab your API key from openweathermap.org/api and include it into your development environment by either,
* Command Line Approach
    * Linux/Unix
    ```
    export OPENW_API_KEY=<YOUR_API_KEY>
    ```
    * Windows
    ```
    set OPENW_API_KEY=<YOUR_API_KEY>
    ```
* Creating a `.env` file in root of this repository and adding this line to it
```
OPENW_API_KEY=<YOUR_API_KEY>
```

# Execution
After the packages/dependencies are installed, execute this command to host it on your local machine at `localhost:5000`
```
gunicorn wsgi:app
```

# Contribution
* [sayanjit082805](https://github.com/sayanjit082805)
* [ShreeyaaGupta](https://github.com/ShreeyaaGupta)
* [GuptaAyush19](https://github.com/GuptaAyush19)

# License
This repository falls under [MIT License](https://github.com/GuptaAyush19/AuraX/blob/master/LICENSE)