from print import append, indentcode


class Statement:
    def __init__(self, instruction):
        self.instruction = instruction
    def append(self,filename,indent):
        data = ""
        data = indentcode(indent,data) + 'print("%s")\n'%self.instruction
        append(filename,data)

class VarCapture:
    def __init__(self, text, var):
        self.text = text
        self.var = var
    def append(self,filename,indent):
        data = ""
        data = indentcode(indent,data) + 'print("%s")\n'%self.text
        data = indentcode(indent,data) + '%s = input()\n'%self.var
        append(filename,data)

class VarOptions:
    def __init__(self, text, var, options):
        self.text = text
        self.var = var
        self.options = options
    def append(self,filename,indent):
        data = ""
        data = indentcode(indent,data) + 'print("%s")\n'%self.text
        data = indentcode(indent,data) + 'print("%s")\n'%self.options
        data = indentcode(indent,data) + '%s = input()\n'%self.var
        append(filename,data)

class Condtional:
     def __init__(self, text, var, conditions):
         self.text = text
         self.var = var
         self.conditions = conditions

     def append(self,filename,indent):
        data = ""
        data = indentcode(indent,data) + 'while %s :\n'%str(self.conditions[0][0])
        data = indentcode(indent,data) + '\tprint("%s")\n'%self.text
        data = indentcode(indent,data) + '\t%s = input()\n'%self.var
        append(filename,data)

class Evaluate:
    def __init__(self, calculated_variable, var, formula):
        self.calculated_variable = calculated_variable
        self.var = var
        self.formula = formula

    def append(self,filename,indent):
        data = ""
        if self.calculated_variable:
            data = indentcode(indent,data) + '%s = %s\n'%(self.var,self.formula)
        append(filename,data)

class Substiute:
    def __init__(self, instruction, instruction_var):
        self.instruction = instruction
        self.instruction_var = instruction_var
    def append(self,filename,indent):
        data = ""
        placeholder = "%("
        for var in self.instruction_var:
            placeholder = placeholder + "%s,"%var
        placeholder = placeholder[:-1] + ")"
        data = indentcode(indent,data) + 'print("%s"%s)\n'%(self.instruction,placeholder)
        append(filename,data)

class Print:
    def __init__(self, list_var, list_length, instruction, instruction_var):
        self.list_var = list_var
        self.list_length = list_length
        self.instruction = instruction
        self.instruction_var = instruction_var
    def append(self,filename,indent):
        data = ""
        if self.list_var:
            data = indentcode(indent,data) + 'for i in range (%s):\n'%self.list_length
            placeholder = "%("
            for var in self.instruction_var:
                placeholder = placeholder + "%s,"%var
            data = indentcode(indent,data) + '\tprint("%s"%s)\n'%(self.instruction,placeholder[:-1]+")")
        append(filename,data)
