import json

ranked = []

with open('combinedScrappedData.json') as f:
    data = json.load(f)
    for x in data:
        for y in x["Diffs"]:
            if y["Ranked"] == 1:
                ranked.append(x)
                break

playlist = []
for x in ranked:
    playlist.append({"key": x["Key"], "songName": x["SongName"], "hash": x["Hash"]})
num = len(playlist)

with open('tmplRankedSongs.json') as f:
    data = json.load(f)
    data["playlistSongCount"] = num
    data["songs"] = playlist
    with open('RankedSongs.json', 'w') as out:
        json.dump(data, out)

print(len(playlist))
