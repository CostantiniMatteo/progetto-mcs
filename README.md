# Progetto Metodi del Calcolo Scientifico


## Progetto 1

Studio dell'implementazione di algoritmi di risoluzione diretta di sistemi lineari (Ax=b) per matrici sparse di librerie open source e confronto con l'implementazione in MATLAB.

I parametri analizzati sono:

- Tempi di calcolo
- Errore relativo della soluzione trovata rispetto alla soluzione esatta
- Memoria utilizzata per la risoluzione
- Semplicità di utilizzo della libreria
- Chiarezza della documentazione

## Linguaggi utilizzati

### MATLAB

Per la risoluzione di sistemi lineari del tipo Ax=b si utilizza la funzione `mldivide` (equivalente all'operatore `\`).

### Python

In Python è stata utilizzata la libreria `scipy`, in particolare la funzione `spsolve` di `scipy.sparse.linalg` specifica per la risoluzione di sistemi lineari la cui matrice A è sparsa.


### Uso

#### Matlab

...

#### Python

Per eseguire il codice Python è possibile utilizzare il comando

```
$ python sparse_matrix_solver.py [-u] [-i] PATH
```

`PATH` è la directory contenente le matrici da risolvere salvate in formato `.mtx`. `-u` permette di utilizzare la libreria `umfpack` per la risoluzione dei sistemi lineari. Questa è più veloce, ma a causa di un bug, con la maggior parte delle matrici verrà sollevata un'eccezione. `-i` è per lanciare il programma in modalità interattiva, ovvero dopo aver caricato la matrice e dopo averla risolta il programma si interrompe in attesa di un input.

## Progetto 2

Nella prima parte del progetto abbiamo implementato la DCT come spiegata a lezione ed abbiamo poi confrontato i tempi di esecuzione della nostra implementazione con quella della libreria scelta.

Nella seconda parte abbiamo implementato un'interfaccia minimale tramite la quale è possibile scegliere un'immagine su cui applicare un'alterazione nel dominio delle frequenze. In particolare viene calcolata la DCT dell'immagine e viene alterata in funzione dei parametri *d* e *β*. Le frequenze della DCT a partire dalla *d-esima* antidiagonale verranno moltiplicate per *β*, viene poi applicata l'IDCT e confrontata l'immagine originale con quella ottenuta dopo la trasformazione.

### Linguaggio scelto

Anche per questa parte abbiamo scelto Python e la libreria `scipy`, in questo caso il modulo utilizzato è `scipy.fftpack` che implementa diverse trasformate tra cui FFT e DCT.

### Uso

Per lanciare il programma relativo alla **prima parte** del progetto è possibile utilizzare il comando:

```
$ python parte1.py [PATH | -d]
```

Il programma calcolerà la DCT di ogni immagine in formato `.bmp` utilizzando sia la nostra implementazione, basata su quanto visto a lezione, sia quella di `scipy.fftpack.dct` e valuterà i tempi di calcolo di entrambe le versioni.


Per lanciare il programma relativo alla **seconda parte** è possibile utilizzare  la GUI lanciando il comando:

```
$ python parte2.py
```
e impostare i valori direttamente da questa.

## Studenti

- Matteo Colella, 794028
- Matteo Angelo Costantini, 795125
- Dario Gerosa, 793636
