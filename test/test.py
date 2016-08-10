from walkscore.api import *
from nose.tools import *

# Enter a valid key here
apiKey='yourapikey'
if apiKey=='yourapikey':
   raise InvalidApiKeyException("Please change the apiKey in `test/test.py` before running `python setup.py test`") 


@raises(InvalidApiKeyException)
def test_invalidapi():
    badapiKey='badkey'
    walkscore = WalkScore(badapiKey)

    address='somewhere'
    lat = '47.6085'
    lng= '-122.3295'
    walkscore.makeRequest(address, lat, lng)
    
def test_valid_walskcore_call():
    
    walkscore = WalkScore(apiKey)

    address='1119 8th Avenue Seattle WA 98101'
    lat=47.6085
    lon=-122.3295
    jsonResp = walkscore.makeRequest(address, lat, lon)
    assert(jsonResp['status'] == 1)
    print(jsonResp)
    assert(jsonResp['walkscore'] == 97)

    
def test_valid_transitscore_call():

    transitscore = TransitScore(apiKey)

    # reference https://www.walkscore.com/professional/public-transit-api.php
    params = {
        'lat': '47.6101359',
        'lon': '-122.3420567',
        'city': 'Seattle',
        'state': 'WA',
    }

    jsonResp = transitscore.makeRequest('score', params)
    print(jsonResp)
    assert(jsonResp['transit_score'] == 100)