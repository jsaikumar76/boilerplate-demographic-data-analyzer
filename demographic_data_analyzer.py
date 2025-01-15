import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df["race"].value_counts())

    # What is the average age of men?
    men = df[df.sex == "Male"]
    average_age_men = round(men["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df[df.education == "Bachelors"]
    percentage_bachelors = round(len(bachelors) / len(df) * 100, 1)

    
    adv_edu = len(df[df.education == "Bachelors"])
    adv_edu += len(df[df.education == "Masters"])
    adv_edu += len(df[df.education == "Doctorate"])

    lower_edu = len(df) - adv_edu

    salary_morethan_50k = df[df.salary == ">50K"]
    adv_edu_morethan_50k = len(salary_morethan_50k[salary_morethan_50k.education == "Bachelors"])
    adv_edu_morethan_50k += len(salary_morethan_50k[salary_morethan_50k.education == "Masters"])
    adv_edu_morethan_50k += len(salary_morethan_50k[salary_morethan_50k.education == "Doctorate"])

    lower_edu_morethan_50k = len(salary_morethan_50k) - adv_edu_morethan_50k
        
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = round(adv_edu_morethan_50k / adv_edu * 100, 1)
    lower_education_rich = round(lower_edu_morethan_50k / lower_edu * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df["hours-per-week"] == min_work_hours])
    min_work_hours_morethan_50k = len(salary_morethan_50k[salary_morethan_50k["hours-per-week"] == min_work_hours])

    rich_percentage = int(min_work_hours_morethan_50k / num_min_workers * 100)

    # What country has the highest percentage of people that earn >50K?
    native_country = df["native-country"]
    high_salary = df[df.salary ==  ">50K"]
    salary_df = pd.concat([native_country.value_counts(), high_salary["native-country"].value_counts()], axis=1)
    salary_df.columns = ["salary", "high-salary"]
    salary_df["high-salary"] = salary_df["high-salary"].fillna(0).astype(int)
    salary_df["percent"] = round(salary_df["high-salary"] / salary_df["salary"] * 100, 1)
    

    highest_earning_country = salary_df[salary_df["percent"] == salary_df["percent"].max()].index
    highest_earning_country_percentage = salary_df["percent"].max()

    # Identify the most popular occupation for those who earn >50K in India.
    bharath_nationals = df[df["native-country"] == "India"]
    bharath_nationals_morethan_50k = bharath_nationals[bharath_nationals.salary == ">50K"]
    top_IN_occupation = bharath_nationals_morethan_50k.occupation.describe().top

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
