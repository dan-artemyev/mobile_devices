import csv
import os
from math import ceil
import matplotlib.pyplot as plt
import datetime

billing_ip = "217.15.20.194"
nfcapd_file = "nfcapd.202002251200"
price = 0.5


def billing(input_file):
    traffic = 0
    reader = csv.DictReader(input_file, delimiter=",")
    dots_list = []
    for row in reader:
        if row['da'] == billing_ip:
            traffic += int(row['ibyt'])
            if row['ts'] == "Summary":
                break
            else:
                dot = (datetime.datetime.strptime(row['ts'], '%Y-%m-%d %H:%M:%S'), int(row['ibyt']))
                dots_list.append(dot)
    traffic = ceil(traffic / (2**20))
    cost = price * traffic
    print("Ip 217.15.20.194 used {0}Mb and have to pay {1} rubles.".format(traffic, cost))
    dots_list_sorted = sorted(dots_list, key=lambda time: time[0])
    bytes_list = []
    time_list = []
    for dot in dots_list_sorted:
        bytes_list.append(dot[1] / (2**20))
        time_list.append(dot[0])
    plt.plot
    fig, graph = plt.subplots()
    graph.plot(time_list, bytes_list, label='Traffic usage in Mb')
    graph.legend(loc='upper left')
    graph.grid()
    graph.set_xlabel('Time')
    graph.set_ylabel('Mb')
    graph.set_title('Dependence of traffic volume on time')
    plt.savefig('graph.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    csv_path = "lab2.csv"
    os.system(
        "nfdump  -r {0} -o extended -o csv 'src ip {1} or dst ip {1}' > {2}".format(nfcapd_file, billing_ip, csv_path))
    with open(csv_path, "r") as in_file:
        billing(in_file)
