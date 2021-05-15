"""In a town, the percentage of men is 52. The percentage of
total literacy is 48. If total percentage of literate men is 35 of
the total population, write a program to find the total number 
of illiterate men and women if the population of the town is
80,000."""

total_population = int(input("Enter the population of the town:"))
per_men = int(input("Enter the percentage of man in town:")) 
per_total_lit = int(input("Enter the total literacy in town:"))
per_lit_men = int(input("Enter the percentage of literate men:"))
men_in_town = total_population*(per_men/100)
print("Men in town:" + str(men_in_town))
Women_in_town = (total_population - men_in_town)
print("Women in town:" + str(Women_in_town))
lit_in_town = total_population*(per_total_lit/100)
print("Total literacy in town:" + str(lit_in_town))
lit_men = (total_population*per_lit_men/100)
print("Literate men in town:" + str(lit_men))
lit_women = (lit_in_town-lit_men)
print("Literate women in town:"+str(lit_women))
illit_men = men_in_town-lit_men
print("Illiterate men:"+str(illit_men))
illit_women = (Women_in_town-lit_women)
print("Illiterate women:"+str(illit_women))