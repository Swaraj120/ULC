def varmap(targetVar, state):
    if targetVar in state:
        return state[targetVar]
    else:
        raise ValueError("Error: Var not found")
    
    
    

def parse(function):
    opslist = {"+", "-", "*", "/", "%"}     #listing the operations
    

    for operation in opslist: #loops through opslist
        if operation in function:      # see if the symbol of operation is in
            value1, value2 = function.split(operation) # when you see an operation split the function into val1 and val2 
               
            if operation == "+":
                return int(parse(value1)) + int(parse(value2))       #need to specify int won't work on floats
            elif operation == "-":
                return int(parse(value1)) - int(parse(value2))
            elif operation == "*":
                return int(parse(value1)) * int(parse(value2))
            elif operation == "/":
                return int(parse(value1)) / int(parse(value2))
            elif operation == "%":
                return int(parse(value1)) % int(parse(value2))
    return int(function.strip())






DataTypes = {
     'short int', 'Int', 'Long int', 'double', 'Long double', 'String'
}





def executeProgram(program, state={}):
    
    
    for line in program.splitlines():          # each line in the program gets split into their own line
        
        
        line = line.strip()
        if not line:
            continue                                             # was not allowing me to put any of the Instructions past the first line.
        statements = line.split(maxsplit=1)
        if len(statements) != 2:
            continue
        instruction, expression = statements
        

        if instruction == "INTRODUCING":                        #instructions will be the more generic logic #expression will require more logic
            variable, value = expression.split('=')         # in this instance we're splitting up expression and saying left side is variable so for first case Y and right side is value 5 this split occurs when we see a =
            state[variable.strip()] = parse(value)
            
        
            
        elif instruction == "ANOUNCING":
            try:
                value = varmap(expression, state)
                print(value)
            except ValueError as e:
                print(e)
                
                
                

        elif instruction == "IF":                               # rather than making a function specified for IF I built it into the main program cause the other way was not working
            condition, code = expression.split(":")               #split the statement into a condition (X<10) and a code which is executed like x<10 -> print(Hello)
            condition = condition.strip()
            

            
            if "<" in condition:                                #look for a less than sign
                variable, value = condition.split("<")          #if exists split the conditional segment of the code into a variable and value
                if variable.strip() in state:                   #Check if the variable is in the state
                    if varmap(variable.strip(), state) < int(value.strip()): #see if the var is less than
                        executeProgram(code.strip(), state)
                        
                        
                        
            elif ">" in condition:
                variable, value = condition.split(">")
                if variable.strip() in state:
                    if varmap(variable.strip(), state) > int(value.strip()):
                        executeProgram(code.strip(), state)
                        
                        
            elif "=" in condition:
                variable, value = condition.split("=")
                if variable.strip() in state:
                    if varmap(variable.strip(), state) > int(value.strip()):
                        executeProgram(code.strip(), state)
                        

            
        
        
        
sampleProgram1 = """
INTRODUCING JONJONES = 30
ANOUNCING JONJONES
INTRODUCING CONORMCGREGOR = 24
INTRODUCING KHABIB = 100
ANOUNCING KHABIB
ANOUNCING JONJONES
ANOUNCING CONORMCGREGOR
"""
        
        
        
        
        
        
        
        
sampleProgram2 = """
INTRODUCING Jb = 19
INTRODUCING G = 10
IF G < 50: ANOUNCING G
"""

executeProgram(sampleProgram1)