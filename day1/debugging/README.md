## Debugging with PyCharm  
  
1. Click debug button  

2. Add a breakpoint  

3. Reload URL (as it the current scenario we print "Hello RAND_NUM" on 127.0.0.1:5000, where RAND_NUM is the highest random number we have seen after drawing 100 random numbers) 
![alt tag](https://github.com/estambolieva/fast_track_to_python/blob/master/day1/debugging/images/breakpoint.PNG)  
  
4. Evaluate an expression  by clicking this button  
![alt tag](https://github.com/estambolieva/fast_track_to_python/blob/master/day1/debugging/images/evaluate_expression.PNG)

5. Go back to Console, and select "Show Python Prompt"  
  * there you can see current values of variables, and evaluate expressions such as (var + 20)/2  
![alt tag](https://github.com/estambolieva/fast_track_to_python/blob/master/day1/debugging/images/interactive_console.PNG)  

6. Walk Through Exacution  
  * insert a new breakpoint inside the loop - line 9 
  * reload page  
  * click green button to iterate over the separate calls of the foor loop  
   
 7. Step into  
   * insert a new breakpoint - line 20    
   * press Step Into My Code to enter the inner fuction  
 ![alt tag](https://github.com/estambolieva/fast_track_to_python/blob/master/day1/debugging/images/step_into_my_code.PNG)  
  
 8. Watches  
   * track the value of r on each iteration and see if ti is bigger than highest - to do that, set a new breakpoint at line number 10  s
  
Note:  

This code followed the following [video tutorial](https://www.youtube.com/watch?v=QJtWxm12Eo0)  