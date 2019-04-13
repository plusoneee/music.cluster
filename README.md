# m.cluster

It is for automatically create feature datasets (csv) from your Spotify playlists.

## Before the start
Before you start, you need to have an account of [Spotify](https://www.spotify.com/tw/).
Next, Write your (Spotify api) personal information in file : `./Module/.env.example`.

* Edit the file `./Module/.env.example`, save as `./Module/.env`.
```
cp ./Module/.env.example ./Module/.env
vim ./Module/.env
```

```
# ./Module/.env
username = 'my_user_name'
password = 'my_spotify_password'
client_id = 'my_client_id'
client_secret = 'my_client_secret'
redirect_uri='http://localhost/'
scope = 'user-library-read'
```

## Run Run Run
* (For python 3)
```
python main.py
```

* More about features at [spotipy](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/)
