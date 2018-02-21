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
#define TIME_WINDOW 20 // Time in minutes | Calc IR based on (downtime/time-window)*100
#define UPDATE_INTERVAL 20 // Time in sec between every update
#define HISTORY 1 //how much time will be taken as history to keep last state change (HISTORY * TIME_WINDOW) Eg. 2 * 1h --> i keep 1h as history 
#define JSON_PATH "/opt/lampp/htdocs/system/pageGenerator/data/"

/* SIMULATION */

//file: robotTree.h method: generateDummyTree()

#define BORN_TIME 19 //time in minutes used to calc: ARRIVE_ISTANT = (CURRENT_TIME - BORN_TIME) 
#define DUMMY 1 // set to '1' to create a dummy tree with following 2 parameters
#define N_CLUSTERS 1500 //cluster number in dummy tree
#define N_ROBOTS 900 //robot number per cluster in dummy tree
#define N_AREAS 2 //robot number per cluster in dummy tree

