import csv
from dtos.EntryResponseDto import EntryResponseDto

"""
    TBC: 
        - Explore a more streamline way to map rows to DTO fields
        - Update to use pandas for csv import
        - Fix encoding issue of artistName & songName
"""

SONG_DATA_CSV_PATH = "data/song_data.csv"

# reads song data CSV file and returns a list of entries from table mapped to eurovision entry objects
def get_all_entries():

    entries =  []

    try:
        with open(SONG_DATA_CSV_PATH, mode="r", encoding="Windows-1252") as file:

            reader = csv.DictReader(file)

            for row in reader:
                entry = EntryResponseDto(
                    year=int(row["year"]),
                    country=row["country"],
                    artistName=row["artist_name"], # encoding issue for some - eg., Marko Kon\u00a0and\u00a0Milaan
                    songName=row["song_name"], # encoding issue for some - eg., \u00c9videmment
                    runningOrder=int(row["final_draw_position"]) if row["final_draw_position"].isdigit() else None,
                    points=int(row["final_total_points"]) if row["final_total_points"].isdigit() else None,
                    place=int(row["final_place"]) if row["final_place"].isdigit() else None
                )
                entries.append(entry)

            # 565 objects in list - all entries are mapped correctly
            # print(len(entries))

    except FileNotFoundError:
        print(f"Error: File {SONG_DATA_CSV_PATH} not found.")

    return entries

def get_entries_by_year(year):
    # gets eurovision entries for a given year - returns as json serialisable data
    all_entries = get_all_entries()
    return [entry.to_json() for entry in all_entries if entry.year == year]
