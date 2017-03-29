#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

import sys

names = []
	
def get_average(marks):
	total_add = 0;
	for mark in marks:
		total_add = total_add + mark
		
	print(total_add)	
	return float(total_add) / float(len(marks))
		
def name_holder(name, surname):
	if type(name) == str and type(surname) == str:
		names.append(str(name + ' ' + surname))
	else:
		print('Impossible to store the name. Name and Surname should be strings')
		
			
def check_attendance(attendance):
	total_attendance = 0
	for value in attendance:
		if value is (1 or 0):
			pass
		else:
			sys.exit('Not valid value in Attendance list')
			
		total_attendance += day
		return total_attendance			
	
	
if __name__ == '__main__':
	marks = [1, 5, 4, 3 ,5]
	name = 'Hector'
	surname = 'Blanco'
	attendance = [0,1,1,1,0,0,1,0,1,1,1,1,1,0]
	
	




