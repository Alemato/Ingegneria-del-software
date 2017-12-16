## Info e configurazione

Il server è impostato per girare in localhost su una porta da specificare al momento dell'esecuzione.
Il client al momento dell'esecuzione richiede di specificare un ip (default localhost) e una porta che dovrà essere la stessa del server.

## Compilazione

Compilare il sorgente server.cpp tramite comando: | g++ server.cpp -o "nome eseguibile" |.
Compilare il sorgente client.cpp tramite comando: | g++ client.cpp -o "nome eseguibile" |.

## Utilizzo

Lanciare il server E.g. ./server 2222 .

Lanciare il client E.g. ./client localhost 2222 .


Il client potrà inviare dei messaggi di test al server (To-do : Fix bug messaggi multipli).


## Collegamento con HttpHandler (Apache)

Lanciare il server E.g. ./server 2222 .

Modificare il file "index.php" con l'ip del server e la porta su cui è in ascolto.

Il modulo php potrà inviare messaggi multipli. 

Questi verranno parsati e incapsulati all'interno di oggetti "Message" che verranno poi utilizzati nel calcolo IR e costruzione albero robot. 


## TO-DO

Creare albero N-ario di Aree-Cluster-Robot.

Algoritmo calcolo IR basato sulla visita dell'albero.


## Final TO-DO

Accelerated GPU Parallel Computation with Multi Threading by C-Cuda Library.

