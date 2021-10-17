class Solution(object):
    def winnerOfGame(self, colors):

        color = []

        flag = 0
        stop = 0

        for i in range(len(colors)):
            if i % 2 == 0:
                flag = self.func('A', color)

            else:
                flag = self.func('B', color)


        return flag

    def func(self, str, colors, stop):

        i = 0
        flag = 0
        while i + 2 < len(colors):
            if colors[i] == colors[i + 1] == colors[i + 2] == str:
                colors.remove(colors[i + 1])
                flag = 1
            else:
                stop = 1
                i += 1
                flag = 0

    
        return flag
