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

real	0m3.021s
user	0m0.151s
sys	0m1.420s
---------------------------------------------------
10000 spawns with fastprocess (posix_spawn)...

real	0m3.240s
user	0m1.746s
sys	0m0.265s
---------------------------------------------------
10000 spawns with old fastprocess (fork/exec)...

real	0m3.624s
user	0m0.863s
sys	0m2.738s
---------------------------------------------------
10000 spawns with subprocess...

real	0m10.873s
user	0m4.902s
sys	0m9.480s
---------------------------------------------------
```
