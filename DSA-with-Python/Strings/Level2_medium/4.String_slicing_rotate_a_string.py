'''*******************************************************************************************************
Rotate the given string.
Input : s = "NituRanaSoftwareDeveloper" 
        d = 2
Output : Left rotation : "tuRanaSoftwareDeveloperNi"
         Right rotation : "erNituRanaSoftwareDevelop"
***********************************************************************************************************'''
def rotate(input,d):
 
    Lfirst = input[0 : d]
    Lsecond = input[d :]
    Rfirst = input[0 : len(input)-d]
    Rsecond = input[len(input)-d : ]
 
    print ("Left Rotation : ", (Lsecond + Lfirst) )
    print ("Right Rotation : ", (Rsecond + Rfirst))
 
if __name__ == "__main__":
    input = 'NituRanaSoftwareDeveloper'
    d=2
    rotate(input,d)