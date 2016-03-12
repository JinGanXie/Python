
import time;
import random
from threading import Thread

class ProducerCLS(Thread):
    '''
    classdocs
    '''


    def __init__(self, t_name,queue):
        '''
        Constructor
        '''
        Thread.__init__(self, name=t_name);
        self.data=queue;
    
    def run(self):
        for i in range(10): #随机产生10个数字 ，可以修改为任意大小
            randomnum = random.randint(1,99);
            print('%s:%s is producing %d to the queue!'%(time.ctime(),self.getName(),randomnum));
            self.data.put(randomnum);#将数据依次存入队列
            time.sleep(1);
        print('%s:%s finshed!'%(time.ctime(),self.getName()));
        
            
    
        