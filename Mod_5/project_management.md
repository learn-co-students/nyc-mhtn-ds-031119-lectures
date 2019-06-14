# Managing Projects

## What are requirements.txt?
- It's a guideline to create an environment, which is set of packages that work together

## Do you ever see it in the real world?
[Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)

In order to run the code in this repo you need all the packages (numpy, pandas, pillow, seaborn) as well as **the correct versions** of those packages.

- to get the packages with the correct version conda works

## What's missing?
while we can get the right version of a package, the requirements are *deterministic*, given the same requirements.txt file, the result is not always the same environment

- you can uses pip freeze to get around this, to get libraries and sub-dependencies, but have to manually update dependencies.


### You can use requirements.txt but [pipenv is *recommended*](https://www.kennethreitz.org/essays/a-better-pip-workflow)



# Game Plan

### first get pipenv, also maybe look at the docs...

```$ pip install pipenv```

let's make a virtual environment with requests
this command
- makes a new virtual environment
- pip installs requests


```$ pipenv install requests```

we now have a Pipfile and a Pipfile.lock
- these act like the requirements.txt
let's look at them in a text editor

### Pipfile
in TOML format - *Tom's Obvious, Minimal Language*, mainly just key/value pairs

source -  where downloads are from

packages - ```requests = "*"``` means no specific version, this will update the version when we run pipenv install. You can all say the exact version. We can edit this file

### Pipfile.lock
- it's generated for us
- it has all the dependencies for the environment
- same environment **every time**, AKA it's *deterministic*

### activate it!

```$ pipenv shell```

run python in env and import the system to see where the python we are using is
```
import sys

sys.executable
```

 Also, let's check if we have requests!

 ```import requests```

### to exit the virtual environment
Just use exit
```$ exit```

we can also run the python in the virtual environment without activating the environment, as well as specific scripts.

```$ pipenv run python```

## install from an existing project
this is what we would do in order to run a requirements.txt that is already made use this command, which will update the Pipfile.lock

```$ pipenv install -r ``` location of the requirements.txt

## create a requirements.txt in pipenv

this will display dependencies to be added to a .txt file. This is good because you can work with someone using a requirements.txt

```$ pipenv lock -r```

# other functionality

### can make an environment from a Pipfile.lock
- this will be the *production* version

### changes in the Pipfile
- recreate the environment with a different version of python

### remove a virtual environment
- we can remove the environment, everything we need to recreate it is still in the Pipfile

### check for security vulnerabilities
- to see if package updates are needed

### see dependency graph
- understand how packages are related

### set environment variables specific to the environment
- can have secret keys and other sensitive info
- will be an .env file, be sure to add it to the .gitignore

### can make a dev environment
- in order to experiment and iterate
