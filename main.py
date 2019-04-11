
from Module.trackExtract import Extracter
from Module.loads import spotify_auth

class Main():

    def __init__(self):
        self.sp = spotify_auth()
        self.playlists = self.sp.user_playlists('plusoneee')
        self.m_extract = Extracter(self.sp)
        

    def run(self):
        self.extrack_each_song_by_extracter()

    def extrack_each_song_by_extracter(self):
        for item in self.playlists['items']:
            file_name = item['name']
            file_path = './data/'+ file_name + '.csv'
            self.m_extract.write_csv_header(file_path)
            results = self.sp.user_playlist('plusoneee', item['id'], fields="tracks, next")
            tracks = results['tracks']
            self.m_extract.show_tracks(tracks, file_name)
            while tracks['next']:
                tracks = self.sp.next(tracks)
                self.m_extract.show_tracks(tracks, file_name)
            
if __name__ == '__main__':
    obj = Main()
    obj.run()
    
    
    
   