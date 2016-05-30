## The following creates a random list of numbers (user inputs list length of numbers), and outputs the list, the sorted list, the steps in sorting the list, and the number of shifts that occured.



import numpy as np

def sortedlist(leng):
    counter=0
    aray=np.random.randint(1,1000,leng)
    for i in range(0,leng):
        ini=0
        ini1=1
        for i in aray:
            i2=aray[ini1]
            if i>i2:
                np.put(aray,ini1,i)
                np.put(aray,ini,i2)
                counter=counter+1
                print(aray)
                ini1=ini1+1
                ini=ini+1
                if ini1==len(aray):
                    break
            else:
                ini1=ini1+1
                ini=ini+1
                if ini1==len(aray):
                    break
    
    print"the number of shifts that occured are: ",counter-1
    return(aray)
    