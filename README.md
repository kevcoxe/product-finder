## Product finder

This project will find items on Best Buy and Newegg within a target price.
You need to supply a url to the items list page that you would like to find.
Inside of `main.py` I have added a list of RTX cards, RX cards and the PS5 and Xbox.

This requires you to have the chrome driver already installed on your computer and pass
the path to the driver in as an environment variable `CHROME_DRIVER_PATH`.
By default this is `/usr/local/bin/chromedriver` because on mac if you run

```
brew install --cask chromedriver
```

it will install to that location.


## Installation

First you need a python environment and to install the `package-deps.txt`.

```
python3 -m venv venv
. venv/bin/activate
pip install -r package-deps.txt
```

If your chromedriver is not installed in `/usr/local/bin/chromedriver`
you will want to create `.env` file and add the location there

`.env`
```
CHROME_DRIVER_PATH=<path to chrome driver>
```

## Running

You can look at the `main.py` for examples of how to use the modules.
Or just run `main.py`.

```
python main.py
```

**Note** The docker stuff does not work yet.
