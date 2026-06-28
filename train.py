def string_train():
    string = "Hello World!, This is Train.py"

    lower_string = string.lower()
    print(lower_string)

    upper_string = string.upper()
    print(upper_string)

    strip_text = "   HEllo    !  "
    stripped_text = strip_text.strip()
    print(stripped_text) 

    replaced_text = string.replace("Hello","Bye")
    print(replaced_text)

    split_text = string.split(" ")
    print(split_text)

    string_v2 = "Nice to meet You!"

    print(" ".join(split_text))

    print(string_v2.find("Mice"))

    print(string_v2.upper().startswith(string_v2[:4].upper()))

    print(string_v2.endswith("You!"))

    string_v3 = "Hey, This is a PS5 Pro!"
    print(string_v3.count("P"))

    if "PS5" in string_v3:
        print("GTA6")
    else:
        print("No luck!")
    
    console = "PS5"
    game = "Resident Evil Requiem"

    string_v4 = f"Hey, I have {console}, and we can play {game} together!"

    print(string_v4)
    
def list_train():
    AAA_Games = ["God of War","Red Dead Redemption 2","RE9","GTA6"]
    for i in AAA_Games:
        print(f"{i},", end = " ")
    print()
    print(AAA_Games[0:2])
    
    AAA_Games[1] = "Sekiro Shadows Die Twice"
    
    print(AAA_Games[::-1])
    
    AAA_Games.append("Detroit Human")
    AAA_Games_v2 = ["RE4 Remake","Forza Horizon 6","Marvel's Spiderman"]
    AAA_Games.extend(AAA_Games_v2)
    
    for i in AAA_Games:
        print(f"{i}," ,end = " ")
    print()
    
    for i in AAA_Games_v2:
        print(f"{i}," ,end = " ")
    print()
    AAA_Games_v2.insert(0,"MineCraft")
    print(AAA_Games_v2)
    for i in AAA_Games_v2:
        try:
            AAA_Games.remove(i)
        except Exception as e:
            print("Pass")
    print(AAA_Games)
    AAA_Games.pop()
    
    AAA_Games.sort()
    
    AAA_Games.reverse()
    print(AAA_Games)
    
    AAA_Games_v3 = AAA_Games.copy()
    AAA_Games_v3.extend(AAA_Games_v2)
    AAA_Games_v3.sort()
    AAA_Games_v3.reverse()
    print(AAA_Games_v3)
    
    
    squares = []
    
    for i in range(1,10):
        squares.append(i*i)
    print(squares)
    
    cubes = [i*i*i for i in range(1,11)]
    print(cubes)
    
def dictionary_train():
    players = {
        "Spain":["Pedri","Yamal","Gavi"],
        "France":["Mbappe","Dembelle"],
        "Norway" :["Haaland","Asgard"],
        "Brazil":["Neymar","Vinci Jnr"]
    }
    
    print(players["France"])
    
    players["Spain"][2] = "Rodri"
    
    print(players["Spain"])
    
    players["Argentina"] = ["Messi","Martinez"]
    print(players.get("Portugal","Not found"))
    
    print(players.keys())
    print(players.values())

        
    players.update({
        "Spain":["Yamal","Gavi"],
        "Portugal":["Ronaldo","Bruno"]
    })
    
    print(players.items())
    
    players.pop("Argentina")
    print(players)
    
    players_v2 = {
        "Spain":{
            "Forward": "Yamal",
            "Mid-Fielder":"Gavi",
            "Defender": "Torres"
        },
        "France":{
            "Forward":["Mbappe","Dembelle"]
        }
    }
    print(players_v2["France"]["Forward"])
    
def tuples_set_train():
    players = ("Yamal","Mbappe","Ronaldo","Messi")
    print(players)
    
    Spain , France , Portugal , Argentina = players
    print(Argentina)
    
    players_set = {"Haaland","Messi","Ronaldo","Ronaldo","Messi","Haaland"}
    print(players_set)
    players_set.add("Mbappe")
    players_set.remove("Messi")
    players_set.discard("Neymar")
    players_set.discard("Ronaldo")
    
    FCB = {"Yamal","Robert"}
    RMA = {"Mbappe","Vini Jnr"}
    
    print(FCB | RMA)
    print(FCB & RMA)
    print(RMA - FCB)
if __name__ == "__main__":
    tuples_set_train()