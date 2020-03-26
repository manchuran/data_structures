# Data Structures

I have been examining nested lists after reading up recursion in _How to Think like a Computer Scientist: Learning with Python 3 Documentation_ by Peter Wenthworth, Jeffrey Elkner, Allen B. Downey and Chris Meyers.

In their example on recursive data structures, they examined a function which calculated the sum of numbers in a nested list, i.e. a list which may contain any of a number, another list, or an empty list.

Though one could use a for loop in tackling such a list, recursion is much more ideally suited for this problem. For my own solution, I examined an alternative recursive approach and another different one-line technique which employed list comprehension.

## Solution 1

Solution 1 is offered in the text book. It uses a recursive function and a for loop.

```python
def r_sum(nested_num_lst):
    tot = 0
    for element in nested_num_lst:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot
```

For `b` expressed as:
```
b = [[7000,[415,[],321],5],6,21,9,[20,32,4],[],[12, [345,[900,12040]],12],11,[0,[],2400,5],19]
```
`r_sum` provides a correct answer of `23577`

The function produces a `%timeit` output of `5.26 µs ± 135 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)`


## Solution 2
One of the solutions I created follows nearly after the pattern of Solution 1, but explicitly begins from the first item in the nested list.

```python
def nested_list_sum(lst):
    '''
    Calculate sum of a nested list
    Input: Nested list (Lists)
    Output: Sum (Integer)
    '''
    
    if lst == []:
        return 0
    if type(lst[0]) is list:
        lst[0] = nested_list_sum(lst[0])
    return lst[0] + nested_list_sum(lst[1:])
```

For the same `b` it produces a `%timeit` output of `8.6 µs ± 301 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)`

## Solution 3
An alternative solution converts the whole list to string, strips it and then convert the numbers back to integer (or float) types as may be required. I have used integer in this case.

```python
def nested_list_sum2(nested_list):
    '''
    Calculate sum of a nested list
    
    Input: Nested List (Lists)
    Output: Sum (Integer)
    
    '''
    
    return sum([int(item.strip('[ [] ]')) 
                for item in str(nested_list).split(',') 
                if item.strip() != '[]'])
```

For the same `b` it produces a `%timeit` output of `10.3 µs ± 255 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)`

Though their speed are comparable to the original, both turn out to be not as fast as. Solution 3, however, is quite unique in its employment of the `split` and `strip` functions in solving the problem.
