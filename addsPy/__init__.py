"""
General Client for Working with the ADDS Data

Builds a dictionary for easy working based on expected returns

http://aviationweather.gov/dataserver
"""
import requests
import untangle
import addsPy.endpoints

BASEURI = 'https://aviationweather.gov/adds/dataserver_current/httpparam'

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
        self._robj = None
        self._wxobj = None
        self.wxdata = {}
        self.required_params = {
            'dataSource': self.datasource,
            'requestType': 'retrieve',
            'format': 'xml'
        }
        self.request_params = {}

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
        attributes = definition['attributes'] if definition['attributes'] is not None else []
        multi_occurs = definition['multi_occurs']
        children = definition['children'] if definition['children'] is not None else {}

        # Cut slingload if there's nothing to work on
        if getattr(start_location, location, None) is None:
            if multi_occurs:
                return None  # []
            return None  # AddsDict()

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
                attr, typr = a
                if o[attr] is not None:
                    wd[attr] = typr(o[attr])

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
        self._robj = requests.get(
            url=BASEURI,
            params={**self.required_params, **self.request_params},
        )

        self._wxobj = untangle.parse(self._robj.text).response

        for k, v in self.map.items():
            self.wxdata[k] = self._process_element(start_location=self._wxobj, definition=v)
