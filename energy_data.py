import tweepy
import urllib.request
from local_settings import *

def post_tweet():
    

if __name__ == '__main__':
    data = urllib.request.urlopen(DATA_URL).read().decode("utf-8")

    # Determine locations of the power data of interest
    turbine_index = data.index(TURBINE_DATA) + len(TURBINE_DATA)
    # Extract power output by starting at the index of the lastvalue parameter, adding 1 to chop off the quote,
    # and adding the length of the output number to the index. Results in the number between quotes in lastvalue.
    turbine_output = data[turbine_index + 1: turbine_index + 1 + data[turbine_index + 1:].index('\"')]

    charlton_index = data.index(CHARLTON_DATA) + len(CHARLTON_DATA)
    charlton_output = data[charlton_index + 1: charlton_index + 1 + data[charlton_index + 1:].index('\"')]

    elmsub_index = data.index(ELMSUB_DATA) + len(ELMSUB_DATA)
    elmsub_output = data[elmsub_index + 1: elmsub_index + 1 + data[elmsub_index + 1:].index('\"')]

    westwindsor_index = data.index(WESTWINDSOR_DATA) + len(WESTWINDSOR_DATA)
    westwindsor_output = data[westwindsor_index + 1: westwindsor_index + 1 + data[westwindsor_index + 1:].index('\"')]

    post_tweet()

