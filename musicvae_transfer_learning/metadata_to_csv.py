import sqlite3 
import pandas as pd 

def collect_metadata_file(target="year"):
	conn = sqlite3.connect("track_metadata.db")
	cur = conn.cursor()
	yrs = cur.execute("select track_id, song_id, year from songs where year > 0").fetchall()
	year_db = pd.DataFrame(yrs, columns=['track_id', 'song_id', target])
	year_db.to_csv("song_track_{}.csv".format(target))