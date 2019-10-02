import pandas as pd, requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)


def car_guru():
    url = """https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?
        sourceContext=carGurusHomePageModel&newSearchFromOverviewPage=true&inventorySearchWidgetType=AUTO&
        entitySelectingHelper.selectedEntity=c23116&entitySelectingHelper.selectedEntity2=c24168&zip=94709&
        distance=50&searchChanged=true&sellerTypes=Private&newUsed=2&modelChanged=false&filtersModified=true"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all("div", {"class": "cg-dealFinder-result-wrap clearfix"})
    return results[0].text


@app.route('/')
def hello_world():

    return car_guru()


if __name__ == '__main__':
    app.run()
