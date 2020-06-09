import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests


def getResponse():
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "d977ce9798msh4e5fe441381dc13p1addf4jsn5ad3eadb6644"
    }

    response = requests.request("GET", url, headers=headers)
    return getResponse().json()['response']

data = getResponse()
print(data)