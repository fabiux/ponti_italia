# -*- coding: utf-8 -*-
"""
Genera un file in formato GeoJSON contenente la geolocalizzazione dei ponti.
"""
from pymongo import MongoClient
from json import dump

ponti = MongoClient().hamradio.ponti

cnt = 0
json = dict(type='FeatureCollection',
            crs=dict(type='name',
                     properties=dict(name='urn:ogc:def:crs:OGC:1.3:CRS84')),
            features=[])
# estraggo solo i ponti geolocalizzati
res = ponti.find({'geoloc': {'$exists': 1}},
                 {'_id': 0, 'frequenza': 1, 'nome': 1, 'identificatore': 1, 'geoloc': 1, 'tono': 1, 'shift': 1})
for ponte in res:
    frnum = float(ponte['frequenza'].replace(',', ''))
    # colore del marker
    if frnum < 144000:
        marker_color = '#ffff00'
    elif frnum < 430000:
        marker_color = '#ff0000'
    elif frnum < 436000:
        marker_color = '#00ff00'
    else:
        marker_color = '#0000ff'
    properties = {'name': ponte['nome'],
                  'marker-color': marker_color,
                  'marker-symbol': 'circle-stroked',
                  'title': ponte['nome'],
                  'description': 'frequenza: ' + ponte['frequenza'] + '<br />id: ' +
                                 (ponte['identificatore'] or '') + '<br />tono: ' +
                                 (ponte['tono'] or '') + '<br />shift: ' + (ponte['shift'] or '')
                  }
    feature = dict(type='Feature',
                   properties=properties,
                   geometry=dict(type='Point', coordinates=ponte['geoloc']))
    json['features'].append(feature)
    cnt += 1
with open('ponti.json', 'wb') as f:
    dump(json, f, indent=4, separators=(',',':'))
print 'Totale ponti geolocalizzati: ' + str(cnt)
