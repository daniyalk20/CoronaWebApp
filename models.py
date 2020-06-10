import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests


def growthVisualizer(url):
    df = pd.read_csv(url)

    def dataHead(self):
        return df.head(10)

    def plot(self, label):
        plt.style.use('seaborn-bright')
        plt.plot(cases['ObservationDate'], cases['Confirmed'], 'y')
        plt.plot(cases['ObservationDate'], cases['Deaths'], 'r')
        plt.plot(cases['ObservationDate'], cases['Recovered'], 'g')
        plt.plot(cases['ObservationDate'], cases['Active'], 'c')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
        plt.gcf().autofmt_xdate()
        plt.title(label=label)
        plt.ylabel('Cases')
        plt.xlabel('Dates')
        return plt

    country = df['Country_Region'].unique()
    cases = df.groupby('ObservationDate')
    result = []
    for k, v in df.groupby('ObservationDate'):
        result.append([k, sum(v['Confirmed']), sum(v['Deaths']),
                       sum(v['Recovered']), sum(v['Active'])])
    cases = pd.DataFrame(result, columns=['ObservationDate',
                                          'Confirmed',
                                          'Deaths', 'Recovered', 'Active'])



def getResponse():
    # URL of the api where we want to extract data from
    url = "https://covid-193.p.rapidapi.com/statistics"

    # including secret keys into header of the request
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "d977ce9798msh4e5fe441381dc13p1addf4jsn5ad3eadb6644"
    }

    response = requests.request("GET", url, headers=headers)
    # return received response in json format
    return response.json()['response']


def extractData(data):
    """ Column Names whihc we got in response from the api.
                'continent',
               'country',
               'population',
               'new_cases', 'active_cases', 'critical_cases', 'recovered_cases', '1M_po_cases', 'total_cases',
               'new_deaths', '1M_pop_deaths', 'total_deaths',
               '1M_pop_tests', 'total_tests',
               'day',
               'time']"""
    # Creating empty lists for each column
    continents = []
    country = []
    population = []
    new_cases = []
    active_cases = []
    critical_cases = []
    recovered_cases = []
    M1_pop_cases = []
    total_cases = []
    new_deaths = []
    M1_pop_deaths = []
    total_deaths = []
    M1_pop_tests = []
    total_tests = []
    day = []
    time = []

    # filling the data into each column separately
    for i in range(len(data)):
        continents.append(data[i]['continent'])
        country.append(data[i]['country'])
        population.append(data[i]['population'])
        new_cases.append(data[i]['cases']['new'])
        active_cases.append(data[i]['cases']['active'])
        critical_cases.append(data[i]['cases']['critical'])
        recovered_cases.append(data[i]['cases']['recovered'])
        M1_pop_cases.append(data[i]['cases']['1M_pop'])
        total_cases.append(data[i]['cases']['total'])
        new_deaths.append(data[i]['deaths']['new'])
        M1_pop_deaths.append(data[i]['deaths']['1M_pop'])
        total_deaths.append(data[i]['deaths']['total'])
        M1_pop_tests.append(data[i]['tests']['1M_pop'])
        total_tests.append(data[i]['tests']['total'])
        day.append(data[i]['day'])
        time.append(data[i]['time'])
    # creating a dictionary of all columns in which keys are the columns and values are the rows
    data_frame = {'continents': continents, 'country': country, 'population': population, 'new_cases': new_cases,
                  'active_cases': active_cases, 'critical_cases': critical_cases, 'recovered_cases': recovered_cases,
                  '1M_pop_cases': M1_pop_cases, 'total_cases': total_cases, 'new_deaths': new_deaths,
                  '1M_pop_deaths': M1_pop_deaths,
                  'total_deaths': total_deaths, '1M_pop_tests': M1_pop_tests, 'total_tests': total_tests, 'day': day,
                  'time': time}
    # converting the data_frame dictionary into pandas data-frame
    df = pd.DataFrame(data_frame)
    # return the data-frame
    return df

