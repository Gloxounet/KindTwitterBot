from bs4 import BeautifulSoup
import requests
import random

seen_disquette = []

def get_disquette():
    alea = random.randint(1,1000)
    page    = requests.get(f"http://www.jokes4us.com/pickuplines/random/pickupline{alea}.html")
    soup = BeautifulSoup(page.text,'html.parser')
    return soup.find_all("font", size="5")[0].string.extract()

def get_unique_disquette():
    disk = get_disquette()
    while (disk in seen_disquette) or ("(" in disk) or ("girl" in disk) or ("boy" in disk) or ("girl" in disk)  :
        disk = get_disquette()
    
    seen_disquette.append(disk)
    return disk


if __name__ == "__main__" :
    print(get_unique_disquette())
