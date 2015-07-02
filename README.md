# WalkScore Python API binding
No official Python bindings on Pypi and GitHub, we decided to write a lightweight stand-alone module to keep our code base clean.

# How to install?
It is available on pip and GitHub,

```
pip install walkscore-api-binding
```

or
```
git clone git@github.com:knockrentals/walkscore.git
python setup.py install
```

# Features:
- Auto escape address
- Inject Etag to enable caching
- JSON support (XML support will come when there is a need)
- Proper error handling
- Test coverage (more will come in the upcoming releases)

# Dependencies
- simplejson/json
- urllib
- urllib2
- nose (only if you need to run test)

### Example code:
See https://github.com/knockrentals/walkscore/blob/master/example/example.py

### Example output:
```
{
   "status":1,
   "updated":"2014-03-25 22:05:09.233650   ",
   "description": "Walker's Paradise",
   "walkscore": 95,
   "more_info_icon":"http://cdn.walk.sc/images/api-more-info.gif",
   "snapped_lat":47.6085,
   "snapped_lon":-122.3295,
   "more_info_link":"http://www.walkscore.com/how-it-works.shtml",
   "logo_url":"http://cdn.walk.sc/images/api-logo.gif",
   "ws_link":"http://www.walkscore.com/score/1119%208th%20Avenue%20Seattle%20WA%2098101/lat=47.6085/lng=-122.3295"
}
```

### Exceptions:
```InvalidApiKeyException``` is thrown when api key is invalid

```InvalidLatLongException``` is thrown when lat and/or longitude are invalid or empty

```ExceedQuotaException``` is thrown when api key exceeds daily quota

```ScoreUnavailableException``` is thrown when a walk score is unavailable

```InternalServerException``` is thrown when internal server error occurs


### Note:
- API key can be requested from http://www.walkscore.com/professional/api-sign-up.php
- Address (incomplete address may yield unpleasant result), latitude and longitude are required
- API Key is rate limited (see plans for details)

### Found issues? Feature requests?
Sure, please send them to: https://github.com/knockrentals/walkscore/issues

### More details:
See http://www.walkscore.com/professional/api.php
