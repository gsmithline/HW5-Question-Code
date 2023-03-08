class HW:  
    
    def Q1(a):
        #BASE
        H = 0
        M = H
        #"RECURSIVE CASE"
        for i in a:
            H = max(0, H+i)
            M = max(H, M); 
        return M
    #This only is correct for all non-negative integers
    def Q3(heros, v):
        #If we have 1 we can compute any value, but might bot makes sense as O(n) to do this
        if (1 in heros or v == 0): return True
        #CREATE ARRAY FOR MEMOIZATION
        marvel = [False] * (v+1)
        #BASE CASE:
        marvel[0] = True
        #RECURSIVE CASE: we go marvel[hero] to marvel[V]
        for hero in heros: 
            for i in range(hero, v+1):
                if (marvel[i] == True):
                    continue
                elif (marvel[i-hero] == True):
                    marvel[i] = True
        return marvel[v]

print(HW.Q1([25, -11, 15, 16, -20]));
print(HW.Q3([4, 5, 6, 7, 8, 9], 109));
