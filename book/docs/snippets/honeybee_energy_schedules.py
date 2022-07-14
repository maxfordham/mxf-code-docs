# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # [honeybee-energy schedules](https://www.ladybug.tools/honeybee-energy/docs/honeybee_energy.schedule.html)

# +
"""
make usage schedules from honeybee_energy

Reference:
    https://www.ladybug.tools/honeybee-energy/docs/honeybee_energy.schedule.html
"""

from honeybee_energy.schedule.typelimit import ScheduleTypeLimit
from honeybee_energy.schedule.day import ScheduleDay
from honeybee_energy.schedule.rule import ScheduleRule
from honeybee_energy.schedule.ruleset import ScheduleRuleset
# -

di_day = {
"type": 'ScheduleDay',
"identifier": 'Office_Occ_900_1700',
"display_name": 'Office Occupancy',
"values": [0, 1, 0],
"times": [(0, 0), (9, 0), (17, 0)],
"interpolate": False
}
day = ScheduleDay.from_dict(di_day)
day.to_dict()

# +
di_rule = {
    "type": 'ScheduleRule',
    "schedule_day": day.to_dict(),
    "apply_sunday": False,
    "apply_monday": True,
    "apply_tuesday": True,
    "apply_wednesday": True,
    "apply_thursday": True,
    "apply_friday": True,
    "apply_saturday": False,
    "start_date": (1, 1),
    "end_date": (12, 31)
}

s = ScheduleRule.from_dict(di_rule)
# -

di_tl = {
    "type": 'ScheduleTypeLimit',
    "identifier": 'Fractional',
    "display_name": 'Fractional',
    "lower_limit": 0,
    "upper_limit": 1,
    "numeric_type": "Discrete",
    "unit_type": "Dimensionless",
}
stl = ScheduleTypeLimit.from_dict(di_tl)
stl.to_dict()

di_ruleset = {
"type": 'ScheduleRuleset',
"identifier": 'Office_Occ_900_1700_weekends',
"display_name": 'Office Occupancy',
"day_schedules": [day.to_dict()], # Array of ScheduleDay dictionary representations
"default_day_schedule": "Office_Occ_900_1700", # ScheduleDay identifier
"schedule_rules": [s.to_dict(abridged=True)], # list of ScheduleRuleAbridged dictionaries
"schedule_type_limit": stl.to_dict(), # ScheduleTypeLimit dictionary representation
"holiday_schedule": "Office_Occ_900_1700", # ScheduleDay identifier
"summer_designday_schedule": "Office_Occ_900_1700", # ScheduleDay identifier
"winter_designday_schedule": "Office_Occ_900_1700" # ScheduleDay identifier
}
ss = ScheduleRuleset.from_dict(di_ruleset)
ss.data_collection()


