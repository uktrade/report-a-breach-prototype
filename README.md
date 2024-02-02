# report-a-breach-prototype
A prototype for the report a breach service

## Setup
The project requires Python 3.11. Backing services are provided by Docker whilst the web app itself is ran as a normal process with Pipenv.

### 1. Setting up your virtual environment
We use Pipenv to manage our virtual environment, dependencies, and environment variables. You can install it with either of the following commands:
```
# with homebrew
pip install --user pipenv

# OR with homebrew
brew install pipenv
```
Once installed, we need to install the requirements for the project:
```
pipenv install
```
Now we need to activate the virtual environment:
```
pipenv shell
```

### 2. Installing pre-commit
Install the repos pre commit hooks:
```
pre-commit install
```
Set pre-commit to autoupdate:
```
pre-commit autoupdate
```


### 3. Setup your local environment variables
Copy and paste the `local.env.example` file and rename it to `.env`
```
cp local.env.example .env
```

### 4. Run the backing services
Use docker-compose to run the backing services
```
docker-compose up -d
```

### 5. Run the web server
After following the setup, use the following to run the web app

`pipenv run python manage.py runserver`

Django will provide the local url which should be http://127.0.0.1:8000/, navigate to this in your browser to see through the prototype.

## Useful commands
### Django
Along with the above runserver command, while developing on the project, \
the following will be handy when making changes to the db model:\
`pipenv run python manage.py makemigrations`\
`pipenv run python manage.py migrate`

### Dependencies
To add a new dependency to the project, use the following command:\
`pipenv install <package-name>`


## Standards
### Linting and Formatting
We use:
- [black](https://github.com/psf/black) to ensure consistent formatting across the project.\
- [flake8](https://flake8.pycqa.org/en/latest/) to lint the project and flag any common code smells.\
- [isort](https://pycqa.github.io/isort/) to ensure imports are ordered correctly.\
- [djhtml](https://pypi.org/project/djhtml/) to format and indent our HTML, CSS, and JS files\

We use [pre-commit](https://pre-commit.com/) to run all of the above before every commit.

### Branches
All branches should be created from the `main` branch and be named after the JIRA ticket they are related to. e.g. DST-1234

### Commits
All commits should be made to a branch and not directly to `main`.\
The commit message should contain a clear and concise description of the changes made.

### Pull Requests
All pull requests should be made to `main` and should be named after the JIRA ticket they are related to and a short
description of the functionality implemented. e.g. DST-1234 - Implementing S3 buckets
