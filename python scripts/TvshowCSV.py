import csv
import sys
maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True


def createCSV():
    with open('title_basics.csv','r', encoding='utf-8', newline='') as cin:
        with open('tvShow.csv','w', encoding='utf-8', newline='') as cout:

            csv_in = csv.reader(cin)
            csv_out = csv.writer(cout, delimiter=',')
            type_set = {'tvSpecial', 'tvShort','tvEpisode','tvMiniSeries','tvSeries','titleType'}
            for row in csv_in:
                if row[1] in type_set:
                    list = []
                    list.append(row[0])
                    list.append(row[5])
                    list.append(row[6])
                    csv_out.writerow(list)


if __name__ == "__main__":
    createCSV()