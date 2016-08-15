from walkscore.api import WalkScore

def main():
    apiKey='yourapikey'
    walkscore = WalkScore(apiKey)

    address='1119 8th Avenue Seattle WA 98101'
    lat=47.6085
    lon=-122.3295
    print(walkscore.makeRequest(address, lat, lon))

if __name__ == '__main__':
    main()
