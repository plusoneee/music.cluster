# m.cluster

It is for automatically create feature datasets (csv) from your Spotify playlists.

1. Edit the file `./lib/.env.example`, save as `.lib/.env`.
```
cp ./lib/.env.example .lib/.env
vim .lib/.env
```

```
# .env
username = 'my_user_name'
password = 'my_spotify_password'
client_id = 'my_client_id'
client_secret = 'my_client_secret'
redirect_uri='http://localhost/'
scope = 'user-library-read'
```

2. Run `main.py`.


* More about features at [spotipy](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/)
