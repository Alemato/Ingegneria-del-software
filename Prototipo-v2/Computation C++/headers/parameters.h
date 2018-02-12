/* DEBUG MODE */

#define DEBUG 0 // 0 disable 1 enable

/* SERVER SETTING */

#define BUFSIZE 2048
#define SERVICE_PORT 222 
#define VERBOSE 1 // display messages on console
#define MSG_INFO 0 // display content of messages 

/* PERFORMANCE TWEAKS */

#define THREAD_COUNT 1 // How many thread will consume the message queue 
#define QUEUE_SLEEP 500 // How much time Queue Consumer will wait in each loop with "Empty Queue"

/* IR */
#define TIME_WINDOW 5 // Time in minutes | Calc IR based on (downtime/time-window)*100
#define UPDATE_INTERVAL 8 // Time in sec between every update

/* SIMULATION */

//file: robotTree.h method: generateDummyTree()

#define BORN_TIME 0 //time in minutes used to calc: ARRIVE_ISTANT = (CURRENT_TIME - BORN_TIME) 
#define DUMMY 0 // set to '1' to create a dummy tree with following 2 parameters
#define N_CLUSTERS 100 //cluster number in dummy tree
#define N_ROBOTS 900 //robot number per cluster in dummy tree
