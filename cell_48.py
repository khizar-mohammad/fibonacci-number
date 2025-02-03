#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fib(n):
  if(n == 1): return 1;
  if (n == 2): return 1;
  else: return( fib(n-1) + fib(n-2) )
x = int(input("Please enter a value"))
print(fib(x));

