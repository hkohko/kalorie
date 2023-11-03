import csv
import json
from collections.abc import Iterator

from kalorie.constants import DATADUMP_DIR


def analyze_lines(row: list[str]) -> Iterator[list[str]]:
    marker = []
    index_of_falsy: list[int] = []
    for item in row:
        if bool(item) is False:  # discard empty column ''
            continue
        try:
            int(item)
            marker.append(True)
        except ValueError:
            marker.append(False)

    for idx, boolean in enumerate(marker):
        if boolean is False:
            index_of_falsy.append(idx)

    for idx, _ in enumerate(index_of_falsy):  # yield new lists
        try:
            yield row[index_of_falsy[idx] : index_of_falsy[idx + 1]]
        except IndexError:
            yield row[index_of_falsy[idx] : len(row)]


def remove_empty_strings(new_list: list[str]):
    for idx, item in enumerate(new_list):
        if bool(item) is False:
            new_list.pop(idx)
    return new_list


def remove_leftover_decimal(discarded_emptry_string: list[str]):
    first_item = discarded_emptry_string[0]
    try:
        int(first_item)
        discarded_emptry_string.pop(0)
    except ValueError:
        pass
    finally:
        return discarded_emptry_string


def remove_table_title(discarded_leftver_decimal: list[str]):
    banned_words = ("tabel", "kalori", "golongan")
    for idx, item in enumerate(discarded_leftver_decimal):
        for word in banned_words:
            if word in item.lower():
                discarded_leftver_decimal.pop(idx)
                return discarded_leftver_decimal
    return discarded_leftver_decimal


def get_first_three(discarded_table_title: list[str]):
    return discarded_table_title[:3]


def to_dict(first_three: list[str]):
    if len(first_three) == 3:
        try:
            return {
                "nama": first_three[0],
                "berat": int(first_three[1]),
                "kalori": int(first_three[2]),
            }, True
        except ValueError:
            print(first_three)
            return "lost", False
    else:
        return "lost", False


def remove_literal_unit(discarded_table_title: list[str]):
    if discarded_table_title[0].lower() == "unit":
        discarded_table_title.pop(0)
        return discarded_table_title
    else:
        return discarded_table_title


def simplify_rows():
    list_of_simplified_rows = []
    with open(DATADUMP_DIR.joinpath("data_source1_clean.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for simplified_rows in analyze_lines(row):
                if len(simplified_rows) < 3:
                    continue
                list_of_simplified_rows.append(simplified_rows)
    return list_of_simplified_rows


def sanitize():
    compile_result = []
    lost_data = []

    list_of_simplified_rows = simplify_rows()

    for rows in list_of_simplified_rows:
        discarded_empty_string = remove_empty_strings(rows)
        discarded_leftover_decimal = remove_leftover_decimal(discarded_empty_string)
        discarded_table_title = remove_table_title(discarded_leftover_decimal)
        discarded_literal_unit = remove_literal_unit(discarded_table_title)
        first_three = get_first_three(discarded_literal_unit)
        converted_to_dict = to_dict(first_three)
        data, check = converted_to_dict
        if check:
            compile_result.append(data)
        else:
            lost_data.append(data)
    print("Cleaned data: ", len(compile_result))
    print("Data lost: ", len(lost_data))
    return compile_result


def save_data():
    to_save = sanitize()
    with open(DATADUMP_DIR.joinpath("final_data.json"), "w") as file:
        json.dump(to_save, file)


if __name__ == "__main__":
    save_data()
