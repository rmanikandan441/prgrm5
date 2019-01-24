def kLargest(arr, k): 
     
    arr.sort(reverse=True) 
    for i in range(k): 
        print (arr[i],end=" ")  
  

arr = [1, 27, 11, 8, 33, 5, 51] 

k = 3
kLargest(arr, k) 
  
