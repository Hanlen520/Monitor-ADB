import math


class ManageReport:
    def __init__(self, wd, st):
        self.wd = wd
        self.st = st

    def unit_format(self):
        self.wd.add_format({'align': 'center', 'bold': True})

    def gen_chart(self, data):
        self.st.write('A1', 'cpu(%)', self.unit_format())
        self.st.write('B1', 'men(M)', self.unit_format())
        temp = 2
        for item in data['cpu']:
            self.st.write('A' + str(temp), item)
            temp += 1
        temp = 2
        for item in data['men']:
            self.st.write('B' + str(temp), math.ceil(item/1024))
            temp += 1
        self.plot("cpu", len(data["cpu"]))
        self.plot("men", len(data["men"]))

    def plot(self, date_type, len_data):
        values = ""
        row = ""
        title = ""
        if date_type == "cpu":
            values = '=详细信息!$A$2:$A$' + str(len_data + 1)
            row = 'D1'
            title = "CPU使用率%"
        elif date_type == "men":
            values = '=详细信息!$B$2:$B$' + str(len_data + 1)
            row = 'D18'
            title = "内存使用MB"
        new_chart = self.wd.add_chart({'type': 'line'})
        new_chart.add_series({
            'values': values
        })
        new_chart.set_title({'name': title})
        self.st.insert_chart(row, new_chart)

    def close(self):
        self.wd.close()
