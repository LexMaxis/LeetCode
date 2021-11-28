class Solution(object):
    # def countWords(self, words1, words2):
    #     count = 0
    #     temp = []
    #     if len(words1) <= len(words2):
    #         for it in words1:
    #             temp.append(it)
    #
    #         for word in temp:
    #             if words1.count(word) != 1 and words1.count(word)!= 0:
    #                 for i in range(words1.count(word)):
    #                     words1.remove(word)
    #             else:
    #                 words1.remove(word)
    #                 if word not in words1:
    #                     if word in words2:
    #                         words2.remove(word)
    #                         if word not in words2:
    #                             count += 1
    #     else:
    #         for it in words2:
    #             temp.append(it)
    #         for word in temp:
    #             words2.remove(word)
    #             if word not in words2:
    #                 if word in words1:
    #                     words1.remove(word)
    #                     if word not in words1:
    #                         count += 1
    #
    #     return count
    #

    def countWords(self, words1, words2):
        dict_words1 = {}
        dict_words2 = {}
        count = 0
        for it in words1:
            dict_words1[it] = words1.count(it)

        for it in words2:
            dict_words2[it] = words2.count(it)

        for it in dict_words1:
            if dict_words2.get(it):
                if dict_words1[it] == dict_words2[it] == 1:
                    count += 1

        return count



if __name__ == '__main__':
    word1 = ["ibxyatvglhltxngewrcrqbbnew", "towokpjpkccmob", "kdmtwngzpebwpnvlazhdcmtwpjh", "muh",
             "fzzlmacbbvoqdueutjqoutwd", "ylluspdftxxqbwadivfdzulghq", "hioiacezaiptpsvcojzckhxz",
             "nzcjhjomaupevyekennyrfwyd", "tdwtuinstwsfyjnfkxkbnsptisuifo", "wrdwoxzsczzlnwjugopohxh", "p", "jkez",
             "drisymx", "fsva", "myqc", "aovjoxzpkylpecltwtottzidq", "wqspbhpberqjabockesc", "f", "qostobxgfliil",
             "gsekmhjpuedeivioudx", "tzelzowtgnvjsxgbw", "zgmpazgnioprk", "fucybddarjcve", "ldacfviysy",
             "yxyjairoxtvbkljaokca", "vxpiohhvjuwcpiceafcdzobalgpz", "wyflbpmkfwftndgtnftajgla", "xbxvvk",
             "bnrwyshimjamltmlugeiviu", "wsgqysmuakedrrmjk", "ppqmgibqljkwgmiwi", "fly", "uf", "tvvttzrsjbojve",
             "ztxtnmljdhyz", "vxonvloufeksfvg", "wql", "kotdenqjrdlgofubocb", "wlaqceczd", "mtmhtgvqwr",
             "aymzxpfvbqxydmilafyqvapuxtnqe", "ig", "atetjlhdcigunmmit", "enkdcxqnw", "gtlcmkxwvdhumgfurxkesmekmnhjo",
             "hurihasxncgtzleerslvwxkz", "zked", "xiaqvclhuhggcgoouzjgi", "mzejuubgyhvlfbecpmggddby",
             "boyotuukuiprtlvktypxboosw", "vwfceei", "gopsxsihawzhtlmdyiggljzggrhqr", "bckuuqszgncdhkeghudflczm", "e",
             "yvhwysrunkxsppbqjf", "lo", "bze", "kuzoqvgugnrpfkelktfg", "ntjtlwwmuevtsqujpxswgx",
             "zkdwtpdlvrfkbyktqsellmghaxj", "u", "rpmpq", "ajhlzwfrbysqloduofr", "gyfmhcskcrjepgeplbbj", "fe",
             "zyolvtetrdffy", "apbkyczsuvde", "fnkqf", "qwwxpwbr", "krkbnww", "zkvqkugfpziawiokdzlpjomfarkor", "jg",
             "l", "srbvxsnuhyqzmycvavmmakh", "dhkgzjrstir", "smaaptkzpwhukebwboysbnawgzgot"]

    word2 = ["p", "towokpjpkccmob", "vflbjyecpzxnuay", "fzas", "fzzlmacbbvoqdueutjqoutwd", "bwjjzw", "va",
             "manrvuldjzrdnwihzct", "tdwtuinstwsfyjnfkxkbnsptisuifo", "wrdwoxzsczzlnwjugopohxh", "p",
             "tylcyihdjruhaayzcwxrynnkch", "uojzddpgyvqslha", "fsva", "rucvbjzfewjlhddxefhf", "tfihr",
             "wqspbhpberqjabockesc", "f", "bmfo", "zsjbzjmbloaybdofsrqvzwoizz", "tzelzowtgnvjsxgbw", "tproznqma",
             "lmryjiyvkgsxsaylkdmmxeub", "ldacfviysy", "xpamoswlugwjxyny", "rmfvgm", "wm", "xbxvvk", "ubawz", "jbrabb",
             "rgegpb", "fly", "aofydpklgjqmxhvxuhq", "tvvttzrsjbojve", "wj", "vxonvloufeksfvg", "wql", "vu",
             "nhuxqdfyftrbbodztyydb", "mtmhtgvqwr", "aymzxpfvbqxydmilafyqvapuxtnqe", "fqksatpfo", "ylzkfvvzdsryl",
             "enkdcxqnw", "gtlcmkxwvdhumgfurxkesmekmnhjo", "nccwybkxuawwdqyhrhmbt", "zked", "eyzwtvsjt", "qy",
             "boyotuukuiprtlvktypxboosw"]

    s = Solution()
    print(s.countWords(word1, word2))
