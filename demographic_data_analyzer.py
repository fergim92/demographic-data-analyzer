import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().values

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].values.mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate']).value_counts()[True]
    lower_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate']).value_counts()[False]

    # percentage with salary >50K
    higher_education_rich = higher_education_rich = (df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts(normalize=True)['>50K'] * 100).round(1)
    #filtro = df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')
    #resultado_graduados_ricos = df[filtro].shape[0]
    #higher_education_rich =   ((resultado_graduados_ricos / higher_education) * 100).round(1)
    
    lower_education_rich = (df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts(normalize=True)['>50K'] * 100).round(1)
    #filtro2 = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')
    #resultado__no_graduados_ricos = df[filtro2].shape[0]
    #lower_education_rich = ((resultado__no_graduados_ricos / lower_education) * 100).round(1)



    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # Filtrar el DataFrame para obtener las personas que trabajan el número mínimo de horas por semana
    min_work_df = df[df['hours-per-week'] == min_work_hours]
    # Contar el número de personas que trabajan el número mínimo de horas por semana y tienen un salario mayor a 50K
    num_min_workers_with_high_salary = min_work_df[min_work_df['salary'] == '>50K'].shape[0]
    # Calcular el número total de personas que trabajan el número mínimo de horas por semana
    num_min_workers = min_work_df.shape[0]

    num_min_workers = (num_min_workers_with_high_salary / num_min_workers) * 100

    rich_percentage = rich_percentage = 100 - (higher_education_rich + lower_education_rich)

    # What country has the highest percentage of people that earn >50K?
    earning_by_country = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = earning_by_country.idxmax()
    highest_earning_country_percentage =earning_by_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation =df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode().values[0]

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
