import openpyxl
import pprint
import csv


def census_data():
    county_data = {}
    wb = openpyxl.load_workbook("censuspopdata.xlsx")
    sheet = wb.active

    for i in range(2, sheet.max_row + 1):
        # defining values
        state = sheet["b" + str(i)].value
        county = sheet["c" + str(i)].value
        pop = sheet["d" + str(i)].value

        # setting up the data
        county_data.setdefault(state, {})
        county_data[state].setdefault(county, {"pop": 0, "tracts": 0})

        county_data[state][county]["pop"] += int(pop)
        county_data[state][county]["tracts"] += 1
    return county_data


def writing_results():
    county_data = census_data()
    with open("census_result.csv", "w", newline='') as excel_file:
        writer = csv.DictWriter(
            excel_file, fieldnames=["State", "County", "Population", "No. of Tracts"]
        )
        writer.writeheader()
        for state in county_data:
            for county in county_data[state]:
                writer.writerow(
                {
                "State": state,
                "County": county,
                "Population": county_data[state][county]["pop"],
                "No. of Tracts": county_data[state][county]["tracts"]
                }
                )


writing_results()
