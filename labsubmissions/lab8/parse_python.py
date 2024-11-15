import json

with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'a') as csv_file:

    for r in data[:5]:
        name = r['name']
        html_url = r['html_url']
        updated_at = r['updated_at']
        visibility = r['visibility']
        
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(line)
