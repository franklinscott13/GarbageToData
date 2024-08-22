# KinCodeTest
This is process will take a visual representation of numbers using pipes '|' and underscores '_' using three lines of a file, and try to conver them into real numbers. 
As well as try to check some the value to see the formula mod 11 == 0 and then write to a file detrmining if the value is good or not. 
Resulting with the out put of:
 _       _   _   _   _   _   _       
|_  |_| |_  | | |_  | | |_| |_   |_| 
 _|   | |_| |_|  _| |_| |_| |_|    | 
PossibleNumbers: 54605086?
Checksum ILL for: 54605086?
 _   _           _   _       _   _  
|_|  _|   | |_| |_| |_|   |  _| |_ 
|_|  _|   |   | |_| |_|   | |_  |_| 

PossibleNumbers: 831488126
Checksum Valid for: 831488126
 _           _   _   _   _   _   _  
|_|   | |_| |_    | |_  | | |_|   | 
 _|   |   |  _|   |  _| |_| |_|   | 
 
PossibleNumbers: 914575087
Checksum ERR for: 914575087
# Requirements
Need to have python installed. Navigate to the root of the folder(GarbageToData) and run 'pip install requirements.txt' then run 'make run'


# Code explanation
Takes the file that has pipes and underscores and builds a 3D Array then matches the 3D Array to a predetermined pattern. If the array matches the pattern it will map it to a number else will display '?' in its place

All values will land in 'results.txt' showing a good policy number or not, indicating an ERR for not a valid policy number or ILL which has an unreadable numeric value. 