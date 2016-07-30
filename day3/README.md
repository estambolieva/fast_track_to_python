# DAY 3 - Numerical and Scientific Computation     
  
## [Numpy](http://www.numpy.org/) 
  
1. Multidimensional Arrays
  * slicing  
  * zeros  
  * array operations 
  * matrix multiplication  
  * identity matrix  
  * transpose  
  * broadcasting - empty_like(), pile()  
  * transpose vector - reshape()  
  * statistics  
  * random numbers 
  * where   

2. Numpy for Performance  
  * inplace and implicit copy operations  
  * ravel() is faster than flatten()  
  * efficient selection  
  * indexing - mask before np.where()  
  * unfunc at  
  * adding a column - append() v.s. hstack() v.s. r_()  
  
## [Scipy](https://www.scipy.org/)     
  
## Matplotlib  
  
1. Simple Plot  
2. Bell-shaped function anumd its tangents  
3. Gradient Based Methods   

## PRACTICAL SESSION  
  
1. Let f(x) be a function. Use Gradient Descent to find a local minimum starting x0, with step size 0.01. Plot all intermediate estinames that you obtain in the same plot. 

  a. f(x)=x^4-7x^3+12x^2+4x-16, x0 = 1.2 x0 = 1, or x0 = 4.5   
  b. f(x) = -e^(-(x+3)^2) + -e^(-x^2) + -e^-(x-3)^2), x0 = -3.2, x0 = 0 or x0 = 2.3. The function looks like [this](https://www.wolframalpha.com/input/?i=plot+-e%5E(-(x%2B3)%5E2)+%2B+-e%5E(-x%5E2)+%2B+-e%5E-(x-3)%5E2))  

2. Put Titanic Data into a numpy array  

Additional Resources:  
  
  * Numpy tutorial [here](http://cs231n.github.io/python-numpy-tutorial/#numpy) or [here](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf)  
  * Numpy Performance tricks [here](http://ipython-books.github.io/featured-01/)  
  * Advanced Numpy [here](http://www.scipy-lectures.org/advanced/advanced_numpy/)   
  * Scipy [Lectures](http://www.scipy-lectures.org/)  
  * Matplotlib short intro [here](https://github.com/LxMLS/lxmls_guide/blob/master/guides/LxMLS2015.pdf), page 9-10
  * Gradient Based Methods [here](https://github.com/LxMLS/lxmls_guide/blob/master/guides/LxMLS2015.pdf), page 21-25    