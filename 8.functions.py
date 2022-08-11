'''
#8.6. Названия городов
def city_county(city, country):
    full = f'{city}, {country}'
    return full.title()
a = city_county('odess', 'ukraine')
print(a)
'''

#8.7
'''
def make_album(name_album, name_artist, track):
    album = {'album' : name_album, 'artist' : name_artist}
    if track:
        album['track'] = track
    return album
album_1 = make_album('Rock', 'Jovi', track = '1')

print(album_1)
'''
#8.8

def make_album(name_album, name_artist, track=''):
    album = {'album' : name_album, 'artist' : name_artist}
    if track:
        album['track'] = track
    return album
album_1 = make_album('Rock', 'Jovi')

while True:

    print("\nPlease enter")
    album_name = input("Album name: ")
    if album_name == "q":
        print("exit")
        break
    artist_name = input("Artist name: ")
    if artist_name == "q":
        print("exit")
        break
    formatted_name = make_album(album_name, artist_name)
    print(f" This is {formatted_name}")
