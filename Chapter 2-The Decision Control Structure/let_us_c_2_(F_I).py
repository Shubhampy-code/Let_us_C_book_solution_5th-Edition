"""A university has the following rules for a student to qualify
for a degree with A as the main subject and B as the
subsidiary subject:
(a) He should get 55 percent or more in A and 45 percent or
more in B.
(b) If he gets than 55 percent in A he should get 55 percent or
more in B. However, he should get at least 45 percent in
A.
(c) If he gets less than 45 percent in B and 65 percent or more
in A he is allowed to reappear in an examination in B to
qualify.
(d) In all other cases he is declared to have failed.
Write a program to receive marks in A and B and Output
whether the student has passed, failed or is allowed to
reappear in B. """

Per_in_A = float(input("Enter the percentage in main subject : "))
Per_in_B = float(input("Enter the percentage in subsidiary number : "))

if Per_in_A >= 45 and Per_in_B >=45:
    print("Student is qualify for the degree")
elif Per_in_B < 45 :
    print("Student is allowed to reappear in an examination in B to qualify") 
else:
    print("Student is failed")