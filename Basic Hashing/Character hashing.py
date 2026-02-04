#only small letters i.e., 'a' <= s[i]<='z'
s="axtiegndgtdhghdjjdjkdhsksjshnshnsnmshjsthsnhgnhmsnmsjkdjksjndhjdjkszghsbgnndbdhndbd"
q=['a','x','s','t']

l=[0]*26
for ch in s:
    ascii_val=ord(ch)
    i=ascii_val-97
    l[i]+=1
for ch in q:
    ascii_val=ord(ch)
    i=ascii_val-97
    print(f"The '{ch}' repeats {l[i]} times")