from planner import community_details

from growth import future_demand

from sustainability import score,category

from iot_nodes import sensor_data

from recommendation import suggest



name,ctype,houses,use,backup,growth=community_details()



daily=houses*use



future=future_demand(

            daily,

            growth

            )



health=score(backup,growth)

level = category(health)

tips = suggest(
    health,

    backup,

    growth
    )


solar,battery,load,weather,temp=sensor_data()

print("\n")

print("====== TERRAVOLT REPORT ======")



print("\nCommunity")

print(name)



print("\nType")

print(ctype)


print("\nPresent Demand")

print(round(daily,2),"kWh")


print("\nFuture Demand")

print(round(future,2),"kWh")


print("\nSustainability Score")

print(health,"/100")


print()

print("\nCategory")

print(level)


print("\nRecommendation")

for item in tips:

    print("-",item)

print("\nDigital Twin")

print("Solar Node :",solar,"kW")

print("Battery Node :",battery,"%")

print("Load Node :",load,"kW")

print("Weather :",weather)

print("Temperature :",temp,"C")

file=open(

"community_history.txt",

"a"

)


file.write(

f"\n{name}|"

f"{daily}|"

f"{future}|"

f"{health}"

)

file.close()

print("\nPlan Saved")

print("\n========================")

