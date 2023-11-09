# print("no" if input() in ["miso", "hakuto", "ringo", "paula", "sprite"] else "yes")

names = ["miso", "hakuto", "ringo", "paula", "sprite"]
gpt_name = input()
if gpt_name in names:
    print("no")
else:
    print("yes")