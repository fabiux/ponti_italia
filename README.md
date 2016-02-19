# Ponti Italia
Alcuni script di utilità per la gestione dei dati pubblicati da <b><a href="http://www.ik2ane.it/ham.htm">IK2ANE</a></b>.

Altre funzioni di interrogazione dei dati saranno disponibili a breve.

## import.py
Importa le informazioni dei ponti radio italiani in una <i>collection</i> <code>MongoDB</code>.

Salvare il contenuto del foglio Excel <code>ponti</code> in formato <code>CSV</code>. Il file si chiama <code>pontixls.csv</code>.

Eliminare la prima riga (intestazione) e alcune righe alla fine del documento (evidentemente non necessarie).

Lanciare lo script che ricrea la collection <code>ponti</code> e ricostruisce alcuni indici.

## gen_geojson.py
Esporta le informazioni dei ponti geolocalizzati nel file <code>ponti.json</code>, in formato <code>GeoJSON</code>.

## Esempi di query
Numero di ponti per provincia:

    db.ponti.aggregate([{$group: {_id: '$provincia', count: {$sum: 1}}}])

Ponti di una provincia:

    db.ponti.find({provincia: 'PV'}, {_id:0, frequenza: 1, nome: 1, tono: 1, shift: 1, localita: 1})

Lista delle province e delle regioni:

    db.ponti.aggregate([{$group: {_id: '$provincia'}}, {$sort: {_id: 1}}])
    db.ponti.aggregate([{$group: {_id: '$regione'}}, {$sort: {_id: 1}}])

Lista dei nomi:

    db.ponti.aggregate([{$group: {_id: '$nome'}}, {$sort: {_id: 1}}])

Ponti nelle vicinanze (ad es., entro 50 km da un punto):

    db.ponti.find({geoloc: {$near: {$geometry: {type: "Point", coordinates: [8.88, 46.24]},
                            $maxDistance: 50000}}},
                  {_id:0, frequenza: 1, nome: 1, localita: 1})