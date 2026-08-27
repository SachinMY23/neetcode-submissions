class StudentNode():
    
    def __init__(self, val):
        self.val= val
        self.nxt= None
        self.prev= None

class Solution:
    def countStudents(self, students: List[int],   sandwiches: List[int]) -> int:
        count= len(students)
        current_sandwich= 0
        head= None
        tail=None

        if len(students)==1:
            return 0 if students[0]==sandwiches[0] else 1
    
        for i in students:
            if head is None:
                head= StudentNode(i)
            elif head is not None and tail is None:
                tail= StudentNode(i)
                tail.prev= head
                head.nxt= tail
            else:
                item= StudentNode(i)
                item.prev= tail
                tail.nxt= item
                tail= item
        tail.nxt= head
        head.prev= tail
        
        item= head
        loop_size= 0
        students_remaining= len(students)
        while(current_sandwich<len(sandwiches) and loop_size<students_remaining):
            if sandwiches[current_sandwich]==item.val:
                item.nxt.prev= item.prev
                item.prev.nxt= item.nxt
                loop_size=0
                students_remaining -= 1
                current_sandwich += 1
                print(f"sandwich next:{current_sandwich}")
            else:
                loop_size += 1
            item= item.nxt

        return students_remaining
            



    
    
    


   
        