# Student Placement Analytics


## Project Overview

This project analyzes student placement data to understand which academic, technical, and practical factors are associated with placement outcomes.

The analysis uses Python, Pandas, Matplotlib, Seaborn, and statistical techniques such as correlation and linear regression to explore patterns in student placements and salary packages.

## Dataset

The dataset contains information about 750 students and includes academic, technical, and placement-related attributes.

### Features

* Student ID
* Age
* CGPA
* Attendance
* Backlogs
* Internships
* Projects
* Certifications
* Python Skill
* SQL Skill
* DSA Skill
* Aptitude Score
* Placement Status
* Package (LPA)

The dataset used in this project is synthetically generated for educational and analytical purposes.

## Project Objectives

The main objectives of this project are to:

* Analyze the overall placement rate of students.
* Investigate whether students with more internships have better placement outcomes.
* Compare the average CGPA of placed and non-placed students.
* Study the relationship between CGPA, aptitude score, technical skills, and placement.
* Identify the factors most strongly associated with placement.
* Analyze the relationship between CGPA and package among placed students using linear regression.
* Examine placement rates across different Python skill ranges.
* Analyze the distribution of salary packages among placed students.


## Technologies Used

* **Python** — Programming language used for data analysis.
* **Pandas** — Data loading, manipulation, grouping, and analysis.
* **NumPy** — Used for numerical operations and synthetic data generation.
* **Matplotlib** — Used to create charts and visualizations.
* **Seaborn** — Used to create the correlation heatmap.
* **SciPy** — Used for linear regression analysis.
* **Jupyter/VS Code** — Used for developing and running the analysis.

## Analysis and Key Findings

### 1. Overall Placement

The dataset contains **750 students**, of whom **436 were placed**, resulting in an overall placement rate of approximately **58.13%**.

This provides a general overview of the placement outcomes in the dataset before analyzing individual factors.

### 2. Internships and Placement

The analysis shows that placement rates generally increase as the number of internships increases.

| Number of Internships | Placement Rate |
| --------------------: | -------------: |
|                     0 |         53.78% |
|                     1 |         57.37% |
|                     2 |         68.03% |
|                     3 |         72.73% |

Students with more internships had higher placement rates in this dataset. However, this represents an association and does not by itself establish that internships directly cause better placement outcomes.

The correlation between internships and placement was approximately **0.114**, indicating a **weak positive relationship**.

### 3. CGPA and Placement

The average CGPA of placed students was higher than that of non-placed students.

The analysis showed:

* **Average CGPA of non-placed students:** 6.87
* **Average CGPA of placed students:** 7.52
* **Correlation between CGPA and placement:** 0.324

The positive correlation indicates a weak-to-moderate positive relationship between CGPA and placement in this dataset. In general, students with higher CGPAs tended to have better placement outcomes.

However, CGPA alone does not determine placement, as other factors also showed relationships with placement.

### 4. Aptitude and Technical Skills

The analysis examined the relationship between placement and several academic and technical factors.

The correlations with placement were:

| Factor         | Correlation |
| -------------- | ----------: |
| Aptitude Score |       0.268 |
| Python Skill   |       0.198 |
| DSA Skill      |       0.195 |
| Projects       |       0.143 |
| Internships    |       0.114 |
| SQL Skill      |       0.109 |
| Certifications |       0.062 |
| Attendance     |       0.011 |
| Backlogs       |      -0.002 |
| Age            |      -0.033 |

Among these factors, **aptitude score showed the strongest relationship with placement after CGPA**, followed by Python skill and DSA skill.

The results suggest that both academic performance and technical/aptitude skills may be associated with placement outcomes. However, the correlations are mostly weak, so no single factor can be considered a reliable predictor of placement on its own.

### 5. CGPA and Package

For students who were placed, linear regression was used to examine the relationship between CGPA and their package.

The regression results were:

* **Slope:** 0.657
* **Intercept:** 2.364
* **R²:** 0.133

The slope indicates that, according to the fitted regression model, a one-point increase in CGPA corresponds to an estimated 0.657 LPA increase in package.

The R² value of **0.133** means that CGPA alone explains approximately **13.3% of the variation in package** among the placed students.

This indicates that CGPA has some relationship with package, but most of the variation in package is explained by factors other than CGPA.

### 6. Python Skill and Placement

Students were divided into five Python skill ranges to examine whether placement rates differed across skill levels.

| Python Skill Range | Number of Students | Placement Rate |
| ------------------ | -----------------: | -------------: |
| 0–2                |                  1 |       100.00%* |
| 2–4                |                 35 |         37.14% |
| 4–6                |                233 |         47.64% |
| 6–8                |                326 |         61.96% |
| 8–10               |                155 |         70.32% |

The placement rate generally increased as Python skill increased. Students in the **8–10 Python skill range had a placement rate of approximately 70.32%**, compared with **37.14%** for students in the 2–4 range.

The 0–2 range contains only one student, so its 100% placement rate is not representative and was excluded from the visualization.

The correlation between Python skill and placement was approximately **0.198**, indicating a weak positive relationship.

### 7. Package Analysis

Among the placed students, the salary packages ranged from **3.0 LPA to 11.4 LPA**.

| Metric          |     Value |
| --------------- | --------: |
| Average Package |  7.31 LPA |
| Median Package  |  7.40 LPA |
| Minimum Package |  3.00 LPA |
| Maximum Package | 11.40 LPA |

The median package of 7.4 LPA is slightly higher than the average package of 7.31 LPA. The closeness of these values suggests that there is no large difference between the typical package and the overall average in this dataset.

The package distribution was visualized using a histogram to observe how the salaries are spread among placed students.

## Conclusion

This project explored the relationship between student academic performance, technical skills, practical experience, and placement outcomes.

The analysis showed that **CGPA had the strongest positive correlation with placement among the student-related factors**, followed by aptitude score, Python skill, and DSA skill. Projects and internships also showed positive relationships with placement, although their correlations were weaker.

The analysis of internships showed that students with more internships generally had higher placement rates in the dataset. Similarly, placement rates generally increased across higher Python skill ranges.

For placed students, the average package was **7.31 LPA**, while the median package was **7.40 LPA**. The regression analysis showed that CGPA had some relationship with package, but with an R² of **0.133**, CGPA alone explained only a small portion of the variation in package.

Overall, the project demonstrates how data analysis and statistical techniques can be used to identify patterns in placement data and generate meaningful insights. Since the dataset is synthetic, these findings should be treated as analytical examples rather than conclusions about real-world student placements.

## Project Structure

```text
student-placement-analytics/
│
├── generate_data.py
├── placement_data.csv
├── analysis.py
└── README.md
```

* `generate_data.py` — Generates the synthetic student placement dataset.
* `placement_data.csv` — Contains the generated student placement data used for analysis.
* `analysis.py` — Contains the Python code used for data analysis, statistical calculations, and visualizations.
* `README.md` — Provides an overview of the project, methodology, findings, and results.


## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
cd student-placement-analytics
```

### 2. Install the required libraries

```bash
pip install pandas matplotlib seaborn scipy numpy
```

### 3. Generate the dataset

Run:
```bash
python generate_data.py
```

This creates the synthetic `placement_data.csv` file used for the analysis.

### 4. Run the analysis

Run:
```bash
python analysis.py
```

The script will display the statistical results and generate the visualizations used in the project.

## Future Improvements

Some possible improvements to this project include:

* Use a real-world student placement dataset instead of synthetic data.
* Add more advanced statistical analysis to study the relationships between different factors.
* Build a machine learning model to predict placement outcomes.
* Compare multiple machine learning algorithms and evaluate their performance.
* Add an interactive dashboard using tools such as Power BI, Tableau, or Streamlit.
* Include additional features such as interview performance, communication skills, and extracurricular activities.
