#Daily Challenge : Pagination
#Create a Pagination class that simulates a basic pagination system.
print('Daily Challenge, Week 2, Day 2: Pagination')
print('')

import math
#Create the Pagination Class
class Pagination():
    def __init__(self, items=None, page_size=10): #init method with parameters
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.page_size > 0 else 0 #imported math to the file

#Implement the get_visible_items() Method
    def get_visible_items(self):
        start_index = self.current_idx * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

  #Implement Navigation Methods  
    def go_to_page(self, page_num):
        if not (1 <= page_num <= self.total_pages):
            raise ValueError(f"Page number {page_num} is out of range. Must be between 1 and {self.total_pages}.")
        else:         
            self.current_idx = page_num - 1 #since it starts at 0, but user input would be 1
        
        

    def first_page(self):
        if self.total_pages > 0:
            self.current_idx = 0
        return self

    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return '\''.join(str(item) for item in self.get_visible_items())
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(4)
print(p.current_idx + 1)
# Output: ValueError

p.go_to_page(20)
# print(p.get_visible_items())
# Raises ValueError
    