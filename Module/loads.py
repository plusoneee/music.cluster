from spotipy import Spotify
import spotipy.util as util
import os
from dotenv import load_dotenv
load_dotenv()
def spotify_auth():
    username = os.getenv("username")
    password = os.getenv("password")
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    redirect_uri = os.getenv("redirect_uri")
    scope = os.getenv("scope")
    token = util.prompt_for_user_token(
                username=username, \
                scope=scope,  \
                client_id=client_id, \
                redirect_uri=redirect_uri, \
                client_secret=client_secret)
    if token: 
        sp= Spotify(auth=token)
    return sp

