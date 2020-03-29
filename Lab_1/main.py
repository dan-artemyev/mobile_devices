import csv

phone_number = "915783624"
out_call_k = 2
in_call_k = 0
free_sms = 10
sms_k = 1


def billing(input_file):
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
    cost = out_calls + in_calls + sms
    print("------------\nUser {0} have to pay {1}".format(phone_number, cost))


if __name__ == '__main__':
    csv_path = "data.csv"
    with open(csv_path, "r") as in_file:
        billing(in_file)
