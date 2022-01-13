
import json

with open("tokenIDs.json") as inputFile:
    
    data = json.load(inputFile)
    
    updates = []
    for tokenid in data:
        updates.append({
            "mint_account": tokenid,
            "new_uri": "https://raw.githubusercontent.com/loopcreativeandy/assets/main/metadata.json"
        })
    
    with open("updates.json", "w") as outfile:
        json.dump(updates, outfile)
