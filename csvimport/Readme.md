# csv to cayley api

## Run cayley
Download from [here](https://github.com/cayleygraph/cayley/releases)
```bash
$ ./cayley init -db leveldb -dbpath ./db1
$ ./cayley http --db leveldb --dbpath ./db1 --host 0.0.0.0 --port 64210
```

## Run importer
``` bash
$ cd csvimport
$ go build
$ ./csvimport -file PATHTOFILE - user USERID -host http://127.0.0.1:64210
```
