version = "2.2"

def text2ascbin(text, allone=False, justify=False):
    # give this a text string and it converts it to binary ascii as a list of list of bool (note! in fact returns its unicode code)
    # allone: bool, merge every character's code into one unique bool chain
    # justify: bool, default to 8-bit ascii length, fills in front with False if leaks, panics if more than 8 bits set
    asc=[]
    for c in text:
        t=[True if x=="1" else False for x in bin(ord(c))[2:]]
        if justify:
            if len(t)>8:
                raise Exception("Justify set but too long length for this character to be ascii: {} ({})\n\"=> code: {}".format(c, len(t), t))
            while len(t)<8:
                t.insert(0, False)
        if allone:
            for x in t:
                asc.append(x)
        else:
            asc.append(t)
    return asc

def ascbin2text(inc, nofail=False):
    # give this a string of 0/1 or an array/tuple of bool of binary ascii (note! ascii but NOT unicode) and it converts it a string of text
    # nofail: bool, don't fail if receives an incorrect ascii binary

    def bool2str(l):
        # converts a list of bool into a string of 0/1 so int isn't lost
        t=""
        for i in l:
            t+="1" if i else "0"
        return t
    
    if len(inc)%8!=0 and not nofail:
        raise Exception("Input ascii length must be divisible by 8 : {}%8 == {}".format(len(inc), len(inc)%8))
    if type(inc)==list or type(inc)==tuple:
        inc=bool2str(inc)

    out=""
    for i in range(0, len(inc), 8):
        out+=chr(int(inc[i:i+8], 2))
    if nofail and len(inc)>=0:
        print("ascbin2text/log: {} binary values remain undecoded: '{}'".format(len(inc), inc))
    return out

def mendbin(inc, concat=True):
    # mends an incoming array of arrays of booleans so it perfectly fits ascii needs and can be written without woory
    # inc: array of arrays(len<=8) of booleans, incoming data to mend
    # concat: boolean, concats all the arrays of the data array into a single array so it can be directly passed to write()
    # \ otherwise (false) the array of arrays of booleans is returned as is

    out=[]
    if concat: # conditionnally define add() wether it needs to concat arrays or not
        def add(chunk, out):    # note: here out was stated 'outbound' but it shouldn't... so let's just give it as an mutable argument
            out+=chunk
    else:
        def add(chunk, out):
            out.append(chunk)

    for i in range(len(inc)):
        if len(inc[i])>8:
            raise Exception("This chunk is longer than 8 bits! at position {}: '{}'".format(i, inc[i]))
        for _ in range(len(inc[i]), 8):
            inc[i].insert(0, False)
        add(inc[i], out)
    return out

def write(image, value, autoconvert=True, log=False):
    # image: incoming image in RGB mode
    # values: array/tuple of bool, incoming binary values to store in the image
    # autoconvert: boolean, allow converting automatically incoming image to rgb using PIL.Image.Image.convert("RGB")

    def code(p, arg=False):
        # p: RGB value of a pixel in which to store 2 values
        # arg: either bool or (a, b) where a bool value 1 and b bool value 2 of the 2 values to stock in p
        if arg:
            if type(arg[0])!=bool or type(arg[1])!=bool:
                return False
            a=p[1]//2*2
            b=p[2]//2*2
            if not arg[0]:
                a+=1
            if not arg[1]:
                b+=1
            return (p[0]//2*2, a, b)
        else:
            return (p[0]//2*2+1, p[1], p[2])

    if not image.mode == "RGB":
        if autoconvert:
            try:
                print("info: auto-converting input image from {} to RGB...".format(image.mode))
                image=image.convert("RGB")
            except ValueError as e:
                raise Exception("Failed auto-converting image from mode '{}': {}".format(image.mode, e))
        else:
            raise Exception("Image needs to be in RGB mode: '{}'".format(image.mode) + " (try using PIL.Image.Image.convert('RGB'))")
    if type(value)==tuple or type(value)==list:
        if len(value)%2==1:
            value.append(False)
            if log:
                print("added a False to the value to encode to fill the last encoded pixel")
    else:
        raise Exception("Value argument must be an array or a tuple of bools")

    if image.size[0]*image.size[1] <= len(value):
        raise Exception("Image is smaller than text length")

    i=0
    if log:
        print("starting writing to image")
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            c=image.getpixel((x, y))
            if i < len(value):
                c=code(c, (value[i],value[i+1]))
                if c:
                    if log:
                        print("for value", (value[i], value[i+1]), "and pixel", image.getpixel((x, y)), "wrote", c, "at", (x, y))
                else:
                    raise Exception("Encoding to pixel failed for values {}: {}".format((i, i+1), (value[i], value[i+1])))
            else:
                c=code(c)
            image.putpixel((x, y), c)
            i+=2

    if log:
        print("finished writing to image")
    return image

def read(image, autoconvert=True, log=False):
    # image: incoming image in RGB mode
    # log: bool, logging
    # autoconvert: boolean, allow converting automatically incoming image to rgb using PIL.Image.Image.convert("RGB")

    def code(p):
        # returns a tuple of the inner pixel's value
        # p: RGB value of a pixel in which to store 2 values
        v=False
        if p[0]%2==0:
            a=True if p[1]%2==0 else False
            b=True if p[2]%2==0 else False
            v=(a, b)
        return v

    if not image.mode == "RGB":
        if autoconvert:
            try:
                print("info: auto-converting input image from {} to RGB...".format(image.mode))
                image=image.convert("RGB")
            except ValueError as e:
                raise Exception("Failed auto-converting image from mode '{}': {}".format(image.mode, e))
        else:
            raise Exception("Image needs to be in RGB mode: '{}'".format(image.mode) + " (try using PIL.Image.Image.convert('RGB'))")
    if log:
        print("starting reading from image")
    out=[]
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            c=image.getpixel((x, y))
            p=code(c)
            if p:
                out.append(p[0])
                out.append(p[1])
                if log:
                    print("for pixel", c, "at", (x, y), "read value", p)

    if log:
        print("finished reading from image")
    return out
