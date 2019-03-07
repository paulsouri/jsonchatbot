import json
from models import Statement, VarCapture, VarOptions, Condtional, Evaluate, Substiute, Print

config = json.loads(open('config/defaults.json').read())
globals = {}

def generate_file(questions,filename):
    i = 0
    for question in questions:
        i = i + 1
        if (len(question) == 1) & (question.get("instruction") is not None):
            Statement(question.get("instruction")).append(filename,0)
        elif (len(question) == 2) & (question.get("text") is not None) & (question.get("var") is not None):
            VarCapture(question.get("text"),question.get("var")).append(filename,0)
        elif (len(question) == 3) & (question.get("text") is not None) & (question.get("var") is not None) & (question.get("options") is not None):
            VarOptions(question.get("text"),question.get("var"),question.get("options")).append(filename,0)
        elif (len(question) == 3) & (question.get("text") is not None) & (question.get("var") is not None) & (question.get("conditions") is not None):
            Condtional(question.get("text"),question.get("var"),question.get("conditions")).append(filename,0)
        elif (len(question) == 3) & (question.get("formula") is not None) & (question.get("var") is not None) & (question.get("calculated_variable") is not None):
            Evaluate(question.get("calculated_variable"),question.get("var"),question.get("formula")).append(filename,0)
        elif (len(question) == 2) & (question.get("instruction") is not None) & (question.get("instruction_var") is not None):
            Substiute(question.get("instruction"),question.get("instruction_var")).append(filename,0)
        elif (len(question) == 4) & (question.get("list_var") is not None) & (question.get("list_length") is not None) & (question.get("instruction") is not None) & (question.get("instruction_var") is not None):
            Print(question.get("list_var"),question.get("list_length"),question.get("instruction"),question.get("instruction_var")).append(filename,0)
        else:
            print("Problem in JSON file")

if (__name__ == '__main__'):
    APP_NAME = config.get("function")
    QUESTIONS = config.get("questions")
    filename = "output/%s.py"%APP_NAME
    f = open(filename, "w")
    f.write("\n")
    f.close()
    if not isinstance(APP_NAME,str):
        raise Exception('The name of the function should be in string format.')
    generate_file(QUESTIONS,filename)
