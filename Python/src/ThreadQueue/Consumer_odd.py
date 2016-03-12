
from threading import Thread
import time;

class Consumer_oddCLS(Thread):
    '''
    classdocs
    '''


    def __init__(self, t_name,queue):
        '''
        Constructor
        '''
        Thread.__init__(self,name=t_name);
        self.data = queue;
    
    def run(self):
        while 1:
            try:
                val_odd = self.data.get(1,5);
                if val_odd %2 != 0:
                    print('%s:%s is consuming. %d in the queue is consumed!'%(time.ctime(),self.getName(),val_odd));
                    time.sleep(2);
                else:
                    self.data.put(val_odd);
                    time.sleep(2);
            except:
                print('%s:%s finished!'%(time.ctime(),self.getName()));
                break;
                    
        