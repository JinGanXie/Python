
import time;
from threading import Thread

class Consumer_evenCLS(Thread):
    '''
    classdocs
    '''


    def __init__(self, t_name,queue):
        '''
        Constructor
        '''
        Thread.__init__(self, name=t_name);
        self.data = queue;
    
    def run(self):
        while 1:
            try:
                val_even =self.data.get(1,5); #get(self, block=True, timeout=None) ,1就是阻塞等待,5是超时5秒
                if val_even%2 == 0:
                    print('%s:%s is consuming %d in the queue is consumed' %(time.ctime(),self.getName(),val_even));
                else:
                    self.data.put(val_even);
                    time.sleep(2);
            except: #等待输入，超过5秒 就报异常
                print('%s:%s finished!'%(time.ctime(),self.getName()));
                
                
                
        