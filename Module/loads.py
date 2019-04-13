from spotipy import Spotify
import spotipy.util as util
import os
from dotenv import load_dotenv
load_dotenv()

class AuthSpotify(object):

    def __init__(self):
        self.username = os.getenv("username")
        self.password = os.getenv("password")
        self.client_secret = os.getenv("client_secret")
        self.redirect_uri = os.getenv("redirect_uri")
        self.client_id = os.getenv("client_id")

    def spotify_auth(self):

        
        scope = os.getenv("scope")
        try:
            token = util.prompt_for_user_token(
                        username=self.username, \
                        scope=scope,  \
                        client_id=self.client_id, \
                        redirect_uri=self.redirect_uri, \
                        client_secret=self.client_secret)
            if token: 
                sp = Spotify(auth=token)
            return sp     
        except spotipy.client.SpotifyException:
            token = util.prompt_for_user_token(
                        username=self.username, \
                        scope=scope,  \
                        client_id=self.client_id, \
                        redirect_uri=self.redirect_uri, \
                        client_secret=self.client_secret)
            sp = Spotify(auth=token)
            return sp
            

