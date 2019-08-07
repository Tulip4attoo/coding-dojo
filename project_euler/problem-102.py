import time

start_time = time.time()

data = open("p102_triangles.txt", "r")
temp_list = []
base_data = {}
n = 0

def calculate_distance(point_1, point_2):
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5

def calculate_area(sides_len_list):
    side_1 = calculate_distance(sides_len_list[0], sides_len_list[1])
    side_2 = calculate_distance(sides_len_list[0], sides_len_list[2])
    side_3 = calculate_distance(sides_len_list[1], sides_len_list[2])
    half_perimeter = (side_1 + side_2 + side_3) / 2.
    # print(side_1, side_2, side_3, half_perimeter)
    return (half_perimeter * (half_perimeter - side_1) * 
        (half_perimeter - side_2) * (half_perimeter - side_3)) ** 0.5

def is_contain_orgin(points_list, epsilon):
    total_area = calculate_area(points_list)
    part_area_1 = calculate_area([points_list[0], points_list[1],  [0, 0]])
    part_area_2 = calculate_area([points_list[0], points_list[2],  [0, 0]])
    part_area_3 = calculate_area([points_list[1], points_list[2],  [0, 0]])
    if part_area_1 + part_area_2 + part_area_3 - total_area < epsilon:
        return True
    else:
        return False

count = 0
epsilon = 10 ** (-5)
for line in data:
    str_points = line
    points_list = map(int, str_points.split(","))
    split_pt_list = [points_list[0 : 2], points_list[2 : 4], points_list[4 : 6]]
    if is_contain_orgin(split_pt_list, epsilon):
        count += 1

print(count)

print("--- %s seconds ---" % (time.time() - start_time))


