from walkscore.api import TransitScore

def main():
    apiKey='yourapikey'
    transitscore = TransitScore(apiKey)

    # reference https://www.walkscore.com/professional/public-transit-api.php
    params = {
        'lat': '47.6101359',
        'lon': '-122.3420567',
        'city': 'Seattle',
        'state': 'WA'
    }

    print transitscore.makeRequest('score', params)

    network_parmas = {
        'lat': '47.6101359',
        'lon': '-122.3420567'
    }

    print transitscore.makeRequest('network_search', network_parmas)

if __name__ == '__main__':
    main()
