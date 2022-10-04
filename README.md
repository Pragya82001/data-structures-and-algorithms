# 🗯️Data Structures and Algorithms

## ⏰Time Complexity

**Time complexity is defined in terms of how many times it takes to run a given algorithm, based on the length of the input. Time complexity is not a measurement of how much time it takes to execute a particular algorithm because such factors as programming language, operating system, and processing power are also considered.
Time complexity is a type of computational complexity that describes the time required to execute an algorithm. The time complexity of an algorithm is the amount of time it takes for each statement to complete. As a result, it is highly dependent on the size of the processed data. It also aids in defining an algorithm's effectiveness and evaluating its performance.**

#### Example:  
Suppose a ❔problem is to find whether a pair (X, Y) exists in an array, A of N elements whose sum is Z. The simplest 🤔idea is to consider every pair and check if it satisfies the given condition or not.

The _pseudo-code_ is as follows:

int a[n];
for(int i = 0;i < n;i++)
  cin >> a[i]
  

for(int i = 0;i < n;i++)
  for(int j = 0;j < n;j++)
    if(i!=j && a[i]+a[j] == z)
       return true

return false

**Python Code of the above _pseudo-code_**

def findPair(a, n, z) :
     
    # Iterate through all the pairs
    for i in range(n) :
        for j in range(n) :
 
            # Check if the sum of the pair
            # (a[i], a[j]) is equal to z
            if (i != j and a[i] + a[j] == z) :
                return True
 
    return False
 
<!-- Driver Code 
 
 Given Input -->
a = [ 1, -2, 1, 0, 5 ]
z = 0
n = len(a)
 

if (findPair(a, n, z)) :
    print("True")
else :
    print("False")
    
## 🥡OUTPUT - False

_Assuming that each of the operations in the computer takes approximately constant time, let it be c. The number of lines of code executed actually depends on the value of Z. During analyses of the algorithm, mostly the worst-case scenario is considered, i.e., when there is no pair of elements with sum equals Z. In the worst case, 

N*c operations are required for input.
The outer loop i loop runs N times.
For each i, the inner loop j loop runs N times.
So total execution time is **N*c + N*N*c + c**. Now ignore the lower order terms since the lower order terms are relatively insignificant for large input, therefore only the highest order term is taken (without constant) which is N*N in this case. Different notations are used to describe the limiting behavior of a function, but since the worst case is taken so big-O notation will be used to represent the time complexity.

Hence, the time complexity is **O(N2)** for the above algorithm. Note that the time complexity is solely based on the number of elements in array A i.e the input length, so if the length of the array will increase the time of execution will also increase.

Order of growth is how the time of execution depends on the length of the input. In the above example, it is clearly evident that the time of execution quadratically depends on the length of the array. Order of growth will help to compute the running time with ease._

## 👾Space Complexity

**When an algorithm is run on a 💻computer, it necessitates a certain amount of 📝memory space. The amount of memory used by a program to execute it is represented by its space complexity. Because a program requires memory to store input data and temporal values while 🏃running, the space complexity is auxiliary and input space.**

#### Example:
Suppose a ❓problem to 👓find the frequency of array elements.

The _pseudo-code_ is as follows: 

int freq[n];
int a[n];

for(int i = 0; i<n; i++)
{
   cin>>a[i];
   freq[a[i]]++;
}  

**Python Code of the above _pseudo-code_**

def countFreq(arr, n):
    freq = dict()
     
    # Traverse through array elements and
    # count frequencies
    for i in arr:
        if i not in freq:
            freq[i] = 0
        freq[i]+=1
         
    # Traverse through map and print frequencies
    for x in freq:
        print(x, freq[x])
 
arr =  [10, 20, 20, 10, 10, 20, 5, 20 ]
n = len(arr)
countFreq(arr, n)

## 🥡OUTPUT - 
              5 1
              10 3
              2  4
              
_Here two arrays of length N, and variable i are used in the algorithm so, the total space used is **N * c + N * c + 1 * c = 2N * c + c**, where c is a unit space taken. For many inputs, constant c is insignificant, and it can be said that the space complexity is **O(N)**.
There is also auxiliary space, which is different from space complexity. The main difference is where space complexity quantifies the total space used by the algorithm, auxiliary space quantifies the extra space that is used in the algorithm apart from the given input. In the above example, the auxiliary space is the space used by the freq[] array because that is not part of the given input. So total auxiliary space is **N * c + c** which is **O(N)** only._

## How to calculate time-complexity❓

Time complexity estimates the time to run an algorithm. It's calculated by counting elementary operations.
_Let's take an example and analyze the time-complexity in detail_

<!-- Compute the maximum element in the array a -->
Algorithm max(a):
    max ← a[0]
    for i = 1 to len(a)-1
        if a[i] > max
            max ← a[i]
    return max
    
*The answer depends on factors such as input, programming language and runtime, coding skill, compiler, operating system, and hardware.

*We often want to reason about execution time in a way that depends only on the algorithm and its input. This can be achieved by choosing an elementary operation, which the algorithm performs repeatedly, and define the time complexity T(n) as the number of such operations the algorithm performs given an array of length n.

*For the algorithm above we can choose the comparison a[i] > max as an elementary operation.
  *This captures the running time of the algorithm well, since comparisons dominate all other operations in this particular algorithm.
  *Also, the time to perform a comparison is constant: it doesn’t depend on the size of a.
  
The time complexity, measured in the number of comparisons, then becomes T(n) = n - 1.

*In general, an elementary operation must have two properties:
  *There can’t be any other operations that are performed more frequently as the size of the input grows.
  *The time to execute an elementary operation must be constant: it mustn’t increase as the size of the input grows. This is known as unit cost.
  
## How to calculate space-complexity❓

*Whenever we write an algorithm or code and run it in our computational device then it requires some space in our device to be executed. The memory here are required for storing the variables, data, temporary results, constants and many more.

*Calculation and analyzing of this space complexity is important because in real world applications developers are bounded/limited to acquire the memory in the devices. The calculation of the space complexity also helps the developer to know about the worst case of that algo so as to improve that algo to perform in the worst case also.

*There is a sort of confusion among people between the space complexity and the auxiliary space. So let’s be clear about that, so auxiliary space is nothing but the space required by an algorithm/problem during the execution of that algorithm/problem and it is not equal to the space complexity because space complexity includes space for input values along with it also.

  *So we can say that space complexity is the combination or sum up of the auxiliary space and the space used by input values.

**Space Complexity = Auxiliary Space + Space used for input values**
Let's take an example:

    #Sum Of N Natural Number
    int sum(int n)
    {
     int i,sum=0;
     for(i=n;i>=1;i--)
     sum=sum+i
     return sum;
    }
So in the above example input value is 'n' that is constant which will take the space of **O(1)**. Now what about auxiliary space, so it is also O(1) becuase 'i' and 'sum' are also constants.
**Hence total space complexity is O(1).**

Let's take another example:
_Sum of all elements in an array_

  function sum_of_numbers(arr[],N){
      sum=0
      for(i = 0 to N){
        sum=sum+arr[i]
      }
      print(sum)
  }
So here this time there is an algorithm to find the sum of all elements in the array. For that we are passing the array(arr[ ]) and the size of array(N) to the created function. So here,

*In array(arr) the size of array is "N" and each element will take "4bytes" so the space taken by "arr" will be "N * 4 bytes"
*"sum" variable stores the sum of all elements and it will take "4 bytes" of space.
*"i" variable is used to iterate over all the elements in the array and it will also take "4 bytes" of space.
*Now function call, initialisation of for loop and print function these all comes under the auxiliary space and lets assume these all will take combinely "4 bytes" of space.

Hence, **Total space complexity= (4*N + 12)bytes** But these 12 bytes are constant so we will not consider it and after removing all the constants **(4 from 4*N)** we can finally say that this algo have a complexity of **"O(N)"**.

Where the N varies according the size of the input array.

# Time Complexity and Space Complexity For Some Common Algorithms 
![1_8CwawEIoG9VoineE0Rc0qw](https://user-images.githubusercontent.com/100519291/193776562-4343d77c-a1d4-442a-9554-1b0b686d691b.png)
