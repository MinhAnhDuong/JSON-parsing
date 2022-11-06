import json

from datetime import datetime, timezone


def convert_time(json_date):
    date = json_date
    date_stript = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
    timestamp = date_stript.replace(tzinfo=timezone.utc).timestamp()
    return timestamp


class MyFilter:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.list_of_vms = list()
        self.name = str()
        self.memory_usage = int()
        self.status = str()
        self.date = str()
        self.cpu = int()
        self.address = str()
        self.vm = (
            self.name,
            self.memory_usage,
            self.status,
            self.date,
            self.cpu,
            self.address,
        )

    def filter(self):
        with open(self.path_to_file, "r") as file:
            list_data = json.load(file)

            for virtual_machine_cfg in list_data:
                try:
                    name = virtual_machine_cfg["name"]
                    self.name = name
                except (KeyError, TypeError):
                    self.name = "value not found"

                try:
                    cpu = virtual_machine_cfg["state"]["cpu"]["usage"]
                    self.cpu = cpu
                except (KeyError, TypeError):
                    self.cpu = "value not found"

                try:
                    memory_usage = virtual_machine_cfg["state"]["memory"]["usage"]
                    self.memory_usage = memory_usage
                except (KeyError, TypeError):
                    self.memory_usage = "value not found"

                try:
                    date_of_create = virtual_machine_cfg["created_at"]
                    utc_date = convert_time(date_of_create)
                    self.date = utc_date
                except (KeyError, TypeError):
                    self.date = "value not found"

                try:
                    status = virtual_machine_cfg["status"]
                    self.status = status
                except (KeyError, TypeError):
                    self.status = "value not found"

                try:
                    networks = virtual_machine_cfg["state"]["network"]
                    list_of_address = []

                    for network in networks:
                        addresses = virtual_machine_cfg["state"]["network"][network]["addresses"]

                        for address in addresses:
                            list_of_address.append(address["address"])
                            self.address = list_of_address
                except (KeyError, TypeError):
                    self.address = "value not found"

                self.vm = (self.name, self.cpu, self.memory_usage, self.date, self.status, self.address)
                self.list_of_vms.append(self.vm)

        return self.list_of_vms


test_filter = MyFilter("sample-data.json")
filtered_data = test_filter.filter()