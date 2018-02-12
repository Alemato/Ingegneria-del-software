/* DEBUG MODE */

#define DEBUG 0 // 0 disable 1 enable
#define VERBOSE 0 // display messages on console

/* PERFORMANCE TWEAKS */

#define THREAD_COUNT 1 // How many thread will consume the queue 
#define QUEUE_SLEEP 500 // How much time Queue Consumer will wait in each loop with "Empty Queue"

/* SETTINGS */

#define UPDATE_INTERVAL 15 // Time in sec between every update
#define BUFSIZE 2048
#define SERVICE_PORT 222 

/* IR */
#define TIME_WINDOW 60 // Time in minutes | Calc IR based on (downtime/time-window)*100


/* SIMULATION */

//file: robotTree.h method: generateDummyTree()

#define BORN_TIME 15 //time in minutes used to calc: ARRIVE_ISTANT = (CURRENT_TIME - BORN_TIME) 
#define N_CLUSTERS 100 //cluster number
#define N_ROBOTS 900 //robot number per cluster
