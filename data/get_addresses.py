import pandas as pd

def load_addresses(data_filepath):

    addresses = pd.read_csv(data_filepath)

    return addresses

def write_to_file(addresses_filepath, addresses):

    columns = ["address","city"]
    df = pd.DataFrame(columns=columns)

    samples = addresses.sample(n=25)
    samples = samples.loc[:, samples.columns.intersection(['betegnelse'])]

    str_addresses = samples['betegnelse'].tolist()

    dicts = []
    for str_address in str_addresses:
        address = ""
        for x in str_address.split(",")[:-1]:
            address += f"{x} "
            address.strip()

        city = str_address.split(",")[-1]
        city.strip()

        dicts.append({'address': address, 'city': city})

    df = df.append(dicts, ignore_index=True, sort=False)
    df.to_csv(addresses_filepath)

    return

if __name__ == "__main__":
    data_filepath = "all_addresses.csv"
    addresses_filepath = "addresses.csv"

    addresses = load_addresses(data_filepath)
    write_to_file(addresses_filepath, addresses)



