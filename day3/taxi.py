string = '7 TAX 9215'
tax_list = ['TAX', 'TBX', 'TEX']
tax_other = ['TAX', 'TBX']
list_number = string.split()

if len(string) == 10:
    if int(list_number[0]) >= 1 and int(list_number[0]) <= 7:
        print('correct')
    elif int(list_number[0]) == 7 and list_number[1] in tax_other:
        if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
            print('correct')