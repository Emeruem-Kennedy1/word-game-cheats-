k = int(input('number of letters in your word: '))
string=input('word: ')
while k>0:
    from itertools import permutations
    l=list(permutations(sorted(string),(k)))
 
    for i in l:
        a = "".join(i)
        #print(a)

        import enchant
        d = enchant.Dict("en_US")
        c = d.check(a)
        if c ==True:
            print(a,'is',c)
    k -= 1