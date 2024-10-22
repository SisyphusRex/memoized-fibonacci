This program produces Fibonacci sequences through different methods and displays the statistics used to evaluate bigO notation.

The program can produce a Fibonacci sequence through iteration, recursion, memoized recursion, and **PLANNED** optimized cache memoized recursion.

The program can display the run time and the approximate worst case amount of processes a function takes to produce a Fibonacci sequence.

So far, I have calculated sequence_creator:
    Iteration: O(n^2)
        One for loop iterating over n, done n times
    Recursion: O(n2^n)
        performing recursive value finder n times
    Memoized Recursion: O(n^2)
        basically iterating over an n length cache, n times
    Optimized Cache Memoized Recursion: **Projected** O(n)

 Since I am calculating the bigO of creating a Fibonacci sequence and not just finding the value of nth term, one
can determine the bigO of each value finding method by dividing the previous bigOs by n (since each value finder must be
repeated n times to create a sequence) EXCEPT for Optimized Cache Memoized Recursion.

value_finder bigO:
    Iteration: O(n)
    Recursion: O(2^n)
    Memoized Recursion: O(n)
    Optimized Cache Memoized Recursion: STILL O(n)

Optimized Cache Memoized Recursion stays the same because I plan to modify the look-up table, or cache, within the value finder
to only holding the two previous n values rather than the entire fibonacci sequence cache.  To find a value at n, I only need
to know n-2 and n-1.  I know my sequence_creator function is going from least to greatest.  Thus, rather than iterating
over the entire sequence cache (which at worst is length n), I just have to iterate over a cache of constant length 2!  While this
decreases the sequence_creator bigO to linear (because we no longer have to iterate over n n times, but 2 n times), we still have to
create the cache about n times to find a single value if not part of a larger sequence.  NOTE: This is similar to creating a linked-list
that moves the head and tail each time.
