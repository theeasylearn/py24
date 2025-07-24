# example of choice & choices 
import random as rd 

# create list 
ipl_teams_2025 = ["Chennai Super Kings", "Kolkata Knight Riders", "Rajasthan Royals", "Royal Challengers Bengaluru", "Punjab Kings", "Mumbai Indians", "Sunrisers Hyderabad", "Delhi Capitals", "Gujarat Titans", "Lucknow Super Giants"]

print("next winner in ipl will be ",rd.choice(ipl_teams_2025))


print("in ipl 2026 4 qualifiers will be ",rd.choices(ipl_teams_2025,k=4))

rd.shuffle(ipl_teams_2025)
print("point table in 2026 will be below")
print(ipl_teams_2025)
