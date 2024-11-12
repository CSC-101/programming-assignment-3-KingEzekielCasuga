from data import CountyDemographics

# Task 1

# takes in a list of counties and returns their population total

def population_total(counties:list[CountyDemographics]) -> int:
    count = 0
    for county in counties:
        count = count + county.population['2014 Population']
    return count

# Task 2

# takes in a list of counties and a string representing a state
# and returns the list of counties in that state from the original list

def filter_by_state(counties:list[CountyDemographics], state:str) -> list[CountyDemographics]:
    states = []
    for county in counties:
        if state == county.state:
            states.append(county)
    return states

# Task 3
#population by education

# takes in a list of counties and an education level and returns the
# population of people with that education level within the counties

def population_by_education(counties:list[CountyDemographics], education_level:str) -> float:
    county_education = 0
    for county in counties:
        if education_level in county.education:
            county_education += (county.education[education_level]/100) * county.population['2014 Population']
    return county_education

#population by ethnicity

# takes in a list of counties and an ethnicity and returns the
# population of people with that ethnicity within the counties

def population_by_ethnicity(counties:list[CountyDemographics], ethnicity:str) -> float:
    county_ethnicity = 0
    for county in counties:
        if ethnicity in county.ethnicities:
            county_ethnicity += (county.ethnicities[ethnicity]/100) * county.population['2014 Population']
    return county_ethnicity

#population below poverty level

# takes in a list of counties and returns the population of people below the poverty level

def population_below_poverty_level(counties:list[CountyDemographics]) -> float:
    county_below_population = 0
    for county in counties:
        county_below_population += (county.income['Persons Below Poverty Level']/100) * county.population['2014 Population']
    return county_below_population

# Task 4
#percent by education

# takes in a list of counties and an education level and returns the
# average education level population of the entire county list

def percent_by_education(counties:list[CountyDemographics], education_level:str) -> float:
    county_education = 0
    county_count = 0
    for county in counties:
        if education_level in county.education:
            county_count += 1
            county_education += county.education[education_level]
        else:
            county_count += 1
    return county_education/county_count

# percent by ethnicity

# takes in a list of counties and an ethnicity and returns the
# average ethnicity population of the entire county list

def percent_by_ethnicity(counties:list[CountyDemographics], ethnicity:str) -> float:
    county_ethnicity = 0
    county_count = 0
    for county in counties:
        if ethnicity in county.ethnicities:
            county_count += 1
            county_ethnicity += county.ethnicities[ethnicity]
        else:
            county_count += 1
    return county_ethnicity/county_count

# percent below poverty level

# takes in a list of counties and returns the percent below poverty level
# of the entire list

def percent_below_poverty_level(counties:list[CountyDemographics]) -> float:
    county_below_population = 0
    county_count = 0
    for county in counties:
        county_below_population += county.income['Persons Below Poverty Level']
        county_count += 1
    return county_below_population/county_count

# Task 5
# education greater than

# takes in a list of counties, an education level, and a threshold percentage
# and returns a list of counties that are above the threshold

def education_greater_than(counties:list[CountyDemographics], education_level:str, threshold:float) -> list[CountyDemographics]:
    education_list = []
    for county in counties:
        if education_level in county.education:
            if threshold < county.education[education_level]:
                education_list.append(county)
    return education_list

# education less than

# takes in a list of counties, an education level, and a threshold percentage
# and returns a list of counties that are below the threshold

def education_less_than(counties:list[CountyDemographics], education_level:str, threshold:float) -> list[CountyDemographics]:
    education_list = []
    for county in counties:
        if education_level in county.education:
            if threshold > county.education[education_level]:
                education_list.append(county)
    return education_list

# ethnicity greater than

# takes in a list of counties, an ethnicity, and a threshold percentage
# and returns a list of counties that are above the threshold

def ethnicity_greater_than(counties:list[CountyDemographics], ethnicity:str, threshold:float) -> list[CountyDemographics]:
    ethnicity_list = []
    for county in counties:
        if ethnicity in county.ethnicities:
            if threshold < county.ethnicities[ethnicity]:
                ethnicity_list.append(county)
    return ethnicity_list

# ethnicity less than

# takes in a list of counties, an ethnicity, and a threshold percentage
# and returns a list of counties that are below the threshold

def ethnicity_less_than(counties:list[CountyDemographics], ethnicity:str, threshold:float) -> list[CountyDemographics]:
    ethnicity_list = []
    for county in counties:
        if ethnicity in county.ethnicities:
            if threshold > county.ethnicities[ethnicity]:
                ethnicity_list.append(county)
    return ethnicity_list

# below poverty level greater than

# takes in a list of counties and a threshold percentage
# and returns a list of counties that are above the threshold

def below_poverty_level_greater_than(counties:list[CountyDemographics], threshold:float) -> list[CountyDemographics]:
    county_below_list = []
    for county in counties:
        if threshold < county.income['Persons Below Poverty Level']:
            county_below_list.append(county)
    return county_below_list

# below poverty level less than

# takes in a list of counties and a threshold percentage
# and returns a list of counties that are below the threshold

def below_poverty_level_less_than(counties:list[CountyDemographics], threshold:float) -> list[CountyDemographics]:
    county_below_list = []
    for county in counties:
        if threshold > county.income['Persons Below Poverty Level']:
            county_below_list.append(county)
    return county_below_list