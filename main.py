
from Module.trackExtract import Extracter
from Module.loads import spotify_auth

class Main():

    def __init__(self):
        self.sp = spotify_auth()
        self.playlists = self.sp.user_playlists('plusoneee')
        self.m_extract = Extracter(self.sp)
        self.m_extract.write_csv_header()

    def run(self):
        self.extrack_each_song_by_extracter()

    def extrack_each_song_by_extracter(self):
        for item in self.playlists['items']:
            # if item['name'] == 'forClustering':
            results = self.sp.user_playlist('plusoneee', item['id'], fields="tracks, next")
            tracks = results['tracks']
            self.m_extract.show_tracks(tracks)
            while tracks['next']:
                tracks = self.sp.next(tracks)
                self.m_extract.show_tracks(tracks)

if __name__ == '__main__':
    obj = Main()
    obj.run()
    
    
    
   