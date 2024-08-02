import json


# Convert strings to list, add image into list
def to_list(text: str) -> list[str]:
    lines = text.splitlines()
    return lines


# Create an Album instance and convert it to a dictionary
def to_dict(album: list, holder_dataset: list, dataclass):
    holder_dataset.append(dataclass(*album).__dict__)


## Write holder list into json file
def write_json(data_array: list, path: str):
    with open(path, "w") as file:
        json.dump(data_array, file, indent=4)
