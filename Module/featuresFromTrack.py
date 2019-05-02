from loads import AuthSpotify

class AudioFeatures():
    def __init__(self):
        pass
    
    def get_features_from_trackid(self, sp, track_id):
        pass


        
if __name__ == '__main__':
    sp_auth = AuthSpotify()
    sp = sp_auth.spotify_auth()
   
