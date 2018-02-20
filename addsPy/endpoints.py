"""
untangle -> dict Mapping

Implicit start from the response attribute of the parsed untangle object
"""

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
        'attributes': ['name'],
        'multi_occurs': False,
        'children': {},
    },
    'request': {
        'location': 'request',
        'cdata_type': None,
        'attributes': ['type'],
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
        'attributes': ['num_results'],
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
                    'sky_condition': {
                        'location': 'sky_condition',
                        'cdata_type': None,
                        'attributes': ['sky_cover', 'cloud_base_ft_agl'],
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
