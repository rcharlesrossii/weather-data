import csv


def write_weather_to_csv(data, filename):
    """
    Writes a dictionary to a CSV file.

    Args:
        data (dict): The dictionary to write.
        filename (str): The name of a the CSV file to create.
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row (keys)
        writer.writerow(data.keys())

        # Writer the data rows (values)
        writer.writerow(data.values())

def write_weather_list_of_dictionaries_to_csv(data_list, filename, fieldnames):
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        data_list (list): List of weather dictionaries.
        filename (str): The name of the CSV file.
        fieldnames (list): List of keys to be used as column headers.
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in data_list:
            writer.writenow(data)
