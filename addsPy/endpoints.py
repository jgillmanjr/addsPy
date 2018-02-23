"""
untangle -> dict Mapping

Implicit start from the response attribute of the parsed untangle object
"""
import pendulum
from datetime import datetime


# Type processing functions

def utc_timestamp(timestamp):
    return pendulum.parse(timestamp)

# End functions


metar = {
    'request_index': {
        'location': 'request_index',
        'cdata_type': int,
        'attributes': [],
        'multi_occurs': False,
        'children': {}
    },
    'data_source': {
        'location': 'data_source',
        'cdata_type': None,
        'attributes': [
            ('name', str),
        ],
        'multi_occurs': False,
        'children': {},
    },
    'request': {
        'location': 'request',
        'cdata_type': None,
        'attributes': [
            ('type', str),
        ],
        'multi_occurs': False,
        'children': {},
    },
    'errors': {
        'location': 'request',
        'cdata_type': None,
        'attributes': [],
        'multi_occurs': False,
        'children': {
            'error': {
                'location': 'error',
                'cdata_type': str,
                'attributes': [],
                'multi_occurs': True,
                'children': {}
            }
        },
    },
    'warnings': {
        'location': 'request',
        'cdata_type': None,
        'attributes': [],
        'multi_occurs': False,
        'children': {
            'warning': {
                'location': 'warning',
                'cdata_type': str,
                'attributes': [],
                'multi_occurs': True,
                'children': {}
            }
        },
    },
    'time_taken_ms': {
        'location': 'time_taken_ms',
        'cdata_type': int,
        'attributes': [],
        'multi_occurs': False,
        'children': {},
    },
    'data': {
        'location': 'data',
        'cdata_type': None,
        'attributes': [
            ('num_results', int),
        ],
        'multi_occurs': False,
        'children': {
            'metar': {
                'location': 'METAR',
                'cdata_type': None,
                'attributes': [],
                'multi_occurs': True,
                'children': {
                    'raw_text': {
                        'location': 'raw_text',
                        'cdata_type': str,
                        'attributes': [],
                        'multi_occurs': False,
                        'children': {}
                    },
                    'station_id': {
                        'location': 'station_id',
                        'cdata_type': str,
                        'attributes': [],
                        'multi_occurs': False,
                        'children': {}
                    },
                    'observation_time': {
                        'location': 'observation_time',
                        'cdata_type': utc_timestamp,
                        'attributes': [],
                        'multi_occurs': False,
                        'children': {}
                    },
                    'sky_condition': {
                        'location': 'sky_condition',
                        'cdata_type': None,
                        'attributes': [
                            ('sky_cover', str),
                            ('cloud_base_ft_agl', int),
                        ],
                        'multi_occurs': True,
                        'children': {}
                    },
                    'precip_24hr_in': {
                        'location': 'pcp24hr_in',
                        'cdata_type': float,
                        'attributes': [],
                        'multi_occurs': False,
                        'children': {}
                    }
                }
            }
        }
    }
}
