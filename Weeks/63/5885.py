class Solution(object):
    def minMovesToSeat(self, seats, students):
        n = len(seats)
        change_count = 0
        seats.sort()
        students.sort()
        for i in range(n):
            change_count += abs(seats[i]-students[i])
        return change_count