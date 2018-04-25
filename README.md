#Progetto Metodi del Calcolo Scientifico

Studio dell'implementazione di algoritmi di risoluzione diretta di sistemi lineari (Ax=b) per matrici sparse di librerie open source e confronto con l'implementazione in MATLAB.

I parametri analizzati sono:

- Tempi di calcolo
- Errore relativo della soluzione trovata rispetto alla soluzione esatta
- Memoria utilizzata per la risoluzione
- Semplicità di utilizzo della libreria
- Chiarezza della documentazione

## Studenti
- Matteo Colella, 794028
- Matteo Angelo Costantini, 795125
- Dario Gerosa, 793636

## Linguaggi utilizzati

### MATLAB
Per la risoluzione di sistemi lineari del tipo Ax=b si utilizza la funzione `mldivide` (equivalente all'operatore `\`).

### Python
In Python è stata utilizzata la libreria `scipy` utilizzando la funzione `spsolve` di `scipy.sparse.linalg` specifica per la risoluzione di sistemi lineari la cui matrice A è sparsa. I test sono stati fatti richiamando la funzione sia con che senza la libreria `umfpack` che permette di accelerare i calcoli.