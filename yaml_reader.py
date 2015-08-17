import yaml
class yld:
        def __init__ (self):
                data = {}
                
        def yaml_loader(filepath):
                """Loads a yaml file"""
                with open(filepath, "r") as file_descriptor:
                        data = yaml.load(file_descriptor)
                return data

        def ymal_dump(filepath, data):
                """Dump data to a yaml file"""
                with open(filepath, "w") as file_desxriptor:
                        yaml.dump(data, file_descriptor)
"""
if __name__ == "__main__":
	filepath = "config.yaml"
	data = yaml_loader(filepath)
	print (data)
	dbInfo = data.get("dbInfo")
	for item_name, item_value in dbInfo.items():
		print (item_name, item_value)
"""
