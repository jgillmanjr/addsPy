"""
untangle -> dict Mapping

Implied start from the response attribute of the parsed untangle object
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


metars = {
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
        'location': 'errors',
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
        'location': 'warnings',
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
            'METAR': {
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

pireps = {
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
        'location': 'errors',
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
        'location': 'warnings',
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
            'AircraftReport': {
                'location': 'AircraftReport',
                'cdata_type': None,
                'attributes': None,
                'multi_occurs': True,
                'children': {
                    'receipt_time': {
                        'location': 'receipt_time',
                        'cdata_type': utc_timestamp,
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
                    'quality_control_flags': {
                        'location': 'quality_control_flags',
                        'cdata_type': None,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': {
                            'mid_point_assumed': {
                                'location': 'mid_point_assumed',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'no_time_stamp': {
                                'location': 'no_time_stamp',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'flt_lvl_range': {
                                'location': 'flt_lvl_range',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'above_ground_level_indicated': {
                                'location': 'above_ground_level_indicated',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'no_flt_lvl': {
                                'location': 'no_flt_lvl',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'bad_location': {
                                'location': 'bad_location',
                                'cdata_type': out_bool,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                        },
                    },
                    'aircraft_ref': {
                        'location': 'aircraft_ref',
                        'cdata_type': str,
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
                    'altitude_ft_msl': {
                        'location': 'altitude_ft_msl',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'sky_condition': {
                        'location': 'sky_condition',
                        'cdata_type': None,
                        'attributes': [
                            ('sky_cover', str),
                            ('cloud_base_ft_msl', int),
                            ('cloud_top_ft_msl', int),
                        ],
                        'multi_occurs': True,
                        'children': None
                    },
                    'turbulence_condition': {
                        'location': 'turbulence_condition',
                        'cdata_type': None,
                        'attributes': [
                            ('turbulence_type', str),
                            ('turbulence_intensity', str),
                            ('turbulence_base_ft_msl', int),
                            ('turbulence_top_ft_msl', int),
                            ('turbulence_freq', str),
                        ],
                        'multi_occurs': True,
                        'children': None
                    },
                    'icing_condition': {
                        'location': 'icing_condition',
                        'cdata_type': None,
                        'attributes': [
                            ('icing_type', str),
                            ('icing_intensity', str),
                            ('icing_base_ft_msl', int),
                            ('icing_top_ft_msl', int),
                        ],
                        'multi_occurs': True,
                        'children': None
                    },
                    'visibility_statute_mi': {
                        'location': 'visibility_statute_mi',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'wx_string': {
                        'location': 'wx_string',
                        'cdata_type': str,
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
                    'vert_gust_kt': {
                        'location': 'vert_gust_kt',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'report_type': {
                        'location': 'report_type',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'raw_text': {
                        'location': 'raw_text',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                },
            },
        },
    },
}

tafs = {
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
        'location': 'errors',
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
        'location': 'warnings',
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
            'TAF': {
                'location': 'TAF',
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
                    'issue_time': {
                        'location': 'issue_time',
                        'cdata_type': utc_timestamp,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'bulletin_time': {
                        'location': 'bulletin_time',
                        'cdata_type': utc_timestamp,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'valid_time_from': {
                        'location': 'valid_time_from',
                        'cdata_type': utc_timestamp,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'valid_time_to': {
                        'location': 'valid_time_to',
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
                    'elevation_m': {
                        'location': 'elevation_m',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'forecast': {
                        'location': 'forecast',
                        'cdata_type': None,
                        'attributes': None,
                        'multi_occurs': True,
                        'children': {
                            'fcst_time_from': {
                                'location': 'fcst_time_from',
                                'cdata_type': utc_timestamp,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'fcst_time_to': {
                                'location': 'fcst_time_to',
                                'cdata_type': utc_timestamp,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'change_indicator': {
                                'location': 'change_indicator',
                                'cdata_type': str,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'time_becoming': {
                                'location': 'time_becoming',
                                'cdata_type': utc_timestamp,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'probability': {
                                'location': 'probability',
                                'cdata_type': int,
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
                            'wind_shear_hgt_ft_agl': {
                                'location': 'wind_shear_hgt_ft_agl',
                                'cdata_type': int,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'wind_shear_dir_degrees': {
                                'location': 'wind_shear_dir_degrees',
                                'cdata_type': int,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'wind_shear_speed_kt': {
                                'location': 'wind_shear_speed_kt',
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
                            'vert_vis_ft': {
                                'location': 'vert_vis_ft',
                                'cdata_type': int,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'wx_string': {
                                'location': 'wx_string',
                                'cdata_type': str,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'not_decoded': {
                                'location': 'not_decoded',
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
                                    ('cloud_type', str),
                                ],
                                'multi_occurs': True,
                                'children': None
                            },
                            'turbulence_condition': {
                                'location': 'turbulence_condition',
                                'cdata_type': None,
                                'attributes': [
                                    ('turbulence_intensity', str),
                                    ('turbulence_min_alt_ft_agl', int),
                                    ('turbulence_max_alt_ft_agl', int),
                                ],
                                'multi_occurs': True,
                                'children': None
                            },
                            'icing_condition': {
                                'location': 'icing_condition',
                                'cdata_type': None,
                                'attributes': [
                                    ('icing_intensity', str),
                                    ('icing_min_alt_ft_agl', int),
                                    ('icing_max_alt_ft_agl', int),
                                ],
                                'multi_occurs': True,
                                'children': None
                            },
                            'temperature': {
                                'location': 'temperature',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': True,
                                'children': {
                                    'valid_time': {
                                        'location': 'valid_time',
                                        'cdata_type': str,
                                        'attributes': None,
                                        'multi_occurs': False,
                                        'children': None
                                    },
                                    'sfc_temp_c': {
                                        'location': 'sfc_temp_c',
                                        'cdata_type': Decimal,
                                        'attributes': None,
                                        'multi_occurs': False,
                                        'children': None
                                    },
                                    'max_temp_c': {
                                        'location': 'max_temp_c',
                                        'cdata_type': Decimal,
                                        'attributes': None,
                                        'multi_occurs': False,
                                        'children': None
                                    },
                                    'min_temp_c': {
                                        'location': 'min_temp_c',
                                        'cdata_type': Decimal,
                                        'attributes': None,
                                        'multi_occurs': False,
                                        'children': None
                                    },
                                }
                            },
                        }
                    },
                },
            },
        },
    },
}

airsigmets = {
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
        'location': 'errors',
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
        'location': 'warnings',
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
            'AIRSIGMENT': {
                'location': 'AIRSIGMET',
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
                    'valid_time_from': {
                        'location': 'valid_time_from',
                        'cdata_type': utc_timestamp,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'valid_time_to': {
                        'location': 'valid_time_to',
                        'cdata_type': utc_timestamp,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'altitude': {
                        'location': 'altitude',
                        'cdata_type': None,
                        'attributes': [
                            ('min_ft_msl', int),
                            ('max_ft_msl', int),
                        ],
                        'multi_occurs': False,
                        'children': None
                    },
                    'movement_dir_degrees': {
                        'location': 'movement_dir_degrees',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'movement_speed_kt': {
                        'location': 'movement_speed_kt',
                        'cdata_type': int,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'hazard': {
                        'location': 'hazard',
                        'cdata_type': None,
                        'attributes': [
                            ('type', str),
                            ('severity', str),
                        ],
                        'multi_occurs': False,
                        'children': None
                    },
                    'airsigment_type': {
                        'location': 'airsigment_type',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'area': {
                        'location': 'area',
                        'cdata_type': None,
                        'attributes': [
                            ('num_points', int)
                        ],
                        'multi_occurs': True,
                        'children': {
                            'point': {
                                'location': 'point',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': True,
                                'children': {
                                    'longitude': {
                                        'location': 'longitude',
                                        'cdata_type': Decimal,
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
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}

stations = {
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
        'location': 'errors',
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
        'location': 'warnings',
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
            'Station': {
                'location': 'Station',
                'cdata_type': None,
                'attributes': None,
                'multi_occurs': True,
                'children': {
                    'station_id': {
                        'location': 'station_id',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'wmo_id': {
                        'location': 'wmo_id',
                        'cdata_type': str,
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
                    'elevation_m': {
                        'location': 'elevation_m',
                        'cdata_type': Decimal,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'site': {
                        'location': 'site',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'state': {
                        'location': 'state',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'country': {
                        'location': 'country',
                        'cdata_type': str,
                        'attributes': None,
                        'multi_occurs': False,
                        'children': None
                    },
                    'site_type': {
                        'location': 'site_type',
                        'cdata_type': None,
                        'attributes': None,
                        'multi_occurs': False,
                        'has_empty_children': True,
                        'children': {
                            'METAR': {
                                'location': 'METAR',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'rawinsonde': {
                                'location': 'rawinsonde',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'TAF': {
                                'location': 'TAF',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'NEXRAD': {
                                'location': 'NEXRAD',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'wind_profiler': {
                                'location': 'wind_profiler',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'WFO_office': {
                                'location': 'WFO_office',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                            'SYNOPS': {
                                'location': 'SYNOPS',
                                'cdata_type': None,
                                'attributes': None,
                                'multi_occurs': False,
                                'children': None
                            },
                        }
                    },
                },
            },
        },
    },
}