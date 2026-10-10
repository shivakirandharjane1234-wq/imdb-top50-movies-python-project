import sys
from datetime import date

import pandas as pd

BASE="https://datasets.imdbws.com/"

year=int(sys.argv[1]) if len(sys.argv) > 1 else date.today().year

print("Downloading data first run takes a little time....")
basics=pd.read_csv(
    BASE+"title.basics.tsv.gz",sep="\t",na_values="\\N",
    usecols=["tconst","titleType","primaryTitle","startYear"],
    dtype=str,
)
ratings=pd.read_csv(BASE + "title.ratings.tsv.gz",sep="\t",na_values="\\N")

movies=basics[(basics["titleType"]=="movie") & (basics["startYear"]==str(year))]
df=movies.merge(ratings,on="tconst")
top=df.sort_values("numVotes",ascending=False).head(50)

print("\n")
print(f"Top 50 movies of the {year} by votes are \n")
for i,row in enumerate(top.itertuples(),start=1):
    print(f"{i}.{row.primaryTitle} (rating {row.averageRating},row.{row.numVotes} votes)")

top.to_csv(f"top50_{year}.csv",index=False)
print("\n")
print(f"Saved to top50_{year}.csv")