eff = [0, 0, 1, 1]

def make(inp):
    if(inp > 3):
        for i in range(4, inp + 1):
            min = eff[i - 1]
            
            if i % 3 == 0:
                if(eff[i // 3] < min):
                    min = eff[i // 3]
                    
            if i % 2 == 0:
                if(eff[i // 2] < min):
                    min = eff[i // 2]
            eff.append(min + 1)
    print(eff[inp])
    
    
    
    
a = int(input())
make(a)