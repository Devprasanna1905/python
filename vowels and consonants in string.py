v = 0;  
c= 0;  
str = "gopal";  
a = str.lower();  
for i in range(0,len(a)):   
    if str[i] in ('a',"e","i","o","u"):  
        v = v + 1;  
    else:  
        c = c + 1;  
print("Total number of vowel and consonant are" );  
print(v);  
print(c);    
