range_start = int(input())
range_end = int(input())

range_start_as_srt = str(range_start)
range_end_as_str = str(range_end)

for barcode in range(range_start, range_end + 1):
    is_valid_barcode = True
    barcode_as_srt = str(barcode)
    for index, digit in enumerate(barcode_as_srt):
        if int(digit) % 2 == 0:
            is_valid_barcode = False
            break
        if int(digit) < int(range_start_as_srt[index]):
            is_valid_barcode = False
            break
        if int(digit) > int(range_end_as_str[index]):
            is_valid_barcode = False
            break
    if is_valid_barcode:
        print(barcode, end=" ")