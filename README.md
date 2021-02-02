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

**Note** The docker stuff does not work yet.
