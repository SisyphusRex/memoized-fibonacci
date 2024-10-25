This program measures the efficiency of algorithms used to create a Fibonacci Sequence.  It tests the effiency of finding nth value or producing a sequence of n length.

The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding numbers.  
              F₀ = 0, F₁ = 1 (initial cases)    
              Fₙ = Fₙ₋₁ + Fₙ₋₂  
              Which produces  
              0 1 1 2 3 5 8 13 ...  

The algorithms used are:
            Iteration    
            Recursion  
            Memoized Recursion  
            Optimized Cache Memoized Recursion  

The program has two main branches.  One branch is the value finder algorithms.  These algorithms return the value of the nth term in the Fibonacci Sequence.  The second branch is the sequence creator algorithms.  These algorithms return a sequence of n terms and are based upon the value finder algorithms.  
  
I began this project in an effort to improve upon a Fibonacci recursive algorithm.  I thought recursion to be very inefficient because it continually calculates values that were previously calculated.  I thought that there has to be a way to store previous solutions and to reference these solutions rather than repeat an entire recursive call tree.  

I eventually arrived at what I now know as Memoization.  Memoization is an optimization technique in which the results of function calls are stored for use in future function calls.  In practice, it requires comparing the argument of a function to a lookup table, or cache, of previously calculated arguments and their values.  If the argument has already been solved, you return the value from the lookup table rather than calculating it from scratch using the function.  
  
While writing my algorithms, I encountered what I thought was a problem with Memoized Recursion.  I use a Python dictionary as the cache and I assumed the worst case efficiency of comparing a value to the dictionary, "if x in y", was O(n) because I thought the function had to iterate over all members of the dictionary to confirm a match.  Upon further research, I discovered that Python's dictionary is essentially a hashmap and uses no iteration.  The average, bigϴ, lookup is ϴ(1).  The Amortized Worst Case is O(n).  
**NOTE** I need to research hashing and hashmaps further to give an accurate bigO of my Memoized Recursion algorithms.  

Before I discovered the hashmap nature of Python dicts, I created the Optimized Cache Memoized Recursion algorithm.  Since Fibonacci requires only two numbers to calculate the next in the sequence, I made the cache delete the rear number before adding one to the front.  The size of the cache is static so it is not affected by n.  Regardless of what the bigO of dict lookup really is, this algorithm's worst case efficiency will not change.  



Calculated BigO (10/23/24):  
*     Value Finder Algorithms:  
        Iteration:  
            O(n)  
                The algorithm moves through n once  
        Recursion:  
            O(2^n)  
                The algorithm doubles its calls with every increase of n  
        Memoized Recursion:  
            **Not Final**  
            O(n): Assumes that dict lookup ϴ(1)  
            O(n^2): Assumes dict lookup O(n)  
        Optimized Cache Memoized Recursion:  
            O(n)  
                Regardless of dict lookup ϴ(1) or O(n) since cache size is constant  
    Sequence Creator Algorithms:  
        Iteration:  
            O(n^2)  
                The algorithm finds the value, O(n), n times.  
            **Note** This should be improved by modifying the return of the Iterative Value Finder algorithm.  Currently, it creates the entire sequence and then returns the value of the last index.  Why not return the sequence?  
            O(n): assumes modified Value Finder return  
        Recursion:  
            O(n2^n)  
            The algorithm mus calculate the value, O(2^n), n times  
        Memoized Recursion:  
            O(n): assumes dict lookup ϴ(1)  
                Each value finder call is O(1) performed n times  
                Since we are repeating the value finder call, we can reuse the cache from the first call and make each value finder call a dict lookup at O(1)  
            O(n^2): assume dict lookup O(n)  
                Again, we are reusing the cache  
        Optimized Cache Memoized Recursion:  
            O(n)  
                Regardless of dict lookup ϴ(1) or O(n) since cache is constant.  








