import re
from hurricanes import data


# write your update damages function here:
def update_damages():
    updated_damages = []
    for amount in data.damages:
        power = 0
        if amount.find('M') != -1:
            power = 6
        elif amount.find('B') != -1:
            power = 7
        amount = re.sub(r'M|B$', '', amount)
        if amount != 'Damages not recorded':
            amount = round(float(amount) ** power, 0)
        updated_damages.append(amount)
    return updated_damages


# write your construct hurricane dictionary function here:
def create_hurricane_dict(updated_damages):
    hurricanes_dict = {}
    for index in range(34):
        hurricanes_dict[data.names[index]] = {
            "Name": data.names[index],
            "Month": data.months[index],
            "Year": data.years[index],
            "Max Sustained Wind": data.max_sustained_winds[index],
            "Areas Affected": data.areas_affected[index],
            "Damage": updated_damages[index],
            "Death": data.deaths[index]
        }
    return hurricanes_dict


# write your construct hurricane by year dictionary function here:
def hurricane_by_year(hurricanes_dict):
    year_dict = {}
    for hurricane in hurricanes_dict.values():
        if year_dict.get(hurricane.get("Year")):
            year_dict[hurricane.get("Year")].append(hurricane)
        else:
            year_dict[hurricane.get("Year")] = [hurricane]
    return year_dict


# write your count affected areas function here:
def affected_area_counts(hurricane_dict):
    counts = {}
    for hurricane in hurricane_dict.values():
        for area in hurricane.get("Areas Affected"):
            if counts.get(area):
                counts[area] += 1
            else:
                counts[area] = 1
    return counts


# write your find most affected area function here:
def most_affected_area(area_counts):
    max_area = ''
    max_count = 0
    for key, value in area_counts.items():
        if value > max_count:
            max_count = value
            max_area = key
    return max_area, max_count


# write your greatest number of deaths function here:
def most_deaths(hurricane_dict):
    hurricane = ''
    death_count = 0
    for key, value in hurricane_dict.items():
        if value.get("Death") > death_count:
            hurricane = key
            death_count = value.get("Death")
    return hurricane, death_count


# write your categorize by mortality function here:
def mortality_scale(hurricane_dict):
    mortality = {}
    for value in hurricane_dict.values():
        rating = 5
        for scale_key, scale_value in data.mortality_scale.items():
            if value.get("Death") <= scale_value:
                rating = scale_key
                break
        if mortality.get(rating):
            mortality[rating].append(value)
        else:
            mortality[rating] = [value]
    return mortality


# write your greatest damage function here:
def greatest_damage(hurricane_dict):
    hurricane = ''
    most_damage = 0
    for key, value in hurricane_dict.items():
        if value.get("Damage") == "Damages not recorded":
            continue
        elif value.get("Damage") > most_damage:
            hurricane = key
            most_damage = value.get("Damage")
    return hurricane, most_damage


# write your categorize by damage function here:
def damage_scale(hurricane_dict):
    damages = {}
    for value in hurricane_dict.values():
        rating = 5
        if value.get("Damage") == "Damages not recorded":
            continue
        else:
            for scale_key, scale_value in data.damage_scale.items():
                if value.get("Damage") <= scale_value:
                    rating = scale_key
                    break
            if damages.get(rating):
                damages[rating].append(value)
            else:
                damages[rating] = [value]
    return damages
