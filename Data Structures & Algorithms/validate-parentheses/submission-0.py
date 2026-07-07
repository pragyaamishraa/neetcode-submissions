class Solution:
    def isValid(self, s: str) -> bool:
        data = { ")" : "(", "]" : "[", "}" : "{" }
        checkS = []

        for i in s:
            if i in data:
                if checkS and checkS[-1] == data[i]:
                    checkS.pop()
                else:
                    return False
            else:
                checkS.append(i)
        
        return True if not checkS else False