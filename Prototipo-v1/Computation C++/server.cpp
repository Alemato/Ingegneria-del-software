/* A simple server in the internet domain using TCP
   The port number is passed as an argument */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
//#include "./header/msg_parser.h"
#include "./header/message.h"
#include <fcntl.h>

#define BUFF_SIZE 256


void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno;
     socklen_t clilen;
     char buffer[BUFF_SIZE];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
     
     Message messaggio;

     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     sockfd = socket(AF_INET, SOCK_STREAM, 0);
     
     //fcntl(sockfd, F_SETFL, O_NONBLOCK);

     if (sockfd < 0)
        error("ERROR opening socket");
     
     bzero((char *) &serv_addr,  sizeof(serv_addr));
     portno = atoi(argv[1]);
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);

     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0)
              error("ERROR on binding");


 while(1){

    listen(sockfd,5);
    
    while(1){

        clilen = sizeof(cli_addr);

        newsockfd = accept(sockfd,
                    (struct sockaddr *) &cli_addr,
                    &clilen);

        write(newsockfd,"Connessione Stabilita",28);

        if (newsockfd < 0)
            error("ERROR on accept");
        
        bzero(buffer,BUFF_SIZE);

        

        n = read(newsockfd,buffer,BUFF_SIZE);
        
        //if (n < 0) error("ERROR reading from socket");
        //printf("Here is the message: %s\n",buffer);
        
        //n = write(newsockfd,"I got your message",18);
        //if (n < 0) error("ERROR writing to socket");

     
        Parser p;
        Message* messaggio = p.parse((string) buffer);

        cout<<"Messaggio ricevuto e parsato \n";
        cout<<"Contenuto messaggio: \n";

        Message msg = *messaggio;

        msg.info();

        cout<<"In attesa di un messaggio...\n";

        //close(newsockfd);
        
        //close(sockfd);

        }

        write(newsockfd,"Connessione Interrotta",28); 
    }
    
    close(newsockfd);
    close(sockfd);

    return 0;

}
