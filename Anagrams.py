def Anagrams(s1, s2):
    s1.lower()
    s2.lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

str1 = "silent"
print("String 1 : silent")
str2 = "listen"
print("String 2 : listen")

print("Are they anagrams? : ", Anagrams(str1, str2))