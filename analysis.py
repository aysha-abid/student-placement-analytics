#===========================
#1.Load and Inspect Dataset
#============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
df=pd.read_csv("placement_data.csv")
print(df.head())
print("Shape of dataset",df.shape)# gives number of rows and columnsin dataset
print("Columns:")
print(df.columns)
#======================
#2.Basic Data Analysis
#======================
print("\nMissing Values:")
print(df.isnull().sum())#gives missing values in each column
print("\nStatistical Analysis")
print(df.describe())# gives statistical analysis of the dataset
print("Average CGPA:",round(df["cgpa"].mean(),2))
print("Average Attendance:",round(df["attendance"].mean(),2))
print("Placement Rate:",round(df["placed"].mean()*100,2),"%")
print("Students with internships",(df["internships"]>0).sum())
print("Students with projects:", (df["projects"] > 0).sum())
#====================
#3.Placement Analysis
#====================
#Do students with internships have a higher placement rate than students without internships?
internship_placement=df.groupby("internships")["placed"].mean()*100
print("\nPlacement Rate by number of Internships:")
print(internship_placement)
#bar chart to visualize placement rate by number of internships
plt.bar(internship_placement.index,internship_placement.values)
plt.xlabel("Number of Internships")
plt.ylabel("Placement Rate (%)")
plt.title("Placement Rate by Number of Internships")
plt.show()
#Do students with higher CGPA have better placement outcomes?
print("\nAverage CGPA by Placement Status:")
cgpa_by_placement=df.groupby("placed")["cgpa"].mean()
print(cgpa_by_placement)
#First bar - Not Placed
#Second bar - Placed
#Heights - their respective average CGPAs
plt.bar(["Not Placed","Placed"],cgpa_by_placement.values)
plt.xlabel("Placement Status")
plt.ylabel("Average CGPA")
plt.title("Average CGPA by Placement Status")
plt.show()
#=======================
#4.Correlation Analysis
#=======================
#Correlation between CGPA and placement
cgpa_placement_correlation = df["cgpa"].corr(df["placed"])
print("Correlation between CGPA and placement:", cgpa_placement_correlation)
#correlation for internships vs placement
internship_placement_correlation = df["internships"].corr(df["placed"])
print("Correlation between internships and placement:", internship_placement_correlation)
#Correlation between aptitude score and placement
aptitude_placement_correlation = df["aptitude_score"].corr(df["placed"])
print("Correlation between aptitude score and placement:", aptitude_placement_correlation)
#Calculate the correlation between every numerical column and every other numerical column.
correlation_matrix=df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(correlation_matrix)
plt.figure(figsize=(12,8)) #space for the graph
#annot=True to display the correlation numbers on the heatmap
sns.heatmap(correlation_matrix,annot=True,fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()
#making dataframe for placed students
placed_students=df[df["placed"]==1]
print("Number of placed students:",len(placed_students))
#=====================
#5.Regression Analysis
#=====================
#relationship between CGPA and package among the placed students
#linregres(X,Y) X predictor, Y is what we're trying to predict
cgpa_package_regression = linregress(
    placed_students["cgpa"],
    placed_students["package_lpa"]
)
print("Regression slope:",cgpa_package_regression.slope) #regression=0.656 means for every one point increase in  cgpa the model predicts avg increase of about 0.657 lpa in package
print("Regression intercept:", cgpa_package_regression.intercept)
#how much the variation in package can be explained by CGPA alone from regression model.
print("R Squared:", cgpa_package_regression.rvalue**2)
#to make scatter plot 
plt.scatter(
    placed_students["cgpa"],
    placed_students["package_lpa"],
    alpha=0.5
)
#to add regression line to the scatter plot
plt.plot(
    placed_students["cgpa"],
    cgpa_package_regression.intercept
    + cgpa_package_regression.slope * placed_students["cgpa"]
)
plt.xlabel("CGPA")
plt.ylabel("Package (LPA)")
plt.title("CGPA vs Package for Placed Students")
plt.show()
#=================
#6.Skills Analysis
#=================
#For each Python skill level what percentage of students were placed?
python_skill_groups=pd.cut(df["python_skill"],bins=[0,2,4,6,8,10],labels=["0-2","2-4","4-6","6-8","8-10"])
python_placement=df.groupby(python_skill_groups,observed=True)["placed"].mean()*100
print("\nPlacement Rate by Python Skill Range:")
print(python_placement)
print("\nNumber of students in each Python skill range:")
print(python_skill_groups.value_counts().sort_index())
# The 0-2 range has only one student, so we exclude it from the graph
# to avoid a misleading 100% placement rate.
python_placement=python_placement.drop("0-2")# as only onestudent is falling in this range making the placement rate 100% which is misleading for python skill 0-2 range 
plt.bar(python_placement.index,python_placement.values) #one bar for each python skill range with height equal to placement rate
plt.xlabel("Python Skill Range")
plt.ylabel("Placement Rate(%)")
plt.title("Placement Rate by Python Skill")
plt.show()
#===========================
#7.Placement Factor Analysis
#===========================
#Find how strongly each numerical variable is associated with placement
placement_correlations=correlation_matrix["placed"].drop("placed")
placement_correlations=placement_correlations.sort_values(ascending=False)
print("\nFactors correlated with placement:")
print(placement_correlations)
# Package is an outcome after placement, so exclude it from placement factors
placement_factors=placement_correlations.drop("package_lpa")
print("\nPlacement factors:")
print(placement_factors)
plt.figure(figsize=(10,6)) #10 unit wide and 6 units tall
plt.barh(placement_factors.index,placement_factors.values)#barh = horizontal bars
plt.xlabel("Correlation with Placement")
plt.ylabel("Factor")
plt.title("Factors Associated with Placement")
plt.gca().invert_yaxis()#gca=get curretn axes
plt.show()
#===================
#8.Package Analysis
#===================
# Calculate the average package among placed students
average_package=placed_students["package_lpa"].mean() 
print("\n Average package among placed students:",average_package)
# Calculate the median package
# Median represents the middle value and is less affected by extreme values
median_package = placed_students["package_lpa"].median() 
print("Median package among placed students:", median_package)
#Visualize the distribution of packages
plt.hist(placed_students["package_lpa"],bins=10)
plt.xlabel("Package(LPA)")
plt.ylabel("Number of Students")
plt.title("Package Distribution Among Placed Students")
plt.show()
# Find the minimum and maximum packages
minimum_package=placed_students["package_lpa"].min()
maximum_package=placed_students["package_lpa"].max()
print("\nMinimum package among placed students:", minimum_package)
print("Maximum package among placed students:", maximum_package)

