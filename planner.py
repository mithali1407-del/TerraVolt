# planner.py

def community_details():

    print("\n========== TerraVolt ==========")
    print("Designing Tomorrow's Communities")
    print("================================")

    name = input("Community Name : ")

    ctype = input(
        "Type (Village/Hostel/Campus/Society) : "
    )

    houses = int(
        input("Number of Homes : ")
    )

    daily_use = float(
        input("Average Daily Consumption per Home (kWh): ")
    )

    backup = float(
        input("Desired Backup Hours : ")
    )

    growth = float(
        input("Expected Growth (%) : ")
    )

    return (
        name,
        ctype,
        houses,
        daily_use,
        backup,
        growth
    )