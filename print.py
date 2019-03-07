
def append(filename,data):
    f= open(filename,"a+")
    f.write(data)
    f.close()


def indentcode(indent,data):
    for i in range(indent):
        data = "\t" + data
    return data    
