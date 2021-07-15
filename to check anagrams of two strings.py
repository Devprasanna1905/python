def checkanagrams(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("true")
    else:
        print("False")

a=input()
b=input()
checkanagrams(a,b)
