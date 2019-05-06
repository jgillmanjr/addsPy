addsPy
======

This is just a little client library I've been poking at to get data from the Aviation Digital Data Service [(ADDS)](https://www.aviationweather.gov/adds)
[text data server](https://aviationweather.gov/dataserver).

## Supported Endpoints
Currently, the library only supports METARs and Aircraft/Pilot Reports.

The current data source map is as so:

* METARS: `metar`
* Aircraft / Pilot Reports: `aircraftreports`

## Usage

Here's an example to get the METARs for the last hour from KOZW:

```python
from addsPy import Client

req_params = {
    'stationString': 'kozw',
    'hoursBeforeNow': 1
}

ozw_wx = Client(datasource='metar', **req_params)
ozw_wx.request()
```

From there, you get the raw return as specified by the docs. For example, [here](https://aviationweather.gov/dataserver/output?datatype=metar) is the docs regarding
output for METARS. Basically, this gets stuffed into the `wxdata` property.

So for example, if you wanted to iterate through the text of the METARs:

```python
for metar in ozw_wx.wxdata['data']['METAR']:
    print('{station}: {raw}'.format(station=metar['station_id'], raw=metar['raw_text']))
```