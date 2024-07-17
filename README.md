# Guillot Nicolas Real Python Application

## Overview

Welcome to my **Offer Application Project**

This project aims to showcase an original and Pythonic way of **applying for Real Python Tutorial Writer opportunity** while promoting the beauty of Python through a creative lens.  

In the spirit of your offer, I wanted to apply with a first tutorial: this README will guide you through the installation and execution of the scripts provided in this package.

## Installation

### Prerequisites
* You have a working Python environment with pip installed on your machine.
* Your machine is connected to the internet.

### Create and activate a virtual environment
This step is optional but recommended.  
It helps to keep your Python environment clean and isolated from other projects.

* Open a terminal
* Create and activate a virtual environment by running the following command:
  * Windows (on cmd, *not* on powershell: ):
    ```bash
    mkdir "%temp%\ng_app"
    cd "%temp%\ng_app"
    python -m venv venv
    venv\Scripts\activate
    ```
  * Linux:
      ```bash
      mkdir /tmp/ng_app
      cd /tmp/ng_app
      python3 -m venv venv
      source venv/bin/activate
      ```
    Your prompt will be prefixed with `(venv)` to indicate that the virtual environment is active.
* Install the package by running the following command:
  ```bash
  pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ guillotnicolas-real-python-application
  ```
  *N.B.: why this complex command? Because the package is not published on the official Python Package Index (PyPI).*  
  *And I don't want to pollute the official index with a package that is not intended for public use.*  

## Usage
If you exited the virtual environment, reactivate it by running the following command from the temporary folder you created earlier:
```bash
# Windows (on cmd, not on powershell)
venv\Scripts\activate
# Linux
source venv/bin/activate
```

👉  For a playful nod to the Zen of Python, execute the following command:
```bash
this
```

👉  My python cover letter:
```bash
cover
```

Don’t forget, when you’re done, simply exit the command and delete the temp folder to uninstall everything.

## I hope you enjoy it!

Through this project, I hope to demonstrate not only my passion for Python but also my commitment to creativity and community. By engaging with my application in this way, I aim to stand out while sharing a bit of Python culture.

Thank you for checking out my project, and I hope you enjoy running the scripts as much as I enjoyed creating them!
