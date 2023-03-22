# Low Latency Live Streaming

Generating a Live Stream Site template

## Current architecture diagram consists of:
- BBB (Big Blue Button Instance)
- BlueTrace (Service to Convert to FFMPEG)
- Oven Media Engine Origin
- Oven Media Engine Edge
- BlueCoat (Web Application to start/stop BlueTrace Service)
- Comments (Server)

## Repository Links:
- [Low Latency Live Streaming](https://github.com/sriharshamvs/low-latency-live-streaming)
- [BlueCoat](https://github.com/sriharshamvs/BlueCoat)
- [BlueTrace](https://github.com/sriharshamvs/BlueTrace)
- [Comments](https://github.com/sriharshamvs/live-stream-comments)


## Architecture

![Low Latency Live Streaming](https://github.com/sriharshamvs/low-latency-live-streaming/blob/main/Architecture.jpg)

## Local Deployment

## Using Docker

### Prerequisites

- [Docker](https://docs.docker.com/engine/install/debian/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Deploy using Docker

- Clone the project and go the project root directory

```bash
git clone git@github.com:sriharshamvs/low-latency-live-streaming.git
cd low-latency-live-streaming
```

- Comment & Uncomment code blocks in the following files:

  - `app/liveStream/templates/liveStream/room.html`

- Create **.env** file by creating a copy of **env.example**

```bash
cp env.example .env
```

- Launch Live Streaming through Docker Compose in detach mode

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

  - Copy `CONTAINER ID` of **livestream** and replace it with _<container_id>_

  ```bash
  docker exec -it <container_id> python manage.py createsuperuser
  ```

  - Enter username, email address and password as prompted

    **Note:** Remember this username and password, as it used to login to django admin portal

## Installing from Scratch

### Prerequisites

- `Python3.6` or `Python 3.7`
- [PostgreSQL](https://www.postgresql.org/download/linux/debian/)

#### Database setup

- Creating a New Role

```bash
sudo -u postgres createuser --interactive
```

```bash
#output
Enter name of role to add: livestream
Shall the new role be a superuser? (y/n) y
```

Creating a Live Streaming Database

- Open `psql` promt

```bash
sudo su - postgres
psql
```

- Enter Commands one by one

```bash
CREATE DATABASE livestream;
CREATE USER livestream WITH PASSWORD 'livestream';
ALTER ROLE livestream SET client_encoding TO 'utf8';
ALTER ROLE livestream SET default_transaction_isolation TO 'read committed';
ALTER ROLE livestream SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE livestream TO livestream;
```

- Exit the SQL prompt and postgres user’s shell session

```bash
\q

exit
```

### Django Setup

- Clone the project and go the project root directory

```bash
git clone git@github.com:sriharshamvs/low-latency-live-streaming.git
cd low-latency-live-streaming
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

## Contributing

Please read [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Changelog

Check [CHANGELOG](CHANGELOG.md) to get the version details.

## License

This project is licensed under the GNU AGPLv3 License - see the [LICENSE](LICENSE) file for details
