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

idx = 0
found = False
ans = ""
while idx < len(s):
    found = False
    for c in japanese: 
        if c == s[idx : idx + len(c)]:
            idx += len(c)
            found = True
            break
    if not found:
        ans = "no"
        break
if ans != "no":
    ans = "yes"
print(ans)
    