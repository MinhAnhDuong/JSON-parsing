import json


class MyFilter:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.list_of_vms = list()
        self.vm = {
            "name": str(),
            "memory_usage": int(),
            "status": str(),
            "date": str(),
            "cpu": int(),
            "address": list(),
        }

    def filter(self):
        with open(self.path_to_file, "r") as file:
            list_data = json.load(file)

            for virtual_machine_cfg in list_data:
                try:
                    name = virtual_machine_cfg["name"]
                    self.vm["name"] = name
                except (KeyError, TypeError):
                    self.vm["name"] = "value not found"

                try:
                    cpu = virtual_machine_cfg["state"]["cpu"]["usage"]
                    self.vm["cpu"] = cpu
                except (KeyError, TypeError):
                    self.vm["cpu"] = "value not found"

                try:
                    memory_usage = virtual_machine_cfg["state"]["memory"]["usage"]
                    self.vm["memory_usage"] = memory_usage
                except (KeyError, TypeError):
                    self.vm["memory_usage"] = "value not found"

                try:
                    date_of_create = virtual_machine_cfg["created_at"]
                    self.vm["date"] = date_of_create
                except (KeyError, TypeError):
                    self.vm["date"] = "value not found"

                try:
                    status = virtual_machine_cfg["status"]
                    self.vm["status"] = status
                except (KeyError, TypeError):
                    self.vm["status"] = "value not found"

                try:
                    networks = virtual_machine_cfg["state"]["network"]

                    for network in networks:
                        addresses = virtual_machine_cfg["state"]["network"][network]["addresses"]

                        for address in addresses:
                            self.vm["address"] = address["address"]
                except (KeyError, TypeError):
                    self.vm["address"] = "value not found"  

test_filter = MyFilter("sample-data.json")
filtered = test_filter.filter()
print(test_filter.vm)