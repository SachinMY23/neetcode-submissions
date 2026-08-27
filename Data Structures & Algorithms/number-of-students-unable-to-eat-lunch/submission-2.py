class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        rem_students= len(students)
        count= Counter(students)

        for i in sandwiches:
            if count[i]>0:
                count[i] -= 1
                rem_students -= 1
            else:
                break

        return rem_students