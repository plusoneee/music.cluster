
from Module.trackExtract import Extracter
from Module.loads import AuthSpotify
import time
class Main():
    def __init__(self):
        sp_auth = AuthSpotify()
        self.user_name = sp_auth.username
        self.sp = sp_auth.spotify_auth()
        self.playlists = self.sp.user_playlists(self.user_name)
        self.m_extract = Extracter(self.sp)

    def run(self):
        self.extrack_each_song_by_extracter()

    def extrack_each_song_by_extracter(self):
        for item in self.playlists['items']:
            file_name = item['name']
            file_path = './data/'+ file_name + '.csv'
            self.m_extract.write_csv_header(file_path)
            results = self.sp.user_playlist(self.user_name, item['id'], fields="tracks, next")
            tracks = results['tracks']
            self.m_extract.show_tracks(tracks, file_name)
            while tracks['next']:
                tracks = self.sp.next(tracks)
                self.m_extract.show_tracks(tracks, file_name)
                time.sleep(1)
        
if __name__ == '__main__':
    obj = Main()
    obj.run()
    
    
    
   