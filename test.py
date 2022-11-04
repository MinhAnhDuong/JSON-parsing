import json

with open("sample-data.json","r") as file:
    list_data = json.load(file)

    for virtual_machine_cfg in list_data:
        try:
            #name
            print("------------------------------------")
            name = virtual_machine_cfg["name"]
            print(f"name: {name}")

            #cpu
            cpu = virtual_machine_cfg["state"]["cpu"]["usage"]
            print(f"CPU: {cpu}")

            #memory_usage
            memory_usage = virtual_machine_cfg["state"]["memory"]["usage"]
            print(f"memory usage: {memory_usage}")

            #date
            date_of_create = virtual_machine_cfg["created_at"]
            print(f"date: {date_of_create}")

            #status
            status = virtual_machine_cfg["status"]
            print(f"status: {status}")

        except TypeError:
            print("data not found")