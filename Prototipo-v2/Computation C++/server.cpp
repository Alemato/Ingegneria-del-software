/* DEBUG MODE */

#define DEBUG 1 // 0 disable 1 enable
#define VERBOSE 1 // display messages on console

/* PERFORMANCE TWEAKS */

#define THREAD_COUNT 1 // How many thread will consume the queue 
#define QUEUE_SLEEP 500 // How much time Queue Consumer will wait in each loop with "Empty Queue"

/* SETTINGS */

#define UPDATE_INTERVAL 15 // Time in sec between every update
#define BUFSIZE 2048
#define SERVICE_PORT 222 

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include "./header/robotTree.h" // functions to manipulate robot tree
#include "./header/msgParser.h" // functions to parse messages
#include "./header/message.h" // message class
#include "./header/update.h"
#include <thread>
#include <string>
#include <tbb/concurrent_queue.h> // tbb library to manipulate concurrent_queue


bool busy1 = false;
bool busy2 = false;
bool busy3 = false;
bool busy4 = false;
bool consumerBusy = false;
bool resPrinted = false;
bool updating = false;

int i=0;
int i1=0,i2=0,i3=0,i4=0;

using namespace std;
using namespace tbb;


//queue holding messages
concurrent_queue<Message> messageQueue;



void consumeMessage1(Message msg){
	//addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot+"-t1",1516903200000);
	if(DEBUG) cout<<"added robot "<<msg.Name_Robot<<" By Thread 1"<<"\n";
	i1++;
	busy1 = false;
}

void consumeMessage2(Message msg){
	addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot+"-t2",1516903200000);
	cout<<"added robot "<<msg.Name_Robot<<" By Thread 2"<<"\n";
	//printRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot+"-t2");
	i2++;
	busy2 = false;
}

void consumeMessage3(Message msg){
	addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot+"-t3",1516903200000);
	cout<<"added robot "<<msg.Name_Robot<<" By Thread 3"<<"\n";
	//printRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot+"-t3");
	i3++;
	busy3 = false;
}

void consumeMessage4(Message msg){
	addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot+"-t4",1516903200000);
	cout<<"added robot "<<msg.Name_Robot<<" By Thread 4"<<"\n";
	//printRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot+"-t3");
	i4++;
	busy4 = false;
}

void queueConsumer(int j){
	
	long t = getCurrentTime();

	/* looping to look for messages to consume */

	while(true){
		
		if(((getCurrentTime())-t) >= (UPDATE_INTERVAL*1000)){

			std::cout<<"Updating...";
			
			clock_t c = clock();
			
			systemUpdate();

			std::cout<< "OK \n";
			std::cout<< "Tempo esecuzione: " + std::to_string((double)(clock() - c)/CLOCKS_PER_SEC)<<"\n";

			t = getCurrentTime();

		}

		else{

			if(!busy1 && !busy2 && !busy3 && !busy4)
				if (!messageQueue.unsafe_size()){
					
					if(VERBOSE && !resPrinted) 
						{
							cout<<"Queue is empty - "<<"Message count: "<<to_string(i1+i2+i3+i4)<<"\n";
							resPrinted = true;
						}
					
					//sleep to low cpu usage
					usleep(QUEUE_SLEEP);
					continue;

				} else resPrinted = false;

			// Consumer-thread #1
			if(!busy1 && messageQueue.unsafe_size()){
				
				busy1 = true;
				Message result;
				messageQueue.try_pop(result);
				std::thread worker1(consumeMessage1,result);
				worker1.detach();
				
			}
			// Consumer-thread #2
			else if(THREAD_COUNT >= 2 && !busy2 && messageQueue.unsafe_size()){
					
				busy2 = true;
				Message result;
				messageQueue.try_pop(result);
				std::thread worker2(consumeMessage2,result);
				worker2.detach();			
			}
			// Consumer-thread #3
			else if(THREAD_COUNT >= 3 && !busy3 && messageQueue.unsafe_size()){
				
				busy3 = true;
				Message result;
				messageQueue.try_pop(result);
				std::thread worker3(consumeMessage3,result);
				worker3.detach();			
			}
			// Consumer-thread #4
			else if(THREAD_COUNT >= 4 && !busy4 && messageQueue.unsafe_size()){
				
				busy4 = true;
				Message result;
				messageQueue.try_pop(result);
				std::thread worker4(consumeMessage4,result);
				worker4.detach();			
			}
		}
		
	}
		
}

int
main(int argc, char **argv)
{
	struct sockaddr_in myaddr;	/* our address */
	struct sockaddr_in remaddr;	/* remote address */
	socklen_t addrlen = sizeof(remaddr);		/* length of addresses */
	int recvlen = 0;			/* # bytes received */
	int fd = 0;				/* our socket */
	char buf[BUFSIZE];	/* receive buffer */

	Parser p;


	/* create a UDP socket */

	if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
		perror("cannot create socket\n");
		return 0;
	}

	/* bind the socket to any valid IP address and a specific port */

	memset((char *)&myaddr, 0, sizeof(myaddr));
	myaddr.sin_family = AF_INET;
	myaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	myaddr.sin_port = htons(SERVICE_PORT);

	if (bind(fd, (struct sockaddr *)&myaddr, sizeof(myaddr)) < 0) {
		perror("bind failed");
		return 0;
	}
	
	/* looping to receive data */

	for (;;) {
		printf("waiting on port %d\n", SERVICE_PORT);
		//cout <<"Message ---------------------------------------------------------- count: "<<i<<"\n";
		
		recvlen = recvfrom(fd, buf, BUFSIZE, 0, (struct sockaddr *)&remaddr, &addrlen);
		if (recvlen > 0) {
			
			buf[recvlen] = 0;

			string message(buf);
			
			Parser* p = new Parser();

			/* Building message object from received string */

			Message* msg = new Message();

			msg = (*p).parse(message);

			if(DEBUG) (*msg).info();
			
			/* Pushing into queue */

			messageQueue.push(*msg);
			
	
			/* Starting consumer queue Thread */

			if(!consumerBusy){
				
				std::thread queueThread(queueConsumer,0);
				queueThread.detach();
				
				consumerBusy = true;

				if(DEBUG) cout <<"Back to the boss!! \n";

			}
		
		}
		else{

			printf("error!\n");

		}
	}
	
}

