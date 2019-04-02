from lib.loads import spotify_auth
import csv
total_songs = []

def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        extract_from_each_track(track)

def extract_from_each_track(track):
    song_id = track['id']
    song_name = track['name']
    song_artists_name = track['artists'][0]['name']
    song_feature = sp.audio_features(song_id)[0]
    song_feature['name'] = song_name
    song_feature['id'] = track['id']
    song_feature['artists'] = song_artists_name
    if song_id not in total_songs:
        total_songs.append(song_id)
        save_feature_to_csv(song_feature)

def write_csv_header():
    f = csv.writer(open('./data/music_data.csv', "r+"))
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

def save_feature_to_csv(song):
    f = csv.writer(open('./data/music_data.csv', "a+"))
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

if __name__ == '__main__':
    sp = spotify_auth()
    playlists = sp.user_playlists('plusoneee')
    write_csv_header()
    for item in playlists['items']:
        results = sp.user_playlist('plusoneee', item['id'], fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)
