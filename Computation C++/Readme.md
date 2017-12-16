## Info e configurazione

Il server è impostato per girare in localhost su una porta da specificare al momento dell'esecuzione. <br/>
Il client al momento dell'esecuzione richiede di specificare un ip (default localhost) e una porta che dovrà essere la stessa del server. <br/>

## Compilazione

Compilare il sorgente server.cpp tramite comando: | g++ server.cpp -o "nome eseguibile" |. <br/>
Compilare il sorgente client.cpp tramite comando: | g++ client.cpp -o "nome eseguibile" |. <br/>

## Utilizzo

Lanciare il server E.g. ./server 2222 . <br/>
 
Lanciare il client E.g. ./client localhost 2222 . <br/>


Il client potrà inviare dei messaggi di test al server (To-do : Fix bug messaggi multipli). <br/>


## Collegamento con HttpHandler (Apache)

Lanciare il server E.g. ./server 2222 . <br/>

Modificare il file "index.php" con l'ip del server e la porta su cui è in ascolto. <br/>

Il modulo php potrà inviare messaggi multipli. <br/>

Questi verranno parsati e incapsulati all'interno di oggetti "Message" che verranno poi utilizzati nel calcolo IR e costruzione albero robot. <br/>


## TO-DO

Creare albero N-ario di Aree-Cluster-Robot. <br/>

Algoritmo calcolo IR basato sulla visita dell'albero. <br/>


## Final TO-DO

Accelerated GPU Parallel Computation with Multi Threading by C-Cuda Library. <br/>

