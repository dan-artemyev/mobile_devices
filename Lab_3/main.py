import constants
import csv
import os
import datetime
from math import ceil
from docx2pdf import convert
from docxtpl import DocxTemplate


def telephony(in_file, phone_number, out_call_k, in_call_k, free_sms, sms_k):
    with open(in_file, "r") as input_file:
        reader = csv.DictReader(input_file, delimiter=",")
        cost = 0
        out_calls = 0
        in_calls = 0
        sms = 0
        for row in reader:
            if row['msisdn_origin'] == phone_number:
                out_call_duration = float(row['call_duration'])
                out_calls = out_call_duration * out_call_k
                sms_number = int(row['sms_number'])
                if sms_number > free_sms:
                    sms = (sms_number - free_sms) * sms_k
                else:
                    sms = 0
            if row['msisdn_dest'] == phone_number:
                in_call_duration = float(row['call_duration'])
                in_calls = in_call_duration * in_call_k
        calls = out_calls + in_calls
        constants.info['services'][0]['sum'] = calls
        constants.info['services'][1]['sum'] = sms
        constants.info['services'][0]['amount'] = "{0} / {1}".format(in_call_duration, out_call_duration)
        constants.info['services'][1]['amount'] = sms_number
        return calls, sms


def internet(in_file, billing_ip, price):
    with open(in_file, "r") as input_file:
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
        traffic = ceil(traffic * 8 / 2 ** 20)
        cost = price * traffic
        constants.info['services'][2]['amount'] = traffic
        constants.info['services'][2]['sum'] = cost
        return cost


def billing():
    call_costs, sms_costs = telephony(constants.csv_path_telephony, constants.phone_number, constants.out_call_k,
                                      constants.in_call_k, constants.free_sms, constants.sms_k)
    os.system("nfdump  -r {0} -o extended -o csv 'src ip {1} or dst ip {1}' > {2}"
              .format(constants.nfcapd_file, constants.billing_ip, constants.csv_path_internet))
    internet_costs = internet(constants.csv_path_internet, constants.billing_ip, constants.internet_price)

    constants.info['payment']['sum'] = call_costs + sms_costs + internet_costs
    constants.info['payment']['nds'] = (call_costs + sms_costs + internet_costs) * 0.2
    constants.info['payment']['services'] = len(constants.info['services'])

    doc = DocxTemplate(constants.template)
    doc.render(constants.info)
    doc.save(constants.result)
    convert(constants.result)


if __name__ == '__main__':
    billing()