def task_1(level):
    level = int(level)
    count_of_triangles = 0
    for line_in_triangle in range(1, level + 1):
        sum_of_triangles = 0  # місце для збереження суми трикутників у поточному ряді трикутника
        amount_of_triangles = 0  # обчислення к-ті трикутників у кожній ітерації
        for i in range(line_in_triangle, level + 1):
            if i >= line_in_triangle * 2:
                amount_of_triangles = amount_of_triangles + 2
                sum_of_triangles = sum_of_triangles + amount_of_triangles
            else:
                amount_of_triangles = amount_of_triangles + 1
                sum_of_triangles = sum_of_triangles + amount_of_triangles
        count_of_triangles += sum_of_triangles

    print(count_of_triangles)