UECM3033 Assignment #2 Report
========================================================

- Prepared by: Lee Hui Zhong
- Tutorial Group: T2 

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

https://github.com/Huizhonglee/UECM3033_assign2

Explain your selection criteria here.

Explain how you implement your `task1.py` here.

At first, 

For SOR method, I used ?¦Ø=1.25. A positive ¦Ø can help us to get convergence. SOR method can convergence only when 0< ¦Ø<2. The SOR method will reduce to the Gauss Seidel method when ¦Ø=1. With 0< ¦Ø<1, it called as under-relaxation methods while w>1 called as over relaxation methods. So, we can choose ¦Ø between 1 and 2. For certain problems, SOR method will be very effective.

The answer for 1st linear system will be [1 1 1]. For the 2nd linear system is [ 1.  -1.   4.  -3.5  7.  -1. ]. These answers had checked by using online matrix calculator. The answers obtained are same for both linear systems.


---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (photo1.tiff)

![photo1.tiff](photo1.tiff)

How many non zero element in $\Sigma$?

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

What is a sparse matrix?
A?matrix?in which number of zero entries are much higher than the number of non zero entries is called sparse matrix. 
-----------------------------------

<sup>last modified: 11/3/2016</sup>
