## Introduction
Decorators are a powerful feature in Python, allowing you to wrap a function and modify its behavior. This script introduces a cache decorator that stores the results of function calls and returns the cached result if the same inputs are provided again.

## Installation
To use this script, you need to have Python installed on your system. The script uses the time module, which is included in Python’s standard library, so no additional installations are required.

## Clone this repository or download the script.
Ensure Python is installed on your system (Python 3.x recommended).

## Usage
You can use the cache decorator to cache the results of any function. Simply apply the @cache decorator above the function definition.

## Example
In this example, the sum_func function is decorated with the cache decorator. The first time the function is called with the arguments (2, 3), it takes 5 seconds to execute because of the time.sleep(5) delay. The result is then stored in the cache. When the function is called again with the same arguments, the cached result is returned immediately without delay. A different set of arguments, such as (4, 9), will cause the function to execute again and cache the new result.

## Output
When you run the script, it will output something similar to:
{}
10
10
13

The empty dictionary {} is printed initially when the cache decorator is first created.
The first print(sum_func(2,3)) call takes 5 seconds to return 5.
The second print(sum_func(2,3)) call returns immediately with the cached result.
The print(sum_func(4,9)) call also takes 5 seconds since these arguments were not cached yet.

## Explanation
# cache decorator: This decorator uses a dictionary (cache_value) to store the results of function calls. The keys are the arguments passed to the function, and the values are the results. If the same arguments are passed again, the cached result is returned.
# time.sleep(5): This line in the sum_func function simulates a time-consuming operation by delaying the function's execution for 5 seconds.

