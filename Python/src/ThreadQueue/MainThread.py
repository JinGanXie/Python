
from queue import Queue
from ThreadQueue.Producer import ProducerCLS
from ThreadQueue.Consumer_even import Consumer_evenCLS
from ThreadQueue.Consumer_odd import Consumer_oddCLS


def MainThread():
    
    queue = Queue();
    producer = ProducerCLS('Pro.',queue);
    consumer_even = Consumer_evenCLS('Con_even',queue);
    consumer_odd = Consumer_oddCLS('Con_odd',queue);
    
    producer.start();
    consumer_even.start();
    consumer_odd.start();
    producer.join();
    consumer_even.join();
    consumer_odd.join();
    print('All theads terminate');
    
    
    
if __name__ == '__main__':
    MainThread();
    pass