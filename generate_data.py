import numpy as np
import pandas as pd
np.random.seed(42) #to fix the generation of random numbers when run again and again
student_ids=[f"s{i:03d}" for i in range(1,751)]#to generate student ids from s001 to s750
print(student_ids[:10])
print(len(student_ids))
ages=np.random.randint(21,26,size=750)
print(ages[:10])
cgpa=np.random.normal(loc=7.2,scale=1.0,size=750)#loc=mean,scale=sd
cgpa=np.clip(cgpa,4.0,10.0)#to make sure nothing goes below 4.0 or above 10.0.
cgpa=np.round(cgpa,2)#to round off cgpa upto 2 decimal places
print(cgpa[:10])
attendance = np.random.normal(loc=82, scale=8, size=750)
attendance = np.clip(attendance, 60, 100)
attendance = np.round(attendance, 2)
print(attendance[:10])
#backlog choices 0,1,2,3,4,5 with probability 55% 20% 12% 7% 4% 2%
backlogs=np.random.choice([0,1,2,3,4,5],size=750,p=[0.55,0.20,0.12,0.07,0.04,0.02])
print(backlogs[:10])
internships=np.random.choice([0,1,2,3],size=750,p=[0.45,0.35,0.15,0.05])
print(internships[:10])
projects=np.random.choice([0,1,2,3,4,5],size=750,p=[0.05,0.20,0.30,0.25,0.15,0.05])
print(projects[:10])
certifications=np.random.choice([0,1,2,3,4],size=750,p=[0.25,0.35,0.25,0.10,0.05])
print(certifications[:10])
#python skill=base skill+project effect+internship effect+random variation
python_skill=(5+0.5*projects+0.7*internships+np.random.normal(0,1.5,size=750))
python_skill=np.clip(python_skill,1,10)
python_skill=np.round(python_skill,1)
print(python_skill[:10])
sql_skill=(4.5+0.6*projects+0.8*certifications+np.random.normal(0,1.5,size=750))
sql_skill=np.clip(sql_skill,1,10)
sql_skill=np.round(sql_skill,1)
print(sql_skill[:10])
#Taking 7.0 as a baseline CGPA, CGPA above or below that slightly influence DSA skil
dsa_skill=(4.5+0.4*(cgpa-7.0)+0.3*projects+np.random.normal(0,1.5,size=750))
dsa_skill=np.clip(dsa_skill,1,10)
dsa_skill=np.round(dsa_skill,1)
print(dsa_skill[:10])
aptitude_score=(55+6*(cgpa-7.0)+np.random.normal(0,10,size=750))
aptitude_score = np.clip(aptitude_score, 30, 100)
aptitude_score = np.round(aptitude_score, 1)
print(aptitude_score[:10])
placement_score=(-2.5+0.8*(cgpa-7.0)+0.3*internships+0.2*projects+0.15*python_skill+0.10*sql_skill+0.10*dsa_skill+0.03*(aptitude_score-60)+np.random.normal(0,1,size=750))
print(placement_score[:10])
#sigmoid function to convert placement score(which can be negative) to probability(0 to 1)
placement_probability=1/(1+np.exp(-placement_score))
print(placement_probability[:10])
print("Average placement probability:", placement_probability.mean())
print("Minimum probability:", placement_probability.min())
print("Maximum probability:", placement_probability.max())
#letting each student's probability determine their chance of getting a 1
#student whose probability is 0.90 there's a 90% chance that placed becomes 1
# 1 represents placed and 0 represents not placed 
#binomial used to simulate 750 independent trials with different probabilities for each student
placed=np.random.binomial(1,placement_probability)
print(placed[:10])
print("Number of students placed:",placed.sum())
print("Placement rate:",placed.mean())
package_lpa = (3.0+ 0.5 * (cgpa - 6.0)+ 0.4 * internships+ 0.25 * projects+ 0.15 * python_skill+ 0.10 * sql_skill+ 0.10 * dsa_skill+ 0.02 * (aptitude_score - 50)+ np.random.normal(0, 1.5, size=750))
package_lpa = np.clip(package_lpa, 3, 15)
package_lpa = np.round(package_lpa, 1)
package_lpa = package_lpa * placed #to make 0 for placed=0 students
print(package_lpa[:10])
df=pd.DataFrame({"student_id":student_ids,"age":ages,"cgpa":cgpa,"attendance":attendance,"backlogs":backlogs,"internships":internships,"projects":projects,"certifications":certifications,"python_skill":python_skill,"sql_skill":sql_skill,"dsa_skill":dsa_skill,"aptitude_score":aptitude_score,"placed":placed,"package_lpa":package_lpa})
print(df.head()) #to show first five rows of the dataframe
df.to_csv("placement_data.csv",index=False) #to save the dataframe to a csv file without index

