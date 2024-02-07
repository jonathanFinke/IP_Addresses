import csv
import geoip2.database
import pandas as pd

# This file queries an MMDB database for IP mapping for heatmap analysis at the regional level for a given country

# Load GeoLite2 database
reader = geoip2.database.Reader('insert your path to .mmdb file here')

# Load your IP addresses file into a pandas DataFrame
ip_data = pd.read_csv('insert your csv list of IPs here')

# Define a function to retrieve location information
def get_location(ip):
    try:
        response = reader.city(ip)
        country = response.country.name
        state = response.subdivisions.most_specific.name
        city = response.city.name
    except Exception as e:
        country, state, city = 'Unknown', 'Unknown', 'Unknown'
    return pd.Series([country, state, city])

# Apply the function to the DataFrame
ip_data[['Country', 'State', 'City']] = ip_data['IP'].apply(get_location)

# Save the results to a new CSV file
ip_data.to_csv('ip_locations.csv', index=False)

# Close the GeoIP2 reader
reader.close()