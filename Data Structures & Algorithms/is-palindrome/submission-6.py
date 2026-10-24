class Solution:
    def isPalindrome(self, s: str) -> bool:
        
            b = s.replace("?","")
            c = b.replace(" ","")
            f = c.replace(",","")
            g = f.replace("'","").replace(".","").replace("!","").replace("&","").replace("*","").replace(":","").replace(";","")
            a = g[::-1]
            d = g.lower()
            e = a.lower() 


            if d != e:
                return False
            else:
                return True
