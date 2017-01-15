import requests
import bs4
import pandas as pd
import re


def load_data(path_string):
    """Loads up the spreadsheet we want to populate.

    The spreadsheet has the following structure:

    """
    loaded_data = pd.read_table(path_string)

    return loaded_data 

def get_destinations(pd_Dataframe):
    """Extracts the urls from the loaded data.

    Only use the ones corresponding to unresearched trips.
    i.e. ones without data in them.
    """
    # The name of our column of interest.
    header = "Link"

    # Set up criterion for "unresearched" trips to be
    # wherever the test_column_header is still empty,
    # NaN or "null" in a pandas dataframe.
    test_column_header = "Countries"
    criterion = pd_Dataframe[test_column_header].isnull()
    
    # Filter by criterion
    url_Dataframe = pd_Dataframe[[header, "Tour Name"]][criterion & pd_Dataframe["Link"].notnull()]
    
    # Prep output as list
    urls = [row for row in url_Dataframe.itertuples()]

    return urls

def fetch_metadata(string_or_list_of_urls):
    """Fetches the required trip metadata based on urls from loaded data.
    """
    url_list = _process_string_or_list(string_or_list_of_urls)
    trip_metadata = {}
    money = re.compile("\d+")

    for index, url, tour_name in url_list:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        # country = soup.select("div#main > ol > li:nth-of-type(3) > a > span")[0].string
        # NOT valid. You need to read around to figure out all the countries this tour is in.

        number_nights = soup.select("table#detail-table > tr:nth-of-type(3) > td")[0].string[0]
        diff_level = soup.select("table#detail-table > tr:nth-of-type(2) > td")[0].string
        mileage_avg = soup.select("table#detail-table > tr:nth-of-type(4) > td")[0].string[0:2] 
        #cost = money.search(
        #        str(soup.select("table#detail-table > tr:nth-of-type(6) > td")[0].string)).group(0)

        trip_metadata[index] = { "Link": url,
                "Tour Name": tour_name,
                "Countries": None,
                "Mileage Min": None,
                "Mileage Max": None,
                "Surface": None,
                "Number of Nights": number_nights,
                "Difficulty Level": diff_level,
                "Mileage Average": mileage_avg,
                "Number of loops": None,
                "Cites/Towns vs. Villages": None,
                "Attractions": None,
                "Gold Star": None,
                "Cost": None,
                "Flag": None
                }

    return trip_metadata

def update_data(metadata_dict, pd_Dataframe, path_string):
    """Writes the newly scraped trip metadata to file.
    """
    for index, trip_details in metadata_dict.items():
        pd_Dataframe.iloc[index] = trip_details

    pd_Dataframe.to_csv("{}.new.tsv".format(path_string), sep="\t")

    status = "{} updated!".format(path_string)
    print(status)
    return status

# Helpers

def _process_string_or_list(string_or_list):
    """Tests input to confirm whether it is a Python str or list, coerces to list.
    """

    if type(string_or_list) == list:
        items_as_list = string_or_list 
    elif type(string_or_list) == str:
        items_as_list = [string_or_list] 
    else:
        raise RuntimeError("The argument passed to fetch_metadata must be a string or list. Check get_destinations and load_data functions for bugs.")

    return items_as_list

PATH_TO_DATA = "honeymoondb.tsv"
LOADED_DATAFRAME = load_data(PATH_TO_DATA)

if __name__ == "__main__":
    trip_metadata = fetch_metadata(get_destinations(LOADED_DATAFRAME))
    update_data(trip_metadata, LOADED_DATAFRAME, PATH_TO_DATA)


