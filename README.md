# Eurovision Data API 🪩🕺🏼

Python Flask APIs that retrieve Eurovision Song Contest entries (2009-2023) from a CSV [Kaggle dataset](https://www.kaggle.com/datasets/diamondsnake/eurovision-song-contest-data). Created to support my data science project exploring how the running order of performances in the final can influence final places and scores.

### Endpoints

- `/entries` → returns a list of all ESC entries from the dataset - including  artist, country, song name, year, running order, place, and points in the final. Countries that didn't qualify for the final will have `null` values for running order, place, and points.
- `/entries?year=2022` → returns a list of ESC entries filtered for any year (2009-2023) provided in the query parameter.

**DTO structure of ESC entry:** 

```  
{
  "artistName": "Monika Liu",
  "country": "Lithuania",
  "place": 14,
  "points": 128,
  "runningOrder": 14,
  "songName": "Sentimentai",
  "year": 2022
}
```

### Use Case

Designed to feed structured data into a Jupyter notebook for exploratory data analysis, statistical investigation of the relationship between running order and final score/points as well as performance outcome predictions from the entry's running order.