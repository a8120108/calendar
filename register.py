import csv
import sys
# coding: -*- utf-8 -*-


def makeFile():
    header = ["アルバイト名", "時給"]
    body = []

    with open("jobdata.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)
    print("congrtulation")
    f.close()


makeFile()
print(sys.getdefaultencoding())
