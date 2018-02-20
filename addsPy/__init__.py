"""
General Client for Working with the ADDS Data

Builds a dictionary for easy working based on expected returns

http://aviationweather.gov/dataserver
"""
import requests
import untangle
import addsPy.endpoints

BASEURI = 'http://aviationweather.gov/adds/dataserver_current/httpparam'

ENDPOINTS = {
    'metar': {
        'dataSource': 'metars',
        'mapdef': endpoints.metar
    }
}


class AddsDict(dict):
    def __str__(self):
        return str(self.cdata)

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.cdata = None


class Client:
    def __init__(self, datasource, **kwargs):
        self.datasource = ENDPOINTS[datasource]['dataSource']  # This will feed the dataSource parameter
        self.map = ENDPOINTS[datasource]['mapdef']  # The mapping to be applied
        self._wxobj = None
        self.wxdata = {}
        self.request_params = {
            'dataSource': self.datasource,
            'requestType': 'retrieve',
            'format': 'xml'
        }

        for k, v in kwargs.items():
            self.request_params[k] = v

    def _process_element(self, start_location, definition):
        """
        This processes a particular element
        """
        sendback = None  # Placeholder for visibility

        # Break out the defintion values
        location = definition['location']
        cdata_type = definition['cdata_type']
        attributes = definition['attributes']
        multi_occurs = definition['multi_occurs']
        children = definition['children']

        # Cut slingload if there's nothing to work on
        if getattr(start_location, location, None) is None:
            if multi_occurs:
                return []
            return AddsDict()

        if multi_occurs:
            workingobj = getattr(start_location, location, None)
            sendback = []
        else:
            workingobj = [getattr(start_location, location, None)]

        for o in workingobj:
            wd = AddsDict()

            if cdata_type is not None:
                wd.cdata = cdata_type(o.cdata)

            for a in attributes:
                wd[a] = o[a]

            for k, v in children.items():
                wd[k] = self._process_element(start_location=o, definition=v)

            if multi_occurs:
                sendback.append(wd)
            else:
                sendback = wd

        if len(sendback) == 0:
            return sendback.cdata
        return sendback

    def request(self):
        r = requests.get(
            url=BASEURI,
            params=self.request_params,
        )

        self._wxobj = untangle.parse(r.text).response

        for k, v in self.map.items():
            self.wxdata[k] = self._process_element(start_location=self._wxobj, definition=v)
