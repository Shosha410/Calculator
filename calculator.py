import sys

def calculate():
    
    calc = input("Calculate:\n") 

    if not calc:
        print("ERROR! Empty enter")
        return
        
    for index in range(0, len(calc)):
        
        symbol = calc[index]
        if symbol.isalpha():
            print("ERROR! symbol can't be a letter (" + symbol + ")")
            return
            
        if index==0:
            if not symbol.isdigit() and symbol not in ['-', '(']:
                print("ERROR! Wrong first symbol (" + symbol + ")") 
                return 
                
        else:
            prevsymbol = calc[index-1]
            if prevsymbol in ['+','-','*','/']:
                if not symbol.isdigit() and symbol !='(':
                    print("ERROR! Wrong enter (" + symbol + ")")  
                    return
                        
    print("Ответ: " + str(eval(calc)))

while True:
    calculate()
    answer = input("Continue? Yes/No\n")
    if answer == "No":
        break
    if answer != "Yes":
        print("Invalid answer")
        sys.exit()
