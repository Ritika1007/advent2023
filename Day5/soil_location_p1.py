def make_mapping(source,line_num) -> list:
    mapping_dict = {}
    i=line_num
    print(i)
    line = data[i].strip()

    while line:
        mapping = list(map(int, line.split(' ')))
        
        dest_range = (mapping[0],mapping[0]+mapping[2])
        source_range = (mapping[1],mapping[1]+mapping[2])
        mapping_dict[source_range] = dest_range
        i+=1
        line = data[i].strip()
    # print(mapping_dict)
    res_map = {}
    for s in source:
        for key in mapping_dict.keys():
            if s >=key[0] and s < key[1]:
                diff = s - key[0]
                # print(s,key)
                soil_no = mapping_dict[key][0] + diff
                res_map[s] = soil_no
        if s not in res_map:
            res_map[s] = s

    return([list(res_map.values()), i])
          
with open('testcase.txt') as file:
    data = file.readlines()
    dict_map = {} 
    i=0
    while i<len(data):
        line = data[i].strip()

        if line.startswith('seeds'):
            #seeds to fertilize
            seeds = list(map(int, line.split(':')[1].strip().split(' ')))
            # print(seeds)

        elif line.startswith('seed-to-soil'):
            soil_map, i = make_mapping(seeds,i+1)
            print("soil mapped")
            print(soil_map,i)
        
        elif line.startswith('soil-to-fertilizer'):
            fert_map, i = make_mapping(soil_map,i+1)
            print("fertilizer mapped")
            print(fert_map,i)
        
        elif line.startswith('fertilizer-to-water'):
            water_map, i = make_mapping(fert_map,i+1)
            print("water mapped")
            print(water_map,i)

        elif line.startswith('water-to-light'):
            light_map, i = make_mapping(water_map,i+1)
            print("light mapped")
            print(light_map,i)
        
        elif line.startswith('light-to-temperature'):
            temp_map, i = make_mapping(light_map,i+1)
            print("temprature mapped")
            print(temp_map,i)
        
        elif line.startswith('temperature-to-humidity'):
            humidity_map, i = make_mapping(temp_map,i+1)
            print("humidity mapped")
            print(humidity_map,i)
        
        elif line.startswith('humidity-to-location'):
            location_map, i = make_mapping(humidity_map,i+1)
            print("location mapped")
            print(location_map)

            location_map.sort()
            print('minimum', location_map[0])
            break
            
                
                

        i+=1
            



            
