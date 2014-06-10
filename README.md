# Simple Python API wrapper for WalkScore.com
Quick seach on pypi and GitHub show no official python bindings. To keep our code clean, we decide to implement this simple, light-weight binding
as a standalone module.

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
   "ws_link":"http://www.walkscore.com/score/1119%208th%20Avenue%20Seattle%20WA%2098101/lat=47.6085/lng=-122.3295/?utm_source=zipdigs.com&utm_medium=ws_api&utm_campaign=ws_api"
}
```

### Exceptions:
```InvalidApiKeyException``` is thrown when api key is invalid

```InvalidLatLongException``` is thrown when lat and/or longitude are invalid or empty

### Note:
- API key can be requested from http://www.walkscore.com/professional/api-sign-up.php
- Lat & Long are required
- Key is rate limited (see plans for details)

### More details:
See http://www.walkscore.com/professional/api.php
