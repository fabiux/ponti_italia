# -*- coding: utf-8 -*-
"""
Importazione del database dei ponti italiani.
Pubblicati da IK2ANE in formato Excel, salvare sul file pontixls.csv.
Rimuovere la prima riga (intestazione) e alcune delle ultime righe del file.
Vedere: http://www.ik2ane.it
Autore: Fabio Pani [IZ2UQF] <fabiux@fabiopani.it>
Licenza d'uso: GNU/GPL v3 (vedere file LICENSE allegato)
"""
from pymongo import MongoClient
from csv import reader

ponti = MongoClient().hamradio.ponti
ponti.drop()  # ricostruisce la collection da capo

with open('pontixls.csv', 'rb') as f:
    csvfile = reader(f)
    for row in csvfile:
        doc = dict(nome=row[0].strip(),
                   frequenza=row[1].strip(),
                   shift=row[2].strip(),
                   tono=row[3].strip(),
                   regione=row[4].strip().lower(),
                   provincia=row[5].strip().upper(),
                   localita=row[6].strip(),
                   gruppo=row[7].strip(),
                   identificatore=row[8].strip(),
                   traslatore=row[9].strip(),
                   locator=row[10].strip(),
                   gestore=row[15].strip())
        ponti.insert_one(doc)

ponti.create_index('nome')
ponti.create_index('regione')
ponti.create_index('provincia')
