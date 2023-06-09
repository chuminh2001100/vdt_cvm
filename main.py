from scheduler import *                                                                                                                                
import time                                                                                                                                            
from task1 import Task1                                                                                                                                
from task2 import Task2    
from task3 import Task3                                                                                                                            
from datetime import datetime                                                                                                                          
                                                                                                                                                       
current_time = datetime.now().time()                                                                                                                   
hour = current_time.strftime("%H")                                                                                                                     
minute = current_time.strftime("%M")                                                                                                                   
                                                                                                                                                       
scheduler = Scheduler()                                                                                                                                
task1 = Task1()                                                                                                                                        
task2 = Task2()                                                                                                                                        
task3 = Task3()                                                                                                                                                   
scheduler.SCH_Add_Task(task1.Task1_Run, 1000,5000) # 1s sau chạy và 5s chạy 1 lần                                                                      
scheduler.SCH_Add_Task(task2.Task2_Run, 3000,5000) # nếu task thực hiện 1 lần thì 5000 để thành 0                                             
scheduler.SCH_Add_Task(task3.Task3_Run, 4000,5000)                                                                                        
# print("Hour:", hour)                                                                                                                                 
# print("Minute:", minute)                                                                                                                             
                                                                                                                                                       
while True:                                                                                                                                            
    scheduler.SCH_Update()                                                                                                                             
    scheduler.SCH_Dispatch_Tasks()                                                                                                                     
    time.sleep(0.1)    