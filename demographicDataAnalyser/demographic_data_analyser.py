import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

   
    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']
    higher_education_rich_percentage = (len(higher_education_rich) / len(higher_education)) * 100

    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    lower_education_rich_percentage = (len(lower_education_rich) / len(lower_education)) * 100

   
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("\n\nAverage age of men:", round(average_age_men, 1))
        print(f"\n\nPercentage with Bachelors degrees: {round(percentage_bachelors, 1)}%")
        print(f"\n\nPercentage with higher education that earn >50K: {round(higher_education_rich_percentage, 1)}%")
        print(f"\n\nPercentage without higher education that earn >50K: {round(lower_education_rich_percentage, 1)}%")
        print("\n\nMin work time:", min_work_hours, "hours/week")
        print(f"\n\nPercentage of rich among those who work fewest hours: {round(rich_percentage, 1)}%")
        print("\n\nCountry with highest percentage of rich:", highest_earning_country)
        print(f"\n\nHighest percentage of rich people in country: {round(highest_earning_country_percentage, 1)}%")
        print("\n\nTop occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich_percentage': higher_education_rich_percentage,
        'lower_education_rich_percentage': lower_education_rich_percentage,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
