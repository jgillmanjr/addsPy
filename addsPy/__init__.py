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
    'metars': {
        'dataSource': 'metars',
        'mapdef': endpoints.metars
    },
    'aircraftreports': {
        'dataSource': 'aircraftreports',
        'mapdef': endpoints.pireps
    },
    'tafs': {
        'dataSource': 'tafs',
        'mapdef': endpoints.tafs
    },
    'airsigmets': {
        'dataSource': 'airsigmets',
        'mapdef': endpoints.airsigmets
    },
    'stations': {
        'dataSource': 'stations',
        'mapdef': endpoints.stations
    },
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
        has_empty_children = definition['has_empty_children'] if 'has_empty_children' in definition else False  # Station types use this. Rare.

        # Cut slingload if there's nothing to work on
        current_element = getattr(start_location, location, None)

        if current_element is None:
            if multi_occurs:
                return []
            if attributes == [] and children == {}:  # Basically just expecting cdata and nothing else
                return None
            return AddsDict()

        if has_empty_children:
            sendback = []
            for k, v in children.items():
                print(k)
                if self._process_element(start_location=current_element, definition=v):
                    sendback.append(k)
            return sendback

        if multi_occurs:
            if type(current_element) is list:
                workingobj = current_element
            else:
                workingobj = [current_element]
            sendback = []
        else:
            workingobj = [current_element]

        for o in workingobj:
            wd = AddsDict()

            if cdata_type is None and attributes == [] and children == {}:  # We have an empty tag present - Station types use this
                return True

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
