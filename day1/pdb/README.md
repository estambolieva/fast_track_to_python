## PDB and IPDB  
  
The module [pdb](https://docs.python.org/2/library/pdb.html) defines an interactive source code debugger for Python programs. It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control.  
  
The debugger is extensible — it is actually defined as the class Pdb. This is currently undocumented but easily understood by reading the source. The extension interface uses the modules bdb and cmd.  
  
The debugger’s prompt is (Pdb).  
    
1. Installation:

```javascript
pip install pdb
```  
  
2. Use this when you want to put a breakpoint in your code  
```javascript
pdb.set_trace()
```  