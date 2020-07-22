from hurricanes import hurricane_analysis
from hurricanes import  data

updated_damages = hurricane_analysis.update_damages()
hurricane_dict = hurricane_analysis.create_hurricane_dict(updated_damages)
print(hurricane_dict)
year_dict = hurricane_analysis.hurricane_by_year(hurricane_dict)
print(year_dict)
counts = hurricane_analysis.affected_area_counts(hurricane_dict)
print(counts)
print(hurricane_analysis.most_affected_area(counts))
print(hurricane_analysis.most_deaths(hurricane_dict))
mortality = hurricane_analysis.mortality_scale(hurricane_dict)
print(mortality)
print(hurricane_analysis.greatest_damage(hurricane_dict))
damage = hurricane_analysis.damage_scale(hurricane_dict)
print(damage)


