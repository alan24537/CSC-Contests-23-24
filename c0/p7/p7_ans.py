japanese = [
"a", "i", "u", "e", "o",
"ka", "ki", "ku", "ke", "ko",
"sa", "shi", "su", "se", "so",
"ta", "chi", "tsu", "te", "to",
"na", "ni", "nu", "ne", "no",
"ha", "hi", "fu", "he", "ho",
"ma", "mi", "mu", "me", "mo",
"ya", "yu", "yo",
"ra", "ri", "ru", "re", "ro",
"wa", "wo", "n"
]

s = input()
i = 0
valid = True
while i < len(s):
    if s[i] in japanese:
        i+=1
    elif i+2 <= len(s) and s[i:i+2] in japanese:
        i+=2
    elif i+3 <= len(s) and s[i:i+3] in japanese:
        i+=3
    else:
        valid = False
        break
print("yes" if valid else "no")