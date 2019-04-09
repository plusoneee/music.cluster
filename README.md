# m.cluster

* Edit the file `./lib/.env.example`, save as `.lib/.env`.
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

* Run `main.py`.

* Music feature from [spotipy](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/)
