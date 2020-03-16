## -*- mode: python; coding: utf-8 -*-

# Mixin include file to add domosqed to a test

DOMOS_QED_HOSTS=get_test_parameter('domos_qed', default=[], split=True)
#Stats collection from the routers:
for router in DOMOS_QED_HOSTS:
    DATA_SETS["domos_qed_%s" % router] = {'test': 'CPU_STATS',
                   'interval': 0.2,
                   'length': LENGTH,
                   'sta': ("192.168.1.190", "78:0c:b8:63:8b:8e"),
                   'host': router,
                   'interface': "wlan0",
                   'units': '',
                   'runner': 'domqos'}

if DOMOS_QED_HOSTS:
    
    PLOTS['CPU load'] = {'description': 'CPU load in %',
                         'type': 'timeseries',
                         'legend_title': 'CPU load',
                         'series': [{'data': glob('domos_qed_*'),
                                     'raw_key': "CPU",
                                     'label': 'CPU %'},]}
    
    PLOTS['GF Ping'] = {'description': 'Gaming first ping(ms)',
                        'type': 'timeseries',
                        'legend_title': 'GF Ping(ms)',
                        'series': [{'data': glob('domos_qed_*'),
                                    'raw_key': "min",
                                    'label': 'Ping (min)'},
                                   {'data': glob('domos_qed_*'),
                                    'raw_key': "avg",
                                    'label': 'Ping (avg)'},
                                   {'data': glob('domos_qed_*'),
                                    'raw_key': "max",
                                    'label': 'Ping (max)'},]}
    
    PLOTS['BW limit'] = {'description': 'BW limit (Mbit/s)',
                         'type': 'timeseries',
                         'legend_title': 'GF BW limit(Mbit/s)',
                         'series': [{'data': glob('domos_qed_*'),
                                     'raw_key': "Limit",
                                     'label': 'BW limit'},]}
    
    PLOTS['GF Data'] = {'description': "All GF data",
                        'type': 'meta',
                        'subplots': ('CPU load', 'GF Ping', 'BW limit')}
    
    PLOTS['Radio stats'] = {'description': 'Radio use in ms',
                            'type': 'timeseries',
                            'legend_title': 'Channel use in ms',
                            'series': [{'data': glob('domos_qed_*'),
                                        'raw_key': "ch_time",
                                        'label': 'ch_time',
                                        'ignore_zeros': 1,},
                                       {'data': glob('domos_qed_*'),
                                        'raw_key': "ch_time_busy",
                                        'label': 'ch_time_busy',
                                        'ignore_zeros': 1,},
                                       {'data': glob('domos_qed_*'),
                                        'raw_key': "ch_time_tx",
                                        'label': 'ch_time_tx',
                                        'ignore_zeros': 1,},
                                       {'data': glob('domos_qed_*'),
                                        'raw_key': "ch_time_rx",
                                        'label': 'ch_time_rx',
                                        'ignore_zeros': 1,},]}

    PLOTS['PHY Stats'] = {'description': 'PHY stats',
                              'type': 'timeseries',
                              'legend_title': '',
                              'series': [{'data': glob('domos_qed_*'),
                                          'raw_key': "rx_bitrate",
                                          'label': 'rx_bitrate'},
                                         {'data': glob('domos_qed_*'),
                                          'raw_key': "tx_bitrate",
                                          'label': 'tx_bitrate'},
                                         {'data': glob('domos_qed_*'),
                                          'raw_key': "signal",
                                          'label': 'rssi'},]}
