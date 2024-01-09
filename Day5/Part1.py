# full_input = open("test.txt").read().strip().split('\n')
full_input = open("input.txt").read().strip().split('\n')

grouped_input = [[]]

for line in full_input:
    if line == '':
        grouped_input.append([])
    else:
        grouped_input[-1].append(line)

# 0 -> seeds
# 1 -> seed to soil
# 2 -> soil to fertilizer
# 3 -> fertilizer to water
# 4 -> water to light
# 5 -> light to temperature
# 6 -> temperature to humidity
# 7 -> humidity to location

seeds = list(map(int, grouped_input[0][0].split()[1:]))
print("Seeds:", seeds)

def create_mapping(val_arr):
    mapping = []
    for t in val_arr:
        val = list(map(int, t.split()))
        mapping.append([val[1], val[1]+val[2]-1, val[0]-val[1]])
    return mapping

seed_to_soil_map = create_mapping(grouped_input[1][1:])
soil_to_fert_map = create_mapping(grouped_input[2][1:])
fert_to_wate_map = create_mapping(grouped_input[3][1:])
wate_to_ligh_map = create_mapping(grouped_input[4][1:])
ligh_to_temp_map = create_mapping(grouped_input[5][1:])
temp_to_humi_map = create_mapping(grouped_input[6][1:])
humi_to_loca_map = create_mapping(grouped_input[7][1:])

def convert_to_dest(val, mapping):
    for mp in mapping:
        if val>=mp[0] and val<=mp[1]:
            val += mp[2]
            break
    return val

locations = []
for x in seeds:
    x = convert_to_dest(x, seed_to_soil_map)
    x = convert_to_dest(x, soil_to_fert_map)
    x = convert_to_dest(x, fert_to_wate_map)
    x = convert_to_dest(x, wate_to_ligh_map)
    x = convert_to_dest(x, ligh_to_temp_map)
    x = convert_to_dest(x, temp_to_humi_map)
    x = convert_to_dest(x, humi_to_loca_map)
    locations.append(x)

print("Locations:", locations)
print("Min Location:", min(locations))

