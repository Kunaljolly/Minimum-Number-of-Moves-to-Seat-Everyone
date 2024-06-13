class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        count = 0

        for x in range(len(seats)):
            if seats[x]-students[x]<0:
                count += (seats[x]-students[x])*-1
            else:
                count += seats[x]-students[x]
        return count
