from multiprocessing import Process, Value, Array, Queue
from time import sleep

workingProcessID = Value('d',0)
queue = Queue()
allProcesses = []

class MyProcess:
    def __init__(self,id):
        self.id = Value('d',id)
        self.process = Process()

def add(num, value,pr,workingProcessID,allProcesses,queue):
    tmp = 0
    while True:
        if workingProcessID.value == 0 or workingProcessID.value == pr :
            workingProcessID.value = pr
        else:
            for p in allProcesses:
                if(pr == p.id) :
                    p.process.terminate()
                    queue.put(p)
        print('add')
        num.value += value
        tmp = num.value
        print("add temp first",tmp)
        sleep(1)
        print("add temp sec",tmp)
        if tmp != num.value:
            print("Process conflict1")
            
        workingProcessID.value = 0 
        if not queue.empty() :
            newQr = queue.pop()
            newQr.start()

def sub(num, value,pr,workingProcessID,allProcesses,queue):
    tmp = 0
    while True:
        if workingProcessID.value == 0 or workingProcessID.value == pr:
            workingProcessID.value = pr
        else:
            for p in allProcesses:
                if(pr == p.id) :
                    p.process.terminate()
                    queue.put(p)
        print('sub')
        num.value -= value
        tmp = num.value
        print("sub temp first",tmp)
        sleep(1.5)
        print("sub temp sec",tmp)
        if tmp != num.value:
            print("Process conflict2")
            
        workingProcessID.value = 0 
        if not queue.empty() :
            newQr = queue.pop()
            newQr.start()

def mul(num, value,pr,workingProcessID,allProcesses,queue):            
    tmp = 0
    while True:
        if workingProcessID.value == 0 or workingProcessID.value == pr:
            workingProcessID.value = pr
        else:
            for p in allProcesses:
                if(pr == p.id) :
                    p.process.terminate()
                    queue.put(p)
        print('mul')
        num.value *= value
        tmp = num.value
        print("mul temp first",tmp)
        sleep(2)
        print("mul temp sec",tmp)
        if tmp != num.value:
            print("Process conflict3")
            
        workingProcessID.value = 0 
        if not queue.empty() :
            newQr = queue.pop()
            newQr.start()

def div(num, value,pr,workingProcessID,allProcesses,queue):
    tmp = 0
    while True:
        if workingProcessID.value == 0 or workingProcessID.value == pr:
            workingProcessID.value = pr
        else:
            for p in allProcesses:
                if(pr == p.id) :
                    p.process.terminate()
                    queue.put(p)
        print('div')
        num.value /= value
        tmp = num.value
        print("div temp first",tmp)
        sleep(3)
        print("div temp sec",tmp)
        if tmp != num.value:
            print("Process conflict4")
            
        workingProcessID.value = 0       
        if not queue.empty() :
            newQr = queue.pop()
            newQr.start()

def Show(num,pr,workingProcessID,allProcesses,queue):        
    while True:
        if workingProcessID.value == 0 or workingProcessID.value == pr:
            workingProcessID.value = pr
        else:
            for p in allProcesses:
                if(pr == p.id) :
                    p.process.terminate()
                    queue.put(p)
        sleep(0.5)
        print(num.value)
        workingProcessID.value = 0   
        if not queue.empty() :
            newQr = queue.pop()
            newQr.start()
        
            

if __name__ == '__main__':
    num = Value('d', 0.0)

    arr = Array('i', range(2))
    
    p1 = MyProcess(1)
    p2 = MyProcess(2)
    p3 = MyProcess(3)
    p4 = MyProcess(4)
    show = MyProcess(5)
    
    p1.process = Process(target=add, args=(num, 10,p1.id.value,workingProcessID,allProcesses,queue))
    p2.process = Process(target=sub, args=(num, 5,p2.id.value,workingProcessID,allProcesses,queue))
    p3.process = Process(target=mul, args=(num, 2,p3.id.value,workingProcessID,allProcesses,queue))
    p4.process = Process(target=div, args=(num, 4,p4.id.value,workingProcessID,allProcesses,queue))
    show.process = Process(target=Show, args=(num,show.id.value,workingProcessID,allProcesses,queue))
    
    allProcesses = [p1,p2,p3,p4,show]
    
    show.process.start()
    sleep(1)
    p1.process.start()
    p2.process.start()
    p3.process.start()
    p4.process.start()


