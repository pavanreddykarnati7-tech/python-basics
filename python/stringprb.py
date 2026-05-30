s=str(input())
print("number of vowels :", s.count("a")+s.count("e")+s.count("i")+s.count("o")+s.count("u"))
print("number of consonants :", len(s)-s.count("a")-s.count("e")-s.count("i")-s.count("o")-s.count("u")-s.count(" "))