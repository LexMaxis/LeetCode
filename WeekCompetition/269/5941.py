class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        time_order = {}
        scecret_list = [0, firstPerson]

        for i in range(len(meetings)):
            time_order[i] = meetings[i][2]

        for time in time_order.keys():
            print(time)

        return list(set(scecret_list))


if __name__ == '__main__':
    s = Solution()
    n = 6
    meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    firstPerson = 1
    s.findAllPeople(n, meetings, firstPerson)
