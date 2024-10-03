class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        while students:
            if sandwiches[0] not in students:
                return len(students)
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())
        
        return 0
        
            

        