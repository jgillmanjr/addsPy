"""
untangle -> dict Mapping

Implicit start from the response attribute of the parsed untangle object
"""
import pendulum
from decimal import Decimal


# Type processing functions

def utc_timestamp(timestamp):
    return pendulum.parse(timestamp)


def out_bool(booltxt):
    if booltxt is None:
        return None
    return booltxt.lower() == 'true'

# End functions


metar = {
    'request_index': {
        'location': 'request_index',
        'cdata_type': int,
        'attributes': None,
        'multi_occurs': False,
        'children': None
    },
    'data_source': {
        'location': 'data_source',
        'cdata_type': None,
        'attributes': [
            ('name', str),
        ],
        'multi_occurs': False,
        'children': None,
    },
    'request': {
        'location': 'request',
        'cdata_type': None,
        'attributes': [
            ('type', str),
        ],
        'multi_occurs': False,
        'children': None,
    },
    'errors': {
        'location': 'request',
        'cdata_type': None,
        'attributes': None,
        'multi_occurs': False,
        'children': {
            'error': {
                'location': 'error',
                'cdata_type': str,
                'attributes': None,
                'multi_occurs': True,
                'children': None
            },
        },
    },
    'warnings': {
        'location': 'request',
        'cdata_type': None,
        'attributes': None,
        'multi_occurs': False,
        'children': {
            'warning': {
                'location': 'warning',
                'cdata_type': str,
                'attributes': None,
                'multi_occurs': True,
                'children': None
            },
        },
    },
    'time_taken_ms': {
        'location': 'time_taken_ms',
        'cdata_type': int,
        'attributes': None,
        'multi_occurs': False,
        'children': None,
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
                'attributes': None,
                'multi_occurs': True,
                'children': {
                    'raw_text': {
                        'location': 'raw_text',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'station_id': {
                        'location': 'station_id',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'observation_time': {
                        'location': 'observation_time',
                        'cdata_type': utc_timestamp,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'latitude': {
                        'location': 'latitude',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'longitude': {
                        'location': 'longitude',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'temp_c': {
                        'location': 'temp_c',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'dewpoint_c': {
                        'location': 'dewpoint_c',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'wind_dir_degrees': {
                        'location': 'wind_dir_degrees',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'wind_speed_kt': {
                        'location': 'wind_speed_kt',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'wind_gust_kt': {
                        'location': 'wind_gust_kt',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'visibility_statute_mi': {
                        'location': 'visibility_statute_mi',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'altim_in_hg': {
                        'location': 'altim_in_hg',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'sea_level_pressure_mb': {
                        'location': 'sea_level_pressure_mb',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'quality_control_flags': {
                        'location': 'quality_control_flags',
                        'cdata_type': None,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': {
                            'corrected': {
                                'location': 'corrected',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'auto': {
                                'location': 'auto',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'auto_station': {
                                'location': 'auto_station',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'maintenance_indicator_on': {
                                'location': 'maintenance_indicator_on',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'no_signal': {
                                'location': 'no_signal',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'lightning_sensor_off': {
                                'location': 'lightning_sensor_off',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'freezing_rain_sensor_off': {
                                'location': 'freezing_rain_sensor_off',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'present_weather_sensor_off': {
                                'location': 'present_weather_sensor_off',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                        },
                    },
                    'wx_string': {
                        'location': 'wx_string',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'sky_condition': {
                        'location': 'sky_condition',
                        'cdata_type': None,
                        'attributes': [
                            ('sky_cover', str),
                            ('cloud_base_ft_agl', int),
                        ],
                        'multi_occurs': True,
                        'children': None
                    },
                    'flight_category': {
                        'location': 'flight_category',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'three_hr_pressure_tendency_mb': {
                        'location': 'three_hr_pressure_tendency_mb',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'maxT_c': {
                        'location': 'maxT_c',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'minT_c': {
                        'location': 'minT_c',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'maxT24hr_c': {
                        'location': 'maxT24hr_c',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'minT24hr_c': {
                        'location': 'minT24hr_c',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'precip_in': {
                        'location': 'precip_in',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'pcp3hr_in': {
                        'location': 'pcp3hr_in',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'pcp6hr_in': {
                        'location': 'pcp6hr_in',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'pcp24hr_in': {
                        'location': 'pcp24hr_in',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'snow_in': {
                        'location': 'snow_in',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'vert_vis_ft': {
                        'location': 'vert_vis_ft',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'metar_type': {
                        'location': 'metar_type',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'elevation_m': {
                        'location': 'elevation_m',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                },
            },
        },
    },
}
