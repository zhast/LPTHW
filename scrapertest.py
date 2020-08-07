import requests

url = "https://www.msc.com/Site/WebServices/RouteFinder.svc/VSAgreements"

# request the URL and parse the JSON
response = requests.get(url)
response.raise_for_status() # raise exception if invalid response

values = response.json()[0].VoyageNumber

