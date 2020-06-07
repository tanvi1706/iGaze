# importing the required module 
import matplotlib.pyplot as plt 
  
# x axis values 
x = [6,8,10,12,14] 
# corresponding y axis values 
y = [10.75,13.29,14.86,17.77,19.05] 
  
# plotting the points  
plt.plot(x, y,color='red',marker='o',markerfacecolor='blue',markersize=12) 

#plt.plot(x, y)
# naming the x axis 
plt.xlabel('Path Length') 
# naming the y axis 
plt.ylabel('Time') 
# function to show the plot 
plt.show() 


# line 2 points 
#x2 = [1,2,3] 
#y2 = [4,1,3] 
# plotting the line 2 points  
#plt.plot(x2, y2, label = "line 2") 
