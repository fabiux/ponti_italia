# Ponti Italia
Alcuni script di utilità per la gestione dei dati pubblicati da <b><a href="http://www.ik2ane.it/ham.htm">IK2ANE</a></b>.

Altre funzioni di interrogazione dei dati saranno disponibili a breve.

## import.py
Importa le informazioni dei ponti radio italiani in una <i>collection</i> <code>MongoDB</code>.

Salvare il contenuto del foglio Excel <code>ponti</code> in formato <code>CSV</code>. Il file si chiama <code>pontixls.csv</code>.

Eliminare la prima riga (intestazione) e alcune righe alla fine del documento (evidentemente non necessarie).

Lanciare lo script che ricrea la collection <code>ponti</code> e ricostruisce alcuni indici.