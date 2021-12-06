import requests
import datetime
import random
# Gets a random quote out of a collection of quotes
# (this is only for demonstration)
url = 'https://type.fit/api/quotes'
headers = {"Accept": "application/json"}
response = requests.get(url,headers=headers)
rnd = random.randint(0, len(response.json())-1)
quote = response.json()[rnd]["text"]
author = response.json()[rnd]["author"]
print(f"\nQuote of the day:\n{quote} ({author})\n")

# ---------------------STEP 2-------------------------------------
# Volumes test
VOLUME_PATH = "/storage"
STORAGE = "store.txt"
TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
# save scope table
with open(f"{VOLUME_PATH}/{STORAGE}", "a") as store:
    store.write(f"{TIMESTAMP}\t{quote} ({author})\n")
    store.close()
# Print whats already in volume storage
with open(f"{VOLUME_PATH}/{STORAGE}", "r") as store:
        print("All collected quotes:")
        print(store.read())
        store.close()