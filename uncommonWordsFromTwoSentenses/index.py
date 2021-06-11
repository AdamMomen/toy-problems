import collection import Counter
def uncommonFromSentences(A, B):
    c = collections.Counter((A + " " + B).split())
    return [w for w in c if c[w] == 1]

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2))
