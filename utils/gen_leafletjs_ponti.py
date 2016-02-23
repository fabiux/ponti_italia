# -*- coding: utf-8 -*-
"""
Genera un file in formato javascript per leafletjs contenente la geolocalizzazione dei ponti.
"""
from pymongo import MongoClient

ponti = MongoClient().hamradio.ponti

cnt = 0
js = ''
# estraggo solo i ponti geolocalizzati
res = ponti.find({'geoloc': {'$exists': 1}},
                 {'_id': 0, 'frequenza': 1, 'nome': 1, 'identificatore': 1, 'geoloc': 1, 'tono': 1, 'shift': 1})
markers = dict(vhf6m=[], vhf2m=[], uhf70cm=[], uhf23cm=[])
for ponte in res:
    frnum = float(ponte['frequenza'].replace(',', ''))
    # colore del marker
    if frnum < 144000:
        marker_color = 'red'
        band = 'vhf6m'
    elif frnum < 430000:
        marker_color = 'green'
        band = 'vhf2m'
    elif frnum < 440000:
        marker_color = 'blue'
        band = 'uhf70cm'
    else:
        marker_color = 'yellow'
        band = 'uhf23cm'

    desc = '<b>' + ponte['nome'] + '</b><br />frequenza: ' + ponte['frequenza'] + '<br />id: ' +\
           (ponte['identificatore'] or '') + '<br />tono: ' +\
           (ponte['tono'] or '') + '<br />shift: ' +\
           (ponte['shift'] or '')

    markers[band].append('L.marker([' + str(ponte['geoloc'][1]) + ', ' + str(ponte['geoloc'][0]) +
                         '], {icon: ' + marker_color + 'Icon}).bindPopup("' + desc + '")')

    cnt += 1

js = 'var vhf6m = L.layerGroup([' + ','.join(markers['vhf6m']) + ']);\n'
js += 'var vhf2m = L.layerGroup([' + ','.join(markers['vhf2m']) + ']);\n'
js += 'var uhf70cm = L.layerGroup([' + ','.join(markers['uhf70cm']) + ']);\n'
js += 'var uhf23cm = L.layerGroup([' + ','.join(markers['uhf23cm']) + ']);\n'
# genera il file ponti.js
with open('ponti.js', 'wb') as f:
    f.write(js)

print 'Totale ponti geolocalizzati: ' + str(cnt)
