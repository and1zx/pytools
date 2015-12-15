# pytools
specific tools for self-use

* allssh/allscp
    for distribute deployment use, 
    usage `allssh -f hostname_file "cmd"`
    or    `allscp -f hostname_file src_file dst`
* calc
    a simple cmdline calculater, add to path first, set `chmod +x calc`, 
    usage `calc "1+2**5"`
* randline
    get random lines from a huge stdin input, 
    usage `cat huge_file.txt|python randline.py 100`
    or    `randline 100 huge_file.txt`
* lz_tools.py
    stdin_reader: cluster stdin inputs by key, for mapreduce uses
