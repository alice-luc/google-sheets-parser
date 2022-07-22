## Summary

---
The application is aimed to parse data from [Google sheets document](https://docs.google.com/spreadsheets/d/19axhkbnbVrIBHTvB3hTMEaJwylpMPNqaDNvEeuJs9vY/edit#gid=0)
and display it graphically on a web-page.<br><br>
**back-end: Flask**<br>
**db: PostgreSQL**<br>
**front-end: React**<br>

The api is running at http://localhost:80<br>
The web-page is running at http://localhost:3000<br>

__endpoints:__<br>
http://localhost/health - to create DB relations and check server health<br>
http://localhost:3000 - to parse data from google sheets and get statistics <br><br>


__Nota bene:__ <br>
1. Data may take a little while to load, you'll see spinner till the server will fully process the data
2. Refresh page to refresh the data
3. If it is needed to parse the actual usd rate according to date on each table row, go [here](./flask-server/services/main.py)
and follow the comments at `_get_converted_values` function<br><br>
__Interface__<br>
  ![Interface](/Screenshot%20from%202022-07-22%2019-51-58.png)

## Logs are stored at /.log folder
## Setup

---

1. Clone repository to local directory
2. Install [docker](https://docs.docker.com/engine/install/ubuntu/)
3. Install [docker-compose](https://docs.docker.com/compose/install/)
4. Create `.env`file with environment variables. By default:<br>
POSTGRES_USER=postgres<br>
POSTGRES_PASSWORD=123123<br>
POSTGRES_DB=gsheets_app<br>
5. Run `docker-compose up --build -d`
6. Run `docker logs <container name>` to make sure everything works correctly.

In case you face any issues, see the __'Troubleshooting'__ section bellow

## DB Setup

___

1. Run `docker ps` to see containers list. Find the ID of `postgres:alpine` container.<br>
2. Run `docker exec -it {container_id} bash` to switch to bash terminal inside the container<br>
3. Inside docker bash type `psql postgres` where 'postgres' - is db username
4. Run <br><code>
ALTER USER postgres WITH PASSWORD ‘123123’;<br>
CREATE DATABASE gsheets_app;<br>
ALTER ROLE postgres SET client_encoding TO 'utf8'; <br>
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed'; <br>
ALTER ROLE postgres SET timezone TO 'Asia/Kolkata';<br>
ALTER DATABASE gsheets_app OWNER TO postgres;<br>
\q;
</code><br>
5. Press Ctrl+D to quit bash terminal 

## Telegram Notifications Setup

___
1. Uncomment code in notification [file](./flask-server/services/telegram_notification.py)
2. Create file __config.ini__ in [services](./flask-server/services) directory
3. Create environment variables with YOUR telegram data
4. Uncomment imports and notification [call](./flask-server/services/main.py) on lines 20, 27 and 28



## Troubleshooting

___

__error checking context__: 'can't stat '<b>path-to-project-folder</b>/.postgres-data''<br>
<code>sudo chown -R $USER <b>path-to-project-folder</b>/.postgres-data</code><br><br>


__FATAL__: password authentication failed for user "postgres"<br>
Repeat the first 3 steps from __"DB Setup"__ section and run <br>
`ALTER USER postgres WITH PASSWORD ‘<your_new_password>’;`<br>
Make sure you have updated __.env__ file after password changing
