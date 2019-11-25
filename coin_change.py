#Coin change problem using Dynamic programing 

def coin_change( sum, denominations):
  min[0] = 0;
  for i in range(1, sum+1):
    for j in denominations:
        if j <=i:
          min(min[i], min[i-j]+1)
  return min[sum]
  
  #Explinations :
  consider a single dimention array, where indices represents the value. 
  
  now for each of the denominations, check if the index is smaller or not. 
  
  if its smaller then susbstract the denomination with the amount, and check the corresponding resulting index value and add 1 to it 
  now compair if the value of the index before substraction and the resulting index + 1 value, replace the array index  value with the 
  min value.
  
  return the corresponding value for the sum amount 
  
