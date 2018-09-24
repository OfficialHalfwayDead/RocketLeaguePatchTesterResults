# Numdiffs for 1.52 vs 1.53

The script accepts an argument to specify the absolute tolerance passed to numdiff:

```
./getresults.sh 0.01
```

I have included the equal/different lists of files for 0.01 and 1.00 for reference.

These were created like so:

```
./getresults.sh 1.00 | grep equal >  1.00/equal.txt
./getresults.sh 1.00 | grep differs > 1.00/different.txt
./getresults.sh 0.01 | grep equal >  0.01/equal.txt
./getresults.sh 0.01 | grep differs >  0.01/different.txt
```
