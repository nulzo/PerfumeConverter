#Author: Nolan Gregory
#
#Purpose: While developing perfumes, I design them in terms
#         of percentages. This program then converts those
#         percentages to grams of each raw chemical.

import csv

def getData(filename):
    """This function gathers data from a CSV file and converts
    it to a dictionary for use"""
    data_dict = {}
    try:
        with open(filename, "r") as data:
            reader = csv.reader(data)
            for chem in reader:
                data_dict[f"{chem[0]}"] = chem[1]
        return data_dict
    except FileNotFoundError:
        print()
        print(f'\x1b[38;5;124m' + str("FILE NOT FOUND") + u'\u001b[0m')
        return None

def convertGrams():
    """This function gathers how many grams total the user wants"""
    amount = float(input("\nHow many grams total would you like?: "))
    return amount

def converter(data, amount):
    """This function converts the total into grams and prints it/saves it"""
    total = 0
    percent = 0
    new_dict = {}
    print(f"\nTotal chemicals: {len(data)}\n")
    for chem, perc in data.items():
        percent = float(perc) * (amount / 100)
        print(f"{chem:<30}: {percent:.4f}g")
        new_dict["chem"] = percent
        total += percent
    print(f"\n{'Total':<30}: {round(total):.2f}g")
    return new_dict

def main():
    while True:
        filename = input("\nWhat is the name of the file (including file type; Case sensitive): ")
        data = getData(f"data/{filename}")
        cont = 'y'
        if data:
            amount = convertGrams()
            new_data = converter(data, amount)
            #TODO: add function to save new data to csv
        cont = input("\nContinue: (y/n): ").lower()
        while cont != 'y' and cont != 'n':
            print(f'\x1b[38;5;124m' + str("INVALID INPUT") + u'\u001b[0m')
            cont = input("Continue: (y/n): ").lower()
        if cont == "n":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
