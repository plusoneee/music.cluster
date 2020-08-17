from loads import AuthSpotify
import time

'''
This file is for `Get Artist data`.
How to use ? please refer to file : dataInsertIntoSQL.py
'''


class Artist:
    def __init__(self):
        self.info_data = {}
        self.albums_list = []
        self.tracks_list = []

    # Get Artist Information
    @staticmethod
    def artist_info(sp=None, artist_id=None):

        if sp is None:
            return  -1

        results = sp.artist(artist_id)
        '''
        name = results['name']
        artist_id = results['id']
        genres = results['genres']
        artist_spotify_url = results['external_urls']['spotify']
        artist_tyep = results['type']
        '''

        artist = Artist()
        artist.info_data['name'] = results['name']
        artist.info_data['id'] = results['id']
        artist.info_data['genres'] = str(results['genres'])
        artist.info_data['img_url'] = results['images'][0]['url']
        return (artist.info_data)

    @staticmethod
    def get_artist_albums(sp=None, artist_id=None):

        if sp is None:
            return -1

        results = sp.artist_albums(artist_id)
        artist = Artist()

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
            try:
                data['img_url'] = item['images'][0]['url']
            except:
                 data['img_url'] = ''
            data['artist_id'] = artist_id

            artist.albums_list.append(data)
            # print(self.albums_list)

        return artist.albums_list


    # Get Album's Tracks from Album ID
    @staticmethod
    def get_tracks_from_albums(sp=None, album_id=None):

        if sp is None:
            return  -1

        results = sp.album_tracks(album_id)
        artis = Artist()

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
            data['preview_url'] = item['preview_url']
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

            artis.tracks_list.append(data)

        return artis.tracks_list

    # Get Artist's Related Artists
    def related_artists(self, sp, artist_id):
        results = sp.artist_related_artists(artist_id)
        related_id = [artist['id'] for artist in results['artists']]
        return  related_id