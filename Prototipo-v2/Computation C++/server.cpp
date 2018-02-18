

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
#include "./header/parameters.h" // contains system configuration parameters
#include "./header/irEngine.h"


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
concurrent_queue<Message*> messageQueue;



void consumeMessage1(Message msg){

	if(((general[msg.Id_Area])[msg.Id_Cluster]).find(msg.Name_Robot) != ((general[msg.Id_Area])[msg.Id_Cluster]).end()){
		cout<<"il robot esiste! \n";
		updateRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
	}
	else {
			addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
			if(DEBUG) cout<<"added robot "<<msg.Name_Robot<<" By Thread 1"<<"\n";
	}
	i1++;
	busy1 = false;
}

void consumeMessage2(Message msg){

	if(((general[msg.Id_Area])[msg.Id_Cluster]).find(msg.Name_Robot) != ((general[msg.Id_Area])[msg.Id_Cluster]).end()){
		cout<<"il robot esiste! \n";
		updateRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
	}
	else {
			addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
			if(DEBUG) cout<<"added robot "<<msg.Name_Robot<<" By Thread 1"<<"\n";
	}
	i2++;
	busy2 = false;
}

void consumeMessage3(Message msg){

	if(((general[msg.Id_Area])[msg.Id_Cluster]).find(msg.Name_Robot) != ((general[msg.Id_Area])[msg.Id_Cluster]).end()){
		cout<<"il robot esiste! \n";
		updateRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
	}
	else {
			addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
			if(DEBUG) cout<<"added robot "<<msg.Name_Robot<<" By Thread 1"<<"\n";
	}
	i3++;
	busy3 = false;
}

void consumeMessage4(Message msg){

	if(((general[msg.Id_Area])[msg.Id_Cluster]).find(msg.Name_Robot) != ((general[msg.Id_Area])[msg.Id_Cluster]).end()){
		cout<<"il robot esiste! \n";
		updateRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
	}
	else {
			addRobot(msg.Id_Area,msg.Id_Cluster,msg.Name_Robot,stol(msg.timeStamp),msg);
			if(DEBUG) cout<<"added robot "<<msg.Name_Robot<<" By Thread 1"<<"\n";
	}
	i4++;
	busy4 = false;
}

void queueConsumer(int j){
	
	long t = getCurrentTime();

	/* looping to look for messages to consume */

	while(true){
		
		/* triggers update and pauses consume of messages */

		if(((getCurrentTime())-t) >= (UPDATE_INTERVAL*1000)){

			std::cout<<"Updating... \n\n";
			
			clock_t c = clock();
			
			systemUpdate();

			std::cout<< "\nUPDATE OK\n";
			std::cout<< "Tempo esecuzione: " + std::to_string((double)(clock() - c)/CLOCKS_PER_SEC)<<"\n";
			printf("\nwaiting on port %d\n", SERVICE_PORT);


			t = getCurrentTime();

		}

		else{

			if(!busy1 && !busy2 && !busy3 && !busy4)
				if (!messageQueue.unsafe_size()){
					
					if(DEBUG && !resPrinted) 
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
				Message* result;
				messageQueue.try_pop(result);
				std::thread worker1(consumeMessage1,(*result));
				delete result;
				worker1.detach();
				worker1.~thread();
				
			}
			
			// Consumer-thread #2
			else if(THREAD_COUNT >= 2 && !busy2 && messageQueue.unsafe_size()){
					
				busy2 = true;
				Message* result;
				messageQueue.try_pop(result);
				std::thread worker2(consumeMessage2,(*result));
				worker2.detach();			
			}
			// Consumer-thread #3
			else if(THREAD_COUNT >= 3 && !busy3 && messageQueue.unsafe_size()){
				
				busy3 = true;
				Message* result;
				messageQueue.try_pop(result);
				std::thread worker3(consumeMessage3,(*result));
				worker3.detach();			
			}
			// Consumer-thread #4
			else if(THREAD_COUNT >= 4 && !busy4 && messageQueue.unsafe_size()){
				
				busy4 = true;
				Message* result;
				messageQueue.try_pop(result);
				std::thread worker4(consumeMessage4,(*result));
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

	Parser* p = new Parser();
	Message* msg = new Message();

	
	cout<<"\nStarting Server...\n";

	if(DUMMY) createDummyTree();
	
	//addRobot("A1","C1","R1",1518344488398);
	//cin.get();
	//cout<<"ir: "<<getBotIr(((general["A1"])["C1"])["R1"],getCurrentTime());
	//cin.get();
	
	
	/* Starting consumer queue Thread */

	if(!consumerBusy){
		cout<<"Starting Message Queue Handler...";
		std::thread queueThread(queueConsumer,0);
		queueThread.detach();
		
		consumerBusy = true;

		if(DEBUG) cout <<"\nBack to the boss!! \n";
		cout<<"OK\n";
	}

	/* create a UDP socket */
	cout<<"Creating socket...";
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
	cout<<"OK\n";
	cout<<"\nSYSTEM READY\n\n";
	/* looping to receive data */

	for (;;) {
		printf("waiting on port %d\n", SERVICE_PORT);
		//cout <<"Message ---------------------------------------------------------- count: "<<i<<"\n";
		
		recvlen = recvfrom(fd, buf, BUFSIZE, 0, (struct sockaddr *)&remaddr, &addrlen);
		if (recvlen > 0) {
			
			buf[recvlen] = 0;

			string message(buf);
			
			/* Building message object from received string */
			
			msg = (*p).parse(message);

			if(VERBOSE)  {
				cout<<"\nMessage received from robot: "<<((*msg).Name_Robot)<<" Cluster: "<<((*msg).Id_Cluster)<<" Area: "<<((*msg).Id_Area)<<"\n\n";
				if(MSG_INFO){(*msg).info();
					cout<<"\n\n";
				}
			}
			/* Pushing into queue */

			messageQueue.push(msg);

			
			

		}
		else{

			printf("error!\n");

		}
	}
	
}

