def mingle(string1,string2):
    output =""
    if(len(string1)==0): return ""
    if(len(string2)==0): return ""
    else:
        return output+string1[0]+string2[0]+mingle(string1[1:],string2[1:])

print(mingle("abcde","pqrst"))
print(mingle("hacker","ranker"))