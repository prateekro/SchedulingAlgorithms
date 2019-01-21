#!/usr/bin/env python
# coding: utf-8

# # Input = [arrival time, bursttime]

# In[1]:


inputQ = [[0, 5], [2, 4], [1, 1], [5, 2], [8, 3], [7, 4]]


# In[2]:


inputQ.sort()
arrivalTime = 0
burstTime = 0
count = 0


# In[3]:


inQueue = []


# # Create inQueue

# In[4]:


def executeProcess(inputQ, inQueue, arrivalTime):
    for process in inputQ:
        if process[0] <= arrivalTime:
            inQueue.append(process)
            inputQ.pop(inputQ.index(process))
    
    inQueue.sort(key=lambda x: int(x[1]))
    arrivalTime += inQueue[0][1]
    print("Loop: inQueue:: ", inQueue)
    inQueue.pop(0)
    
    return(inputQ, inQueue, arrivalTime)


# In[5]:


print(inputQ)
while(len(inputQ) or len(inQueue)):
    inputQ, inQueue, arrivalTime = executeProcess(inputQ, inQueue, arrivalTime)
    count += 1
    print("Step : ", count)
    print("Input Queue: ", inputQ)
    print("Running Queue: ", inQueue)
    print("Arrival Time: ", arrivalTime)
    print("-----------------------------------------------------------------------------")

print(inputQ)
print(inQueue)
print(arrivalTime)

