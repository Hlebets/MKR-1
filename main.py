print("Модульна Контрольна Робота - 1")
print("Гліб Кобрин, ІКСМ-1, Навчальна Група №2")

massive = [
    [45, 1, 29, 3, 9],
    [7, 13, 21, 4, 8],
    [44, 8, 6, 3, 30],
    [1, 3, 72, 29, 0],
    [9, 12, 13, 3, 7],
]

sums_and_rows = [(sum(row), row) for row in massive]

sort_sum_rows = sorted(sums_and_rows, key=lambda x: x[0])

sorted_massive = [row for _, row in sort_sum_rows]
print("\nВідсортовані суми рядків по зростанню:")
for row in sorted_massive:
    print(sum(row))

print("\nВідсортовані рядки по зростанню")
for row in sorted_massive:
    print(row)
