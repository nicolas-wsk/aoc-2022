import os


# path = f'{os.path.dirname(__file__)}/inputs/11.txt'

monkeys = [[91, 66], [78, 97, 59], [57, 59, 97, 84, 72, 83, 56, 76], [81, 78, 70, 58, 84], [
    60], [57, 69, 63, 75, 62, 77, 72], [73, 66, 86, 79, 98, 87], [95, 89, 63, 67]]
sum = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

#  19 * 5 * 11 * 17 * 7 * 13 * 3 * 2 = 9699690
for _ in range(10000):
    for idx, i in enumerate(monkeys):
        for item in i[:]:
            itemIdx = monkeys[idx].index(item)
            monkeys[idx].pop(itemIdx)

            if idx == 0:
                sum[0] += 1
                item = int((item * 13))

                if item % 19 == 0:
                    monkeys[6].append(int(item % 9699690))
                else:
                    monkeys[2].append(int(item % 9699690))
            if idx == 1:
                sum[1] += 1
                item = int((item + 7))

                if item % 5 == 0:
                    monkeys[0].append(int(item % 9699690))
                else:
                    monkeys[3].append(int(item % 9699690))
            if idx == 2:
                sum[2] += 1
                item = int((item + 6))
                if item % 11 == 0:
                    monkeys[5].append(int(item % 9699690))
                else:
                    monkeys[7].append(int(item % 9699690))
            if idx == 3:
                sum[3] += 1
                item = int((item + 5))

                if item % 17 == 0:
                    monkeys[6].append(int(item % 9699690))
                else:
                    monkeys[0].append(int(item % 9699690))
            if idx == 4:
                sum[4] += 1
                item = int((item + 8))

                if item % 7 == 0:
                    monkeys[1].append(int(item % 9699690))
                else:
                    monkeys[3].append(int(item % 9699690))
            if idx == 5:
                sum[5] += 1
                item = int((item * 5))

                if item % 13 == 0:
                    monkeys[7].append(int(item % 9699690))
                else:
                    monkeys[4].append(int(item % 9699690))
            if idx == 6:
                sum[6] += 1
                item = int(item**2)

                if item % 3 == 0:
                    monkeys[5].append(int(item % 9699690))
                else:
                    monkeys[2].append(int(item % 9699690))
            if idx == 7:
                sum[7] += 1
                item = int((item + 2))

                if item % 2 == 0:
                    monkeys[1].append(int(item % 9699690))
                else:
                    monkeys[4].append(int(item % 9699690))

print(monkeys)
print(sum)

# 141054 * 140049 =  19754471646

# for _ in range(20):
#     for idx, i in enumerate(monkeys):
#         # print(i)
#         for item in i[:]:
#             # print(item)
#             itemIdx = monkeys[idx].index(item)
#             monkeys[idx].pop(itemIdx)
#             # print(item)
#             if idx == 0:
#                 sum[0] += 1
#                 item = int((item * 13) / 3)

#                 if item % 19 == 0:
#                     monkeys[6].append(int(item))
#                 else:
#                     monkeys[2].append(int(item))
#             if idx == 1:
#                 sum[1] += 1
#                 item = int((item + 7) / 3)

#                 if item % 5 == 0:
#                     monkeys[0].append(int(item))
#                 else:
#                     monkeys[3].append(int(item))
#             if idx == 2:
#                 sum[2] += 1
#                 item = int((item + 6) / 3)
#                 if item % 11 == 0:
#                     monkeys[5].append(int(item))
#                 else:
#                     monkeys[7].append(int(item))
#             if idx == 3:
#                 sum[3] += 1
#                 item = int((item + 5) / 3)

#                 if item % 17 == 0:
#                     monkeys[6].append(int(item))
#                 else:
#                     monkeys[0].append(int(item))
#             if idx == 4:
#                 sum[4] += 1
#                 item = int((item + 8) / 3)

#                 if item % 7 == 0:
#                     monkeys[1].append(int(item))
#                 else:
#                     monkeys[3].append(int(item))
#             if idx == 5:
#                 sum[5] += 1
#                 item = int((item * 5) / 3)

#                 if item % 13 == 0:
#                     monkeys[7].append(int(item))
#                 else:
#                     monkeys[4].append(int(item))
#             if idx == 6:
#                 sum[6] += 1
#                 item = int((item * item) / 3)

#                 if item % 3 == 0:
#                     monkeys[5].append(int(item))
#                 else:
#                     monkeys[2].append(int(item))
#             if idx == 7:
#                 sum[7] += 1
#                 item = int((item + 2) / 3)

#                 if item % 2 == 0:
#                     monkeys[1].append(int(item))
#                 else:
#                     monkeys[4].append(int(item))
