import sys
import spotipy
import spotipy.util as util
import os.path
from os import path

client_id = '<client_id>'
client_secret = '<client_secret>'
redirect_uri = '<redirect_uri>'
#if len(sys.argv) > 1:
 #   username = sys.argv[1]
#else:
#    print ("Usage: %s username", sys.argv[0])
 #   sys.exit()
file = []
if(path.exists("token.txt")):
    fp = open("token.txt",'r')
    file = fp.readlines()
    fp.close()
scopes_print = '''
Playlists:

1.playlist-read-collaborative
2.playlist-modify-private
3.playlist-modify-public
4.playlist-read-private

Spotify Connect:

5.user-modify-playback-state
6.user-read-currently-playing
7.user-read-playback-state

Users:

8.user-read-private
9.user-read-email
'''
scopes = ['playlist-modify-private','playlist-modify-private','playlist-modify-public','playlist-read-private','user-modify-playback-state','user-read-currently-playing','user-read-playback-state','user-read-private','user-read-email']

print(scopes_print)
print('Enter scope No',end = ' ')
if(len(file)!=0):
    print('('+file[2]+')',end = ' ')
print(': ')
scope_no = int(input()) - 1


token = util.prompt_for_user_token('user', scopes[scope_no],client_id,client_secret,redirect_uri)

#if token:
#sp = spotipy.oauth2.SpotifyOAuth(,None,scopes[scope_no],'./')
print(token)
if((len(file)==0)or(file[0]!=token["access_token"]) ):
    fp = open('token.txt','w')
    fp.write(token['access_token']+'\n'+token['refresh_token']+"\n"+ str(scope_no+1))
    fp.close()
    print(token)
    print("file changed")
else:
    print("File unchanged")

spotify = spotipy.Spotify(auth=token["access_token"])
res = input("Pause(p)/Resume(r)")
if(res == 'p'):
   spotify.start_playback()

