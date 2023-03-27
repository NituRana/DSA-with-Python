'''*******************************************************************************************************
Convert the Camel case of a given sentence

Input : "Hello here I am nitu rana"
Output : ['H', 'e', 'o', 'h', ',', 'I', "'", 'm', 'i', 't', 'u']


***********************************************************************************************************'''
def convert(s):
    if(len(s) == 0):
        return
    s1 = ''
    s1 += s[0].upper()
    for i in range(1, len(s)):
        if (s[i] == ' '):
            s1 += s[i + 1].upper()
            i += 1
        elif(s[i - 1] != ' '):
            s1 += s[i]
    print(s1)    
             
# Driver Code
def main():
    s = "Hello here I am nitu rana"
    convert(s)
     
if __name__=="__main__":
    main()
