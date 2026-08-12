
from Student import StudentNode
from Stack import Stack
from Sorting import merge_sort

class StudentBST:
    """Binary Search Tree for Student Records"""
    def __init__(self):
        self.root = None

    def insert(self, student_id, name, marks):
        """Insert a student record into the tree """
        new_node = StudentNode(student_id, name, marks)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if student_id < current.student_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, student_id):
        """Search for a student by ID"""
        current = self.root
        while current:
            if current.student_id == student_id:
                return current
            elif student_id < current.student_id:
                current = current.left
            else:
                current = current.right
        return None  # Student not found
    
    def search_by_id(self, student_id):
        
        if not self.root:
            return None

        stack = [self.root]

        while stack:
            node = stack.pop()
            if node.student_id == student_id:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return None  # Not found

  
    
    def locate_student(self, student_id):
        """Searches for a student by performing traversal."""
        return self._search_student(self.root, student_id)

    def _search_student(self, node, student_id):
        """Performs traversal to find the student."""
        if node is None:
            return None  # Not found
    
        if node.student_id == student_id:
            return node  # Found the student
    
        left_result = self._search_student(node.left, student_id)
        if left_result:
            return left_result
    
        return self._search_student(node.right, student_id)  # Continue in right subtree
    
    def _collect_students(self, node, students):
        """Helper function to collect students into a list."""
        if node:
            students.append(node)  # Store node in list
            self._collect_students(node.left, students)
            self._collect_students(node.right, students)
    
    def display_sorted(self):
        """Sorts student records using a simple Bubble Sort approach and displays them."""
        students = []
        self._collect_students(self.root, students)  # Collect student records into a list
        
        # Bubble Sort - inefficient sorting
        n = len(students)
        for i in range(n):
            for j in range(0, n-i-1):
                if students[j].student_id > students[j+1].student_id:
                    students[j], students[j+1] = students[j+1], students[j]  # Swap
        
        # Display sorted students
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, marks: {student.marks}")
            
            
     # Student needs to complete these ( Refer to the Assessment Section A1.1 - A1.3)
     # TODO - A.1.1: define search_by_name method and/or any related helper methods
    def search_by_name(self,name):
        all_names=[]
        if self.root is None:
            return all_names

        stack=[self.root]

        while stack:
            node_x=stack.pop()
            if node_x.name.lower()==name.lower():
                all_names.append(node_x)

            if node_x.left:
                stack.append(node_x.left)

            if node_x.right:
                stack.append(node_x.right)

        return all_names


     
        
    
     # TODO - A.1.2: define total_student_count  method and/or any related helper methods
    # traverse tree
    # update count every time you visit a node 
    def total_student_count(self):
        return self.count_nodes(self.root)

    def count_nodes(self,node):
        if node is None:
            return 0
        return 1+ self.count_nodes(node.left)+self.count_nodes(node.right)
          
        
        
    
    # TODO - A.1.3: define display_ordered  method and/or any related helper methods
    def display_ordered(self):
       
       students=[]
       self._collect_students(self.root,students)

       ids=[]
       for student in students:
           ids.append(student.student_id)

       sorted_ids=merge_sort(ids)
       for student_id in sorted_ids:
           student=self.search(student_id)

           if student:
               print(f"ID:{student.student_id}, Name:{student.name}, Marks:{student.marks}")
       return
       
       # option -1 already displays data in ordered ( ordered by Id)
       # you need to do the same , however, you need to employ  efficient sorting technique
       
       
        
   # TODO  A.1.4 : Complete this method to count the total number of nodes in the BST
   # This uses iterative approach and makes of of provided stack ( refer to stack.py)
    def total_student_count_iter(self):
        #if tree is empty, no any students in there.
        if not self.root:
            return 0
        #this one count total student
        count = 0

        #this one is custom stack name.
        stack = Stack()

        #we put the root in the stack,traversal starts here.
        stack.push(self.root)

        #this one checks,is there any node in the stack?
        condition=stack.is_not_empty()

        #loop will be continued until stack will empty.
        while condition:
            
            #pop() takes a "student node" from the stack.
            node_x=stack.pop()

            #if that's a student then add with count
            count+=1

            #if there any children in left side, then we save in the stack
            if node_x.left:
                stack.push(node_x.left)

            #if there any children in right side , then we save in the stack.
            if node_x.right:
                stack.push(node_x.right)
            #finally check even any node in the tree.
            condition=stack.is_not_empty()
        return count

        
        
       
   # TODO A.1.5: Method to update student record
    def update_student_record(self, student_id):
        student=self.search(student_id)
        if student is None:
            return False

        print("1.Name")
        print("2.Marks")

        choice=input("Enter Your Choice Number:")

        if choice =="1":
            name_x=input("Enter the Name:")
            student.name=name_x

        elif choice=="2":
            marks_x=float(input("Enter the Marks:"))
            student.marks=marks_x

        else:
            print("Invalid Choice")
            return False

        return True


               # TODO : Use provided methods to check if student with given student_id exists
       
       # If the student exists, prompt the user to  enter options 1 -> To update Name , 2 -> update marks.
       # .. update the record based on user choice
       
       
   
       
       
           



