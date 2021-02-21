import json
import discord.client as Client
def save_list_to_path(id_list, path):
    with open(path,"w") as file:
        json.dump(id_list,file)

def get_list_from_path(path):
    try:    
        with open(path,"r") as path:
            return json.load(path)
    except FileNotFoundError:
        return []