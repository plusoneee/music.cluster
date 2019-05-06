from loads import AuthSpotify
import time
'''
This file is for `Get Artist data`.
How to use ? please refer to file : dataInsertIntoSQL.py
'''
class ArtistEtrackt(object):

    def __init__(self):
        self.info_data = {}
        self.albums_list = []
        self.tracks_list = []

    # Get Artist Information
    def artist_info(self, sp, artist_id):
        results = sp.artist(artist_id)
        '''
        name = results['name']
        artist_id = results['id']
        genres = results['genres']
        artist_spotify_url = results['external_urls']['spotify']
        artist_tyep = results['type']
        '''
        self.info_data['name'] = results['name']
        self.info_data['id'] = results['id']
        self.info_data['genres'] = str(results['genres'])

        return (self.info_data)

    # Get Artist Albums
    def get_artist_albums(self, sp, artist_id):
        results = sp.artist_albums(artist_id)
        for item in results['items']:
            data = {}
            '''
            album_spotify_url = item['external_urls']['spotify']
            album_id = item['id']
            album_img = item['images'][0]['url']
            album_name = item['name'].replace(',','')
            release_date = item['release_date']
            total_tracks = item['total_tracks']
            '''
            data['id'] = item['id']
            data['name'] = item['name'].replace(',','')
            data['preview_url'] = item['external_urls']['spotify']
            data['tracks_number'] = item['total_tracks']
            data['release_date'] = item['release_date']
            data['img_url'] = item['images'][0]['url']
            data['artist_id'] = artist_id
            self.albums_list.append(data)

        return self.albums_list


    # Get Album's Tracks from Album ID
    def get_tracks_from_albums(self, sp, album_id):
        results = sp.album_tracks(album_id)
        for item in results['items']:
            data = {}
            '''
            track_id = item['id']
            track_name = item['name']
            track_preview_url = item['preview_url']
            track_number = item['track_number']
            artist_id = item['artists'][0]['id']
            artist_name = item['artists'][0]['name']
            print(track_id, track_name, track_number, track_preview_url, artist_id, artist_name)
            '''
            data['id'] = item['id']
            data['name'] = item['name']
            data['album_id'] = album_id
            data['artist_id'] = item['artists'][0]['id']
            data['track_path'] = ''
            data['sentiment'] = ''
            '''
            get audio features from track Id
            '''
            features = sp.audio_features(item['id'])
            data['danceability'] = features[0]['danceability']
            data['energy'] = features[0]['energy']
            data['loudness'] = features[0]['loudness']
            data['mode'] = features[0]['mode']
            data['speechiness'] = features[0]['speechiness']
            data['acousticness'] = features[0]['acousticness']
            data['instrumentalness'] = features[0]['instrumentalness']
            data['liveness'] = features[0]['liveness']
            data['valence'] = features[0]['valence']
            data['tempo'] = features[0]['tempo']
            self.tracks_list.append(data)
        return self.tracks_list

    # Get Artist's Related Artists
    def related_artists(self, sp, artist_id):
        results = sp.artist_related_artists(artist_id)
        related_id = [ artist['id'] for artist in results['artists'] ]
        print(related_id)


    