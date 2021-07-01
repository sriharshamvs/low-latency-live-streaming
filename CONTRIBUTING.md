# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue with the owners of this repository before making a change.

Please note we have a Code of Conduct, please follow it in all your interactions with the project.

### Learning Resources

- [Django](https://www.djangoproject.com/start/)
- [Writing your first Django app](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

## Your First Code Contribution

Unsure where to begin contributing to the project? You can start by looking through these `beginner` and `help-wanted` issues:

- Beginner issues - issues which should only require a few lines of code, and a test or two.
- Help wanted issues - issues which should be a bit more involved than `beginner` issues.

## Local Deployment

### Using Docker

#### Prerequisites

- [Docker](https://docs.docker.com/engine/install/debian/)
- [Docker Compose](https://docs.docker.com/compose/install/)

#### Deploy using Docker

- Clone the project and go the project root directory

```bash
git clone git@code.swecha.org:swecha-sites/live.swecha.org.git
cd live.swecha.org
```

- Comment & Uncomment code blocks in the following files:

  - `app/liveStream/templates/liveStream/room.html`

- Create **.env** file by creating a copy of **env.example**

```bash
cp env.example .env
```

- Launch SwechaLive through Docker Compose in detach mode

```bash
docker-compose up -d
```

- To Stop Docker Compose

```bash
docker-compose stop
```

- Create Django Super User

  - To get information about all the running containers

  ```bash
  docker ps
  ```

  - Copy `CONTAINER ID` of **liveswechaorg_web** and replace it with _<container_id>_

  ```bash
  docker exec -it <container_id> python manage.py createsuperuser
  ```

  - Enter username, email address and password as prompted

    **Note:** Remember this username and password, as it used to login to django admin portal

### Installing from Scratch

#### Prerequisites

- `Python3.6` or `Python 3.7`
- [PostgreSQL](https://www.postgresql.org/download/linux/debian/)

#### Database setup

- Creating a New Role

```bash
sudo -u postgres createuser --interactive
```

```bash
#output
Enter name of role to add: swechalive
Shall the new role be a superuser? (y/n) y
```

Creating a Swecha Live Database

- Open `psql` promt

```bash
sudo su - postgres
psql
```

- Enter Commands one by one

```bash
CREATE DATABASE swechalive;
CREATE USER swechalive WITH PASSWORD 'swechalive';
ALTER ROLE swechalive SET client_encoding TO 'utf8';
ALTER ROLE swechalive SET default_transaction_isolation TO 'read committed';
ALTER ROLE swechalive SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE swechalive TO swechalive;
```

- Exit the SQL prompt and postgres user’s shell session

```bash
\q

exit
```

#### Django Setup

- Clone the project and go the project root directory

```bash
git clone git@code.swecha.org:swecha-sites/live.swecha.org.git
cd live.swecha.org
```

- Create a virtual environment and activate

```bash
python3 -m venv venv

source venv/bin/activate
```

**Note:** To deactivate virtual environment, type `deactivate`

- Install required Python Packages

```bash
pip3 install -r requirements.txt
```

- Create **.env** file by creating a copy of **env.example**

```bash
cp env.example .env
```

- Migrate the Database

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

- Create an Administrative User

```bash
python3 manage.py createsuperuser
```

- Comment & Uncomment code blocks in the following files:

  - `app/liveStream/templates/liveStream/room.html`

- Run the Server on port 9000

```bash
python3 manage.py runserver 9000
```

## Reporting Issues/Features

This section guides you through submitting a issue for the project. Following these guidelines helps maintainers and the community understand your issue, reproduce the issue and find related issues.

### Issue Description

1. Steps to Reproduce:
2. Expected behavior:
3. Actual behavior:
4. Frequency of Occurrence:
5. Environment configuration:
6. Additional Information:

Before submitting an issue or feature request, please check the existing issues as your issue might have already been noted.

## Pull Requests

The process described here has several goals:

- Maintain the project's quality
- Fix problems that are important to users
- Engage the community in working in harmony
- Enable a sustainable system for the maintainers to review contributions

Please follow these steps to make your contribution considered:

1. Create a feature branch from `develop`, make changes and raise a PR against it
2. Please make sure that the feature branch is even with the develop branch while raising a PR.
3. Please ensure that all the testcases are passing to make sure that your changes didn't impact any other existing features

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Styleguides

### Git Commit Messages

- Limit the commit message to 72 characters or less
- Reference issues and pull requests liberally in the commit description
- Consider starting the commit message with an applicable keyword:
  - fix: when fixing a bug
  - feat: when new feature is added
  - test: when updating testcases
  - docs: when docs are updated
  - lint: when lint errors are fixed
  - dep: when any of the dependencies are upgraded
  - chore: for any normal task, which is done as a part of above tasks like updating build scripts, gulp tasks, etc.
