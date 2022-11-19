# this programm is a simple travel log app

travel_log : list = [
    {
        "country" : "France",
        "visits"  : 12,
        "cities"  : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits"  : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(travel_log : list, country : str, visits : int, cities : list) -> None:
    travel_log.append({"country" : country, "visits" : visits, "cities" : cities})

print("Welcome to the travel log :D")
add_new_country(travel_log, "Czechia", 10000000000000000000000000000000000000, ["Brno", "Prague", "Telč", "Letovice", "Svitavy", "Znojmo"])
print(travel_log)
