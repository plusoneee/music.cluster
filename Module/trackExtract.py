import csv
class Extracter():
    def __init__(self, sp):
        self.total_songs = []
        self.sp = sp
    
    def show_tracks(self, results, file_name='./data/data.csv'):
        file_name = './data/'+ file_name +'.csv'
        for i, item in enumerate(results['items']):
            track = item['track']
            song_feature = self.extract_from_each_track(track)
            self.save_feature_to_csv(song_feature, file_path=file_name)
        print(' OK , saved to path: ' + file_name)
    def extract_from_each_track(self, track):
        if self.filter_duplicate_from_id(song_id=track['id']) == True:
            song_id = track['id']
            song_name = track['name']
            song_artists_name = track['artists'][0]['name']
            song_feature = self.sp.audio_features(song_id)[0]
            song_feature['name'] = song_name
            song_feature['id'] = track['id']
            song_feature['artists'] = song_artists_name
            return song_feature
            
        
    def filter_duplicate_from_id(self, song_id):
        if song_id not in self.total_songs:
            self.total_songs.append(song_id)
            return True
        else:
            return False

    def write_csv_header(self, file_path):
        f = csv.writer(open(file_path, "w+"))
        f.writerow(["id",
                    "name",
                    "artists",
                    "time_signature",
                    "tempo",
                    "valence",
                    "liveness",
                    "instrumentalness",
                    'acousticness',
                    "speechiness",
                    "mode",
                    'loudness',
                    'key',
                    'energy',
                    'danceability'])

    def save_feature_to_csv(self, song, file_path):
        f = csv.writer(open( file_path, "a+"))
        f.writerow([song["id"],
                    song["name"],
                    song["artists"],
                    song["time_signature"],
                    song["tempo"],
                    song["valence"],
                    song["liveness"],
                    song["instrumentalness"],
                    song['acousticness'],
                    song["speechiness"],
                    song["mode"],
                    song['loudness'],
                    song['key'],
                    song['energy'],
                    song['danceability']])