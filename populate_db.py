import requests
import random
from datetime import date, timedelta
import time

BASE_URL = "http://localhost:8000"

def wait_for_api():
    for i in range(30):
        try:
            response = requests.get(f"{BASE_URL}/")
            if response.status_code == 200:
                print("API is ready!")
                return True
        except:
            pass
        print(f"Waiting for API... ({i+1}/30)")
        time.sleep(1)
    return False

def create_tournament(tournament_data):
    try:
        response = requests.post(f"{BASE_URL}/tournaments/", json=tournament_data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error creating tournament: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

def create_participation(participation_data):
    try:
        response = requests.post(f"{BASE_URL}/participations/", json=participation_data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error creating participation: {response.status_code}")
            return None
    except:
        return None

def create_player(player_data):
    try:
        response = requests.post(f"{BASE_URL}/players/", json=player_data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error creating player: {response.status_code}")
            return None
    except:
        return None

def main():
    print("Starting database population...")
    
    if not wait_for_api():
        print("API is not responding. Exiting.")
        return
    
    cities = ["Moscow", "St. Petersburg", "Kazan", "Sochi", "Yekaterinburg"]
    countries = ["Russia", "USA", "Germany", "France", "China"]
    tournament_names = ["Open", "Championship", "Grand Prix", "Masters", "Classic"]
    player_surnames = ["Ivanov", "Petrov", "Sidorov", "Smirnov", "Kuznetsov"]
    titles = ["GM", "IM", "FM", "NM"]
    
    tournaments = []
    print("\nCreating tournaments...")
    
    for i in range(30): 
        tournament = {
            "date": str(date(2024, 1, 1) + timedelta(days=i*7)),
            "city": random.choice(cities),
            "country": random.choice(countries),
            "t_name": f"{random.choice(tournament_names)} {i+1}",
            "qualification_level": random.randint(1, 10),
            "additional_info": {
                "prize_fund": random.randint(1000, 100000),
                "organizer": f"Organization {i+1}",
                "time_control": random.choice(["blitz", "rapid", "classical"]),
                "rounds": random.randint(5, 11)
            }
        }
        
        created = create_tournament(tournament)
        if created:
            tournaments.append(created)
            print(f"✓ Tournament {i+1} created")
        else:
            print(f"✗ Failed to create tournament {i+1}")
    
    print("\nCreating participations and players...")
    player_id = 1
    
    for tournament in tournaments:
        num_participations = random.randint(5, 8)
        
        for place in range(1, num_participations + 1):
            participation = {
                "tur_id": tournament["tur_id"],
                "start_number": place,
                "zanyatoye_mesto": place  
            }
            
            created_participation = create_participation(participation)
            
            if created_participation:
                player = {
                    "par_id": created_participation["part_id"],
                    "second_name": f"{random.choice(player_surnames)}",
                    "country": random.choice(countries),
                    "titul": random.choice(titles),
                    "rating": random.randint(1500, 2800)
                }
                
                created_player = create_player(player)
                if created_player:
                    print(f"✓ Player {player_id} created for tournament {tournament['tur_id']}")
                    player_id += 1
    
    print(f"\nPopulation complete!")
    print(f"Created: {len(tournaments)} tournaments")
    print(f"Created: approximately {player_id-1} players")
    print(f"\nYou can now test the API at:")
    print(f"  - http://localhost:8000/")
    print(f"  - http://localhost:8000/docs")

if __name__ == "__main__":
    main()
