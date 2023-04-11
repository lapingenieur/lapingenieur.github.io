#!/bin/env python
from sys import argv
import re

class Version:
    version=(0,0,1)
    pretty=None
    def pretty(self):
        if not self.pretty:
            self.pretty=".".join((str(x) for x in self.version))
        return self.pretty

class Cache:
    v=Version()
    asmv=None
    sec=None
    ifile=[]
    ofile=None
cs=Cache

class Myword:
    def __init__(self,list):
        if len(list)==0:
            self.list=None
        else:
            self.list=list
            self.point=None
    def p(self):
        if self.point==None:
            self.point=0
        return self.point
    def get(self):
        return self.list[self.p()]
    def next(self):
        if self.isnext():
            if self.point==None:
                self.point=0
            else:
                self.point+=1
            return self.get()
        else:
            return False
    def isnext(self,n=1):
        if self.point==None or len(self.list)>self.point+n:
            return True
        return False

class Array:
    def __init__(self):
        self.list=[]
    def add(self,*a):
        for i in a:
            self.list.append(i)
    def pop(self,*a):
        return [self.list.pop(x) if len(self.list)>x else None for x in a]

### UTILS

def fmt(t, *a):
    return t.format(*a)
def pfmt(t, *a):
    print(fmt(t, *a))

def arr(msg, line, *a): # asm code error
    sec=fmt(" of section '{}'",cs.sec) if cs.sec else ""
    return fmt("Assembly error at line {}{}: {}",line,sec,fmt(msg,*a))

### COMPILERS

def cp_x800(contents):
    ops=Array() # temporary ops array: $XX for raw hex, >XXXX for vector origins, .XXXX for vector pointers, @XX address origin
    contents=contents.split("\n")
    for i in range(len(contents)):
        line=contents[i]
        words=Myword(line.split(" "))
        if words.list==None:
            continue

        #pfmt("line '{}': '{}'",i,line)
        
        wcls=0 # argument number to read, 0=none or opcode
        wtpe=0 # special word, for compiler operations ; 0=normal, 1=address origin, 2=add/sub lib
        while True:
            if not words.isnext():
                break
            w=words.next().lower()

            #pfmt("word '{}', {}",w,words.isnext())
            #print(words.list, words.point)
            
            if w=="":
                continue
            elif w[0]==";":
                break
            elif wcls==0:
                if w in ("nop", "tab", "add", "sub"):
                    wcls=0 # default is 1 more ARG
                else:
                    wcls=1

                if w=="nop":
                    ops.add("$00")
                elif w=="lda":
                    ops.add("$01")
                elif w=="lia":
                    ops.add("$02")
                elif w=="sta":
                    ops.add("$03")
                elif w=="ldb":
                    ops.add("$04")
                elif w=="lib":
                    ops.add("$05")
                elif w=="tab":
                    ops.add("$06")
                elif w in ("add", "sub"):
                    if words.isnext():
                        y=words.list[words.point+1]
                        if y[0]=="$":
                            words.next()
                            if len(y)>1:
                                try:
                                    int(y[1:],16)
                                    ops.add("$05",fmt("${}",int(y[1:],16)))
                                except ValueError:
                                    raise ValueError(fmt("Not a hex number '{}' in line {}: '{}'",y,i,line))
                            else:
                                raise ValueError(fmt("Not a hex number '{}' in line {}: '{}'",y,i,line))
                        elif y.isnumeric():
                            words.next()
                            ops.add("$05",fmt("${}",int(y)))
                        elif y[0]==".":
                            words.next()
                            ops.add("$05",fmt(".{}",y[1:]))
                    if w=="add":
                        ops.add("$07")
                    else:
                        ops.add("$08")
                elif w=="jmp":
                    ops.add("$09")
                elif w=="jsr":
                    ops.add("$10")
                    wcls=2
                elif w=="rts":
                    ops.add("$11")
                elif w=="brz":
                    ops.add("$12")
                elif w=="brc":
                    ops.add("$13")

                elif w[-1]==":":
                    ops.add(fmt(">{}",w[:-1]))
                    wcls=0
                elif w==".word":
                    continue
                elif w==".at":
                    wtpe=1
            else:
                wcls-=1
                
                if w[0]=="$":
                    if len(w)>1:
                        try:
                            int(w[1:],16)
                            ops.add(fmt("{}{}",("$","@")[wtpe],int(w[1:],16)))
                        except ValueError:
                            raise ValueError(fmt("Not a hex number '{}' in line {}: '{}'",w,i,line))
                    else:
                        raise ValueError(fmt("Not a hex number '{}' in line {}: '{}'",w,i,line))
                elif w.isnumeric():
                    ops.add(fmt("{}{}",("$","@")[wtpe],int(w)))
                elif w[0]==".":
                    ops.add(fmt(".{}",w[1:]))
                else:
                    raise Exception(fmt("Unknown argument '{}' in line {}: '{}'",w,i,line))

                wtpe=0
        if wcls>0:
            raise Exception(fmt("{} missing argument/s in line {}: '{}'",wcls,i,line))
    
    print(ops.list)

    i=0
    vec={}
    out=bytearray(2048)

    for a in ops.list:
        if a[0]=="@":
            i=int(a[1:],16)
        elif a[0]==">":
            if a[1:] not in vec:
                vec[a[1:]]=i
            else:
                raise Exception(fmt("There's already a definition for pointer '{}'",a[1:]))
        elif a[0] in ("$", "."):
            if len(out)>i:
                i+=1
            else:
                raise Exception(fmt("Outfile is smaller than index {}: {} bytes",i,len(out)))
    
    print(vec)

    i=0
    for a in ops.list:
        if a[0]=="@":
            i=int(a[1:],16)
            ops.pop(i)
        elif a[0]==".":
            if a[1:] in vec:
                out[i]=vec[a[1:]]
                i+=1
            else:
                raise Exception(fmt("Undefined vector called: '{}'",a[1:]))
        elif a[0]=="$":
            if len(out)>i:
                out[i]=int(a[1:])
                i+=1
            else:
                raise Exception(fmt("Outfile is smaller than index {}: {} bytes",i,len(out)))
    return out

### ARGUMENTS

def nopar(argv,i,n=1):
    if len(argv)<=i+n:
        raise Exception(fmt("Lacks a parameter for argument {}: '{}'",i,argv[i]))

acls=0
i=0
while True:
    i+=1
    if len(argv)<=i:
        break

    a=argv[i]
    if a in ("--version"):
        pfmt("LP assembly compiler - v{}",cs.v.pretty())
    elif a in ("-s", "--section"):
        nopar(argv,i)
        i+=1
        cs.sec=argv[i]
    elif a in ("-i", "--infile"):
        nopar(argv,i)
        i+=1
        cs.ifile.append(argv[i])
    elif a in ("-o", "--outfile"):
        nopar(argv,i)
        i+=1
        cs.ofile=argv[i]
    elif a in ("-n", "--no-output"):
        cs.ofile=False
    elif a[0]!="-":
        cs.ifile.append(a)
    else:
        raise Exception(fmt("Unknown argument {}: '{}'",i,a))

del nopar, acls, i

### RUN

for f in cs.ifile:
    out=bytearray()
    with open(f, "r") as ifile:
        contents = ifile.read()
        ifile.close()
        
        if cs.asmv==None:
            found=re.search("^ *; *! *LP *",contents)
            if found:
                t=contents.split("\n")[0]
                cs.asmv=re.findall("^\w+",t[found.span()[1]:])[0]
            else:
                raise Exception("No assembly revision specified")

        if cs.sec:
            # beg
            found=re.search(fmt("(?m)^ *; *! *sec +beg +{} *$",cs.sec), contents)
            if not found:
                raise Exception(fmt("No '{}' section in '{}' file", cs.sec, f))
            else:
                contents=contents[found.span()[1]:]
            # end
            found=re.search(fmt("(?m)^ *; *! *sec +end +{} *$",cs.sec), contents)
            if found:
                contents=contents[:found.span()[0]]
            tmp=fmt("section '{}' of ",cs.sec)
        else:
            tmp=""
        pfmt("Compiling {}file '{}' with {} assembly",tmp,f,cs.asmv)

        if cs.asmv=="x800":
            out+=cp_x800(contents)
        else:
            raise Exception(fmt("No compiler found for '{}'",cs.asmv))

    if cs.ofile!=False:
        if cs.ofile==None:
            tmp=fmt("{}.{}",re.sub("\.[^\.]+$","",f),cs.asmv)
        else:
            tmp=cs.ofile
        with open(tmp,"w+b") as g:
            g.write(out)
            pfmt("Wrote to file '{}'",tmp)
