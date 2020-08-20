WARNING: This library requires python 3.8

# Fastprocess
A fast subprocess library

## Usage
Spawning a process with fastprocess is very easy
```
In [1]: from fastprocess import FastProcess

In [2]: pid = FastProcess(['echo', 'hello', 'world'])

hello world
In [3]: pid.wait()
Out[3]: 0

```
You can redirect io using the stdin, stdout, and stderr options
```
In [4]: null = open('/dev/null', 'w')

In [5]: pid = FastProcess(['yes'], stdout=null)

In [6]: pid.terminate()
```

## FastProcess methods
terminate():  
Sends SIGTERM to the process

kill(sig):  
Sends signal 'sig' to the process

wait():  
Waits for the process to exit then returns the exit code

## Performance
Here are the results of running ./benchmark/bench
```
---------------------------------------------------
10000 spawns with fork and exec...

real	0m2.181s
user	0m0.116s
sys	0m2.056s
---------------------------------------------------
10000 spawns with fastprocess (posix_spawn)...

real	0m2.587s
user	0m1.150s
sys	0m0.438s
---------------------------------------------------
10000 spawns with old fastprocess (fork/exec)...

real	0m3.668s
user	0m0.440s
sys	0m3.223s
---------------------------------------------------
10000 spawns with subprocess...

real	0m12.134s
user	0m7.768s
sys	0m9.108s
---------------------------------------------------
```
