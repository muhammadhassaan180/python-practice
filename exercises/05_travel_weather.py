# freeCodeCamp python-v9 — Python Basics
# Lab: Travel Weather Planner
# This is a lab: I write the code myself from the requirements.
distance_mi=0
is_raining=False
has_bike=False
has_car=False
has_ride_share_app=False
if not distance_mi:
    print(False)
elif distance_mi<=1 and is_raining==False:
    print('True')
elif distance_mi>1 and distance_mi<=6 and has_bike==True and is_raining==False:
    print('True')
elif distance_mi>6 and (has_car==True or has_ride_share_app==True):
    print('True')
elif distance_mi== False:
    print('False')
else:
    print('False')