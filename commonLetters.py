text1 = "hello"
text2="plus"
new_text1 = set(text1)
new_text2 = set(text2)
common = new_text1.intersection(new_text2)
print(str(common))
