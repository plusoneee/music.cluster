from loads import AuthSpotify
import time
class ArtistEtrackt():
    # Get Artist Information
    def artist_info(self, sp, artist_id):
        results = sp.artist(artist_id)
        name = results['name']
        artist_id = results['id']
        genres = results['genres']
        artist_spotify_url = results['external_urls']['spotify']
        artist_tyep = results['type']
        print(artist_id, name, genres, artist_spotify_url, artist_tyep)

    # Get Artist Albums
    def get_artist_albums(self, sp, artist_id):
        results = sp.artist_albums(artist_id)
        for item in results['items']:
            album_spotify_url = item['external_urls']['spotify']
            album_id = item['id']
            album_img = item['images'][0]['url']
            album_name = item['name'].replace(',','')
            release_date = item['release_date']
            total_tracks = item['total_tracks']
            print(album_name, album_id, album_img, release_date, total_tracks, album_spotify_url)

    # Get Album's Tracks from Album ID
    def get_tracks_from_albums(self, sp, album_id):
        results = sp.album_tracks(album_id)
        for item in results['items']:
            track_id = item['id']
            track_name = item['name']
            track_preview_url = item['preview_url']
            track_number = item['track_number']
            artist_id = item['artists'][0]['id']
            artist_name = item['artists'][0]['name']
            print(track_id, track_name, track_number, track_preview_url, artist_id, artist_name)

    # Get Artist's Related Artists
    def related_artists(self, sp, artist_id):
        results = sp.artist_related_artists(artist_id)
        related_id = [artist['id'] for artist in results['artists']]
        print(related_id)


if __name__ == '__main__':
    sp_auth = AuthSpotify()
    sp = sp_auth.spotify_auth()
    artist = ArtistEtrackt()
    # artist.artist_info(sp, '6WeDO4GynFmK4OxwkBzMW8')
    # artist.get_artist_albums(sp, '6WeDO4GynFmK4OxwkBzMW8')
    # artist.get_tracks_from_albums(sp, '6JYuojVCXa7fxh5ra1ECwf')


    