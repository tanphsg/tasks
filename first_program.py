# -*- coding: utf-8 -*-
"""First_Program.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vi6f7SL-t0Kx-z9WqqYUC7BZEe9apjQt

# First program to introduce to students. Display the num of sweets to be shared among the num of people and how many sweets are left over
```
# This is formatted as code
```
"""

print("How many sweets in the bag?")
NumOfsweets = int(input())
print("How many people sharing the sweets?")
NumOfpeople = int(input())
Numofsweetsshared = NumOfsweets//NumOfpeople
NumofsweetsLeftover = NumOfsweets%NumOfpeople
print( "There will be " , Numofsweetsshared, "sweets each and there would be ",NumofsweetsLeftover, "left over")