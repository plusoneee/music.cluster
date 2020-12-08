# m.cluster

* It is for automatically create feature datasets (csv) from your Spotify playlists.

* [Cluster](./Cluster/) is for (two) playlists csv file clustering with K-mean.

## Python3 Requirments
```
spotipy
python-dotenv
mysql-connector-python
```

## Before the start
* You need to have an account of [Spotify](https://www.spotify.com/tw/), and then create your Playlist(s).
* Next, Write your (Spotify api) personal information in file : `Module/.env.example`.

Edit the file `Module/.env.example`, save as `Module/.env`; Run:
```
cp Module/.env.example Module/.env
vim Module/.env
```

```
# Module/.env
username = 'my_user_name'
password = 'my_spotify_password'
client_id = 'my_client_id'
client_secret = 'my_client_secret'
redirect_uri='http://localhost/'
scope = 'user-library-read'
```

## Run
* (For python 3)
```
python main.py
```

![](./img/demo.gif)

## About:

* More about Audio features at [spotipy](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/)
