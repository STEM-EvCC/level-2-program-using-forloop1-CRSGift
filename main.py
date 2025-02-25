#Level 2: Program with For Loop

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#Counts the total number of space missions
missions_quantity = len(mission_names)
print("Total number of missions: "+str(missions_quantity))

#Counts the number of successful missions
missions_successful_quantity = sum(True for _ in mission_success if _)
print("Number of successful missions: "+str(missions_successful_quantity))

#Calculates the success rate of the missions
success_rate = (missions_successful_quantity/missions_quantity)*100
print("Success rate: "+str(round(success_rate, 2))+"%")

#Lists all the missions that were launched before the year 2000
missions_pre2000 = []
for year in range(len(mission_years)):
    if mission_years[year] < 2000:
        missions_pre2000.append(mission_names[year])
print("Missions launched before the year 2000:\n- "+"\n- ".join(missions_pre2000))