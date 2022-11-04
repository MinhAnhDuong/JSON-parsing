import json

with open("sample-data.json","r") as file:
    list_data = json.load(file)

    for virtual_machine_cfg in list_data:
        try:
            print("------------------------------------")

            name = virtual_machine_cfg["name"]
            print(f"name: {name}")
        except (KeyError, TypeError):
            print("name: value not found")

        try:
            cpu = virtual_machine_cfg["state"]["cpu"]["usage"]
            print(f"CPU: {cpu}")
        except (KeyError, TypeError):
            print("CPU: value not found")

        try:
            memory_usage = virtual_machine_cfg["state"]["memory"]["usage"]
            print(f"memory usage: {memory_usage}")
        except (KeyError, TypeError):
            print("memory usage: value not found")

        try:
            date_of_create = virtual_machine_cfg["created_at"]
            print(f"date: {date_of_create}")
        except (KeyError, TypeError):
            print("date: value not found")

        try:
            status = virtual_machine_cfg["status"]
            print(f"status: {status}")
        except (KeyError, TypeError):
            print("status: value not found")

        try:
            networks = virtual_machine_cfg["state"]["network"]

            for network in networks:
                addresses = virtual_machine_cfg["state"]["network"][network]["addresses"]

                for address in addresses:
                    print(f"address: {address['address']}")
        except (KeyError, TypeError):
            print("address: value not found")