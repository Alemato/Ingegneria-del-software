## Info e configurazione

Il server è impostato per girare in localhost su una porta da specificare al momento dell'esecuzione. <br/>
Il client al momento dell'esecuzione richiede di specificare un ip (default localhost) e una porta che dovrà essere la stessa del server. <br/>

## Compilazione

Compilare il sorgente server.cpp tramite comando: <b> | g++ server.cpp -o "nome eseguibile" |. <br/>
Compilare il sorgente client.cpp tramite comando: <b> | g++ client.cpp -o "nome eseguibile" |. <br/>

## Utilizzo

Lanciare il server <b> E.g. ./server 2222 . </b> <br/>
 
Lanciare il client E.g. ./client localhost 2222 . <br/>


Il client potrà inviare dei messaggi di test al server (To-do : Fix bug messaggi multipli). <br/>


## Collegamento con HttpHandler (Apache)

Lanciare il server <b> E.g. ./server 2222 . </b><br/>

Modificare il file <b> "index.php" </b> con l'ip del server e la porta su cui è in ascolto. <br/>

Il modulo php potrà inviare messaggi multipli. <br/>

Questi verranno parsati e incapsulati all'interno di oggetti "Message" che verranno poi utilizzati nel calcolo IR e costruzione albero robot. <br/>


## TO-DO

Creare <b>albero N-ario</b> di Aree-Cluster-Robot. <br/>

Algoritmo <b>calcolo IR </b>basato sulla visita dell'albero. <br/>


## Final TO-DO

Accelerated GPU Parallel Computation with <b>Multi Threading by C-Cuda Library.</b> <br/>

