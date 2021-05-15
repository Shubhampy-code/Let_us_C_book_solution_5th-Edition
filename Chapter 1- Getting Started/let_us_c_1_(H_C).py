Mathes = input("Enter your number of Mathes:")
Physics = input("Enter your number of Physics:")
Chemistry = input("Enter your number of Chemistry:")
Biology = input("Enter your number of Biology:")
Art = input("Enter your number of Art:")
mathes = float(Mathes)
physics = float(Physics)
chemistry = float(Chemistry)
biology = float(Biology)
art = float(Art)
aggregate_marks = (mathes + physics + chemistry + biology + art)
print("Aggregate marks:" + str(aggregate_marks))
percentage_marks = aggregate_marks*(1/5)
print( "Percentage marks:" + str(percentage_marks) + " %"  )

""" If the marks obtained by a student in five different subjects
are input through the keyboard, find out the aggregate marks
and percentage marks obtained by the student. Assume that
the maximum marks that can be obtained by a student in each
subject is 100. """