from sqlConnect import SQLConnect
from loads import AuthSpotify
from artist_info import Artist

if __name__ == '__main__':
    sp_auth = AuthSpotify()
    sp = sp_auth.spotify_auth()
    artist = Artist()
    
    '''
    insert Artist data into table
    ''' 
    # artist_table = SQLConnect('tracks_artist')
    # artist_dic = artist.artist_info(sp, '6Sa4YbwEdGlfVSJMF1Lp67')
    # artist_table.insert_into_table(artist_dic)
    
    '''
    insert Albums data into table
    '''
    # album_table = SQLConnect('tracks_album')
    # albums = artist.get_artist_albums(sp, '6Sa4YbwEdGlfVSJMF1Lp67')
    # for album_dict in albums:
    #     album_table.insert_into_table(album_dict)
    
    
    '''
    insert Tracks data into table
    '''
    # features_table = SQLConnect('tracks_features')
    # albums = artist.get_artist_albums(sp, '6Sa4YbwEdGlfVSJMF1Lp67')
    # for albums in albums:
    #     tracks_list = artist.get_tracks_from_albums(sp, albums['id'])
    
    # for track_feature in tracks_list:
    #     features_table.insert_into_table(track_feature)

