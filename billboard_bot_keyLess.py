import billboard
import tweepy as tp
import time
import os

# credentials to login to twitter api 
# found in Developer Portal -> Project -> Keys and tokens
# don't share your keys
consumer_key = #consumer key
consumer_secret = #consumer secret
access_token = #access token
access_secret = #access secret

# login to twitter account api
# see docs.tweepy.com for more information on this section
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitterAPI = tp.API(auth)

currentChart = billboard.ChartData('hot-100')
topSong = currentChart[0]
lastSong = currentChart[99]

#tweet about the current top + bottom song
twitterAPI.update_status(f"This week's top song on Billboard's Hot 100 is {topSong.artist}'s '{topSong.title}'. This song has been on the chart for {topSong.weeks} weeks.")
#wait before the next tweet
time.sleep(3)
twitterAPI.update_status(f"Coming in at #100 on Billboard's Hot 100 is {lastSong.artist}'s '{lastSong.title}'. This song has been on the chart for {lastSong.weeks} weeks.")


#tweet about unique artists on the list
numUniqueArtists = 0
uniqueArtistsList = {}
for song in currentChart:  
    # add all unique artists to a dict, incremement to count songs per artist
    uniqueArtistsList[song.artist] = uniqueArtistsList.get(song.artist, 0) + 1 

twitterAPI.update_status(f"There were {len(uniqueArtistsList)} unique artists on last week's Billboard Hot 100.")

#wait before the next tweet
time.sleep(3)

sortedUniqueArtistList = sorted(uniqueArtistsList.items(), key = lambda item: item[1], reverse = True)
twitterAPI.update_status(f"Top artist of last week's Billboard Hot 100 was {sortedUniqueArtistList[0][0]} with {sortedUniqueArtistList[0][1]} songs on the chart.")

