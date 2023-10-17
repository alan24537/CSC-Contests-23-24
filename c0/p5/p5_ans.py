jp1 = ["a", "i", "u", "e", "o","n"]

jp2 = [
    "ka", "ki", "ku", "ke", "ko",
    "sa", "su", "se", "so",
    "ta", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo"
]

jp3 = ["shi","chi", "tsu"]

s = input()

found = [False for i in range(len(s))]
valid = True
for i in range(len(s)):
    if found[i]:
        continue
    for c3 in jp3:
        if i + 2 < len(s) and s[i] == c3[0] and s[i+1] == c3[1] and s[i+2] == c3[2]:
            found[i], found[i+1], found[i+2] = True, True, True
            break
    for c2 in jp2:
        if i + 1 < len(s) and s[i] == c2[0] and s[i+1] == c2[1]:
            found[i], found[i+1] = True, True
            break
    for c1 in jp1:
        if s[i] == c1[0]:
            found[i] = True
            break
    if not found[i]:
        valid = False
        break
print("yes" if valid else "no")