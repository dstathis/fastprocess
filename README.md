# Fastprocess
A fast subprocess library

## Usage
Spawning a process with fastprocess is very easy
```
In [1]: from fastprocess import Fp                                                                       

In [2]: pid = Fp(['echo', 'hello', 'world'])                                                             

hello world
In [3]: pid.wait()                                                                                       
Out[3]: 0

```
You can redirect io using the stdin, stdout, and stderr options
```
In [4]: null = open('/dev/null', 'w')                                                                    

In [5]: pid = Fp(['yes'], stdout=null)                                                                   

In [6]: pid.terminate()
```

## Fp methods
terminate():  
Sends SIGTERM to the process

kill(sig):  
Sends signal 'sig' to the process

wait():  
Waits for the process to exit then returns the exit code

## Performance
Here are the results of running ./benchmark/bench
```
---------------------------------------
10000 spawns with fork and exec...

real	0m2.214s
user	0m0.083s
sys	0m2.123s
---------------------------------------
10000 spawns with fastprocess...

real	0m3.163s
user	0m0.383s
sys	0m2.772s
---------------------------------------
10000 spawns with subprocess...

real	0m11.110s
user	0m6.773s
sys	0m7.772s
---------------------------------------
```
