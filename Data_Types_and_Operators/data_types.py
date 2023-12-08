# String : immutable ordered series of characters
name = "Utkarsh"
middle_name = "Raj"
last_name = "Singh"

full_name = name + " " + middle_name + " " + last_name
print(full_name)

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

# TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
print(
    str(
        int(mon_sales)
        + int(tues_sales)
        + int(wed_sales)
        + int(thurs_sales)
        + int(fri_sales)
    )
)
