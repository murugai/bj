from point_calculation import point_calc


def disp_list_point(ins_someone_info):

    tuple_sum_point = point_calc(ins_someone_info)
    for i in range(len(tuple_sum_point)):
        print(tuple_sum_point[i], end="")

        if (i+1 != len(tuple_sum_point)):  # Aを含むカードの合計の値は2つになる時があるのでその際の表記について
            print("/", end="")

    print("")
    return tuple_sum_point


def disp_point_of_someone(name, ins_someone_info):
    print(name + "の得点は")
    tuple_sum_point = disp_list_point(ins_someone_info)
    return tuple_sum_point
