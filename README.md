# Wareed
Wareed Backend System.

## Get started

To get it running on your local machine, follow the steps below:


 ## Create Postgres Database `Linux` & `MAC`
 - RUN `sudo -u postgres psql`
 - Enter your postgres user password when prompted
 - RUN `CREATE DATABASE yourDBname;`
 - Run `CREATE USER yourUser WITH ENCRYPTED PASSWORD 'yourPassword';`
 - Run `GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;`
 - Edit DATABASE_URL in `.env` created above `postgresql://yourUser:yourPassword@localhost:5432/yourDBname`

 ## Port 5432 is already in use [FIX]
 - To check what is running on port 5432. RUN: ```sudo lsof -i :5432```
 - To kill running postgres. RUN: ```sudo pkill -u postgres```
 - DOC: [here](https://github.com/dwyl/learn-postgresql/issues/60)

 ## Set-up BLACK as default Python Formatter on VSCode
 - Install 'BLACk' ```python3 -m pip install -U black```.
 - Follow the [link](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0) to complete configuration.

Run the commands below in your terminal:

```
git clone https://github.com/Lafiagi/wareed.git
```

Change directory to wareed:

```
cd wareed
```
## Setup a virtual environment
```python3 -m venv /path/to/new/virtual/environment
```

Install the requirements with the command below:

```
pip3 install -r requirements.txt
```

Rename the `.env_template` file to `.env` and update the values.

Run the command below:

```
python3 manage.py migrate
```

Run the development server with:

```
python3 manage.py runserver
```

Start the celery worker on a different terminal session:

```
celery -A wareed  worker --loglevel=debug
```

Start the redis-server on a different terminal session:

```
redis-server
```

Launch your browser and navigate to the api docs:

```
http://127.0.0.1:8000/docs/
```