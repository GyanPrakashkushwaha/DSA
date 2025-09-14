class Solution:
    def spellcheckerBruteForce(self, wordlist: list[str], queries: list[str]) -> list[str]:
        def checkVowel(wrd1, wrd2):
            if len(wrd1) != len(wrd2):
                return False
            for i in range(len(wrd1)):
                if wrd1[i] == wrd2[i]:
                    continue
                else:
                    if wrd1[i] in 'aeiou' and wrd2[i] in 'aeiou':
                        continue
                    return False
            return True

        out = []
        for i in range(len(queries)):
            found = False
            q = queries[i]
            # Exact match
            for j in range(len(wordlist)):
                if q == wordlist[j]:
                    out.append(q)
                    found = True
                    break
            if found:
                continue

            # first occurrence returning
            for k in range(len(wordlist)):
                if q not in out:
                    if q.lower() == wordlist[k].lower():
                        out.append(wordlist[k])
                        found = True
                        break
            if found:
                continue
    
            # Vowel check
            for l in range(len(wordlist)):
                if q not in out and checkVowel(q.lower(), wordlist[l].lower()):
                    out.append(wordlist[l])
                    found = True
                    break
            if found:
                continue
                

            out.append("")

        return out

    def spellcheckerOptimized(self, wordlist: list[str], queries: list[str]) -> list[str]:
        def mask(wrd):
            vowels = set('aeiou')
            masked = ''
            for c in wrd.lower():
                if c in vowels:
                    masked += '*'
                else:
                    masked += c
            return masked

        # vowel checker
        cond1 = set(wordlist)
        cond2 = {}
        cond3 = {}

        for word in wordlist:
            cond2.setdefault(word.lower(), word) # for the first occurrence used default value of key.
            cond3.setdefault(mask(word.lower()), word)
        
        print(cond1)
        print(cond2)
        print(cond3)

        out = []
        for query in queries:
            if query in cond1:
                out.append(query)
            elif query.lower() in cond2:
                out.append(cond2[query.lower()])
            elif mask(query.lower()) in cond3:
                out.append(cond3[mask(query.lower())])
            else:
                out.append("")

        return out

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
sol = Solution()
res = sol.spellcheckerOptimized(wordlist, queries)
# print(res)

