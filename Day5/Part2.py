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
seeds = [[x[0], x[0]+x[1]] for x in zip(seeds[0::2], seeds[1::2])]
print("Seeds:", seeds)

def create_mapping(val_arr):
    mapping = []
    for t in val_arr:
        val = list(map(int, t.split()))
        mapping.append([val[1], val[1]+val[2]-1, val[0]-val[1]])
    mapping.sort(key=lambda x : x[0])
    return mapping

seed_to_soil_map = create_mapping(grouped_input[1][1:])
soil_to_fert_map = create_mapping(grouped_input[2][1:])
fert_to_wate_map = create_mapping(grouped_input[3][1:])
wate_to_ligh_map = create_mapping(grouped_input[4][1:])
ligh_to_temp_map = create_mapping(grouped_input[5][1:])
temp_to_humi_map = create_mapping(grouped_input[6][1:])
humi_to_loca_map = create_mapping(grouped_input[7][1:])

def convert_to_dest_range(inp_range, mapping):
    out_range = []
    for mp in mapping:
        if inp_range[0]>=mp[0] and inp_range[0]<=mp[1]:
            s = inp_range[0] + mp[2]
            if inp_range[1]<=mp[1]:
                e = inp_range[1] + mp[2]
                out_range.append([s, e])
                return out_range
            else:
                e = mp[1] + mp[2]
                out_range.append([s, e])
                inp_range = [mp[1]+1, inp_range[1]]

    out_range.append(inp_range)
    return out_range

soil_range = []
fert_range = []
wate_range = []
ligh_range = []
temp_range = []
humi_range = []
loca_range = []

for seed in seeds:
    soil_range.extend(convert_to_dest_range(seed, seed_to_soil_map))

# print(seed_to_soil_map)
# print(soil_range)

for soil in soil_range:
    fert_range.extend(convert_to_dest_range(soil, soil_to_fert_map))

# print(soil_to_fert_map)
# print(fert_range)

for fert in fert_range:
    wate_range.extend(convert_to_dest_range(fert, fert_to_wate_map))

# print(fert_to_wate_map)
# print(wate_range)

for wate in wate_range:
    ligh_range.extend(convert_to_dest_range(wate, wate_to_ligh_map))

for ligh in ligh_range:
    temp_range.extend(convert_to_dest_range(ligh, ligh_to_temp_map))

for temp in temp_range:
    humi_range.extend(convert_to_dest_range(temp, temp_to_humi_map))

for humi in humi_range:
    loca_range.extend(convert_to_dest_range(humi, humi_to_loca_map))

# print(loca_range)
loca_range_start = [x[0] for x in loca_range]
print(min(loca_range_start))

