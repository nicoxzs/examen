import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "GEr9txFf2jpG0CFqL0QjCuAO12DYaQkj"  # Reemplaza con tu clave de MapQuest

while True:
    orig = input("Ubicacion Inicial: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Kilometers:      " + str(round(json_data["route"]["distance"] * 1.61, 1)))
        print("Trip Duration:   " + json_data["route"]["formattedTime"])
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + str(round(each["distance"] * 1.61, 1)) + " km)")
        print("=============================================\n")