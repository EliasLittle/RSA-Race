import csv


with open('Lockers.csv', mode='r') as csv_file:
    m = csv.reader(csv_file)
    temp = []
    for row in m:
        temp.append(row)
    transpose = [[temp[j][i]
                  for j in range(len(temp))] for i in range(len(temp[0]))]

lockers = {}
for i in range(1, len(transpose)):
    j = 1
    while transpose[i][j] != '' and j < len(transpose[i]):
        key = transpose[i][0] + transpose[0][j]
        val = transpose[i][j]
        a, b = int(val[0:4]), int(val[5:])
        if a == '':
            print(a)
        lockers[key] = [a, b]
        j += 1
        if j == len(transpose[i]):
            break


# for key in lockers:
    # print(key + " "+str(lockers[key]))


def test(number):
    number = int(number)
    for key in lockers:
        a, b = lockers[key][0], lockers[key][1]
        if number > a and number < b:
            return key
