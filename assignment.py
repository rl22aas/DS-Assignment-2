#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 02:15:03 2023

@author: Rimsha
"""

import pandas as pd
import matplotlib.pyplot as plt


def get_data(path):
    """
    Parameters
    ----------
    path : String
        contains the uri of data file.
    Returns
    -------
    df : DataFrame
        Panda DataFrame object containing original data.
    country_df : DataFrame
        Panda DataFrame object having countries as columns.

    """
    df = pd.read_csv(path)
    df= df.set_index("Country Name")
    df = df.dropna()
    t_df = df.copy()
    t_df = t_df.drop(
        ['Indicator Name', 'Indicator Code', 'Country Code'], axis=1)

    t_df = t_df.T
    country_df = t_df.dropna()

    return df, country_df
    

def line_plot(df, title, xlabel, ylabel):
    """
    Parameters
    ----------
    df : DataFrame
        DataFrame having data to plot line graph (time series plot).
    title : String
        Title of the graph.
    xlabel : String
        label for x-axis.
    ylabel : String
        lable for y-axis.

    Returns
    -------
    None.

    """
    countries = ['Australia', 'Bhutan', 'Switzerland', 'Spain', 'Japan',
                 'Singapore']
    countries_df = df[countries]
    plt.figure(figsize=(8,6))
    plt.title(title)
    plt.plot(countries_df)
    plt.xlabel(xlabel)
    plt.xticks(rotation=90)
    plt.ylabel(ylabel)
    plt.legend(countries, bbox_to_anchor=(1.0, 1), loc="upper right")
    plt.show()
    
    
def create_bar_plot(data, title, xlabel, ylabel):
    """
    Parameters
    ----------
    data : DataFrame
        Having data for the bar plot.
    title : String
        Title of the plot.
    xlabel : String
        label for x-axis.
    ylabel : String
        lable for y-axis.
    Returns
    -------
    None.

    """
    countries =  ['Australia', 'Bhutan', 'Switzerland', 'Spain', 'Japan',]
    data = data.iloc[-10:]
    data = data[countries]
    print(data)
    # last_years_data = last_years_data.T
    plt.figure(figsize=(8,6))
    ax = data.plot(kind='bar')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    plt.xticks(rotation=0)
    ax.set_ylabel(ylabel)
    plt.legend(countries, bbox_to_anchor=(1.0, 1), fontsize="7",
               loc="upper right")
    plt.show()

    

data_paths = {
    "debt": "/Volumes/Untitled 2/ds_assignments/assignment_2/" + 
        "rimsha/data_sets/DebtData.csv",
    "population": "/Volumes/Untitled 2/ds_assignments/assignment_2/" + 
        "rimsha/data_sets/PopulationData.csv",
    "methane": "/Volumes/Untitled 2/ds_assignments/assignment_2/" + 
        "rimsha/data_sets/Methane.csv",
    "rural": "/Volumes/Untitled 2/ds_assignments/assignment_2/" + 
        "rimsha/data_sets/RuralPopulation.csv",
    }

debt, debt_country = get_data(data_paths["debt"])
population, population_country = get_data(data_paths['population'])

line_plot(debt_country.iloc[-20:], "Central government debt, total (% of GDP)",
          "Year", "Debt (% of GDP)")
line_plot(population_country.iloc[-20:], "Population growth (annual %)",
          "Year", "Population growth")

methane_data, methane_data_country =  get_data(data_paths["methane"])
rural_population, rural_population = get_data(data_paths['rural'])

create_bar_plot(methane_data_country, 
                "Agricultural Methane Emissions (% of total)", "Year", 
                "Agricultural Methane Emissions")

create_bar_plot(rural_population, "Rural Population", 
         "Year", "Rural Population")
















