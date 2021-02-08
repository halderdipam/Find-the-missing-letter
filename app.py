# Solution One:
def find_missing_letter(chars):
    s = ''
    for i in range(0,len(chars)-1):
        if(ord(chars[i+1]) - ord(chars[i]) > 1):
            s = chr(ord(chars[i])+1)
    return s
 
Solution Two:
def find_missing_letter(chars):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c= 0
    f = False
    for i in s:
        if i == chars[c]:
            f=True
            c += 1
        elif f==True:return i
    
print(find_missing_letter(['a','b','c','d','f']))
    
print(find_missing_letter(['a','b','c','d','f']))
