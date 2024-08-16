import re, openpyxl

wb = openpyxl.load_workbook('docs/str.xlsx')
ws = wb.active

strs = []
for row in ws.iter_rows():
    row_key = []
    for cell in row:
        row_key.append(cell.value)
    strs.append(row_key)
    print(row_key)

with open("lang/english.lng", 'w', encoding='utf-8') as f:
    f.write("##grflangid 0x01"+"\n")
    for i in range(len(strs)):
        if strs[i][1] == None:
            f.write(strs[i][0]+"\n")
        else:
            f.write(f"{strs[i][0]:48} {":"+strs[i][1]:<10}\n")

def other_lang_generate(lang_name, lang_row, lang_code):
    with open("lang/"+lang_name+".lng", 'w', encoding='utf-8') as f:
        f.write("##grflangid "+lang_code+"\n")
        for i in range(len(strs)):
            if strs[i][lang_row] == None:
                if strs[i][1] == None:
                    f.write(strs[i][0]+"\n")
                else:
                    pass
            else:
                f.write(f"{strs[i][0]:48} {":"+strs[i][2]:<10}\n")
   
other_lang_generate("simplified_chinese", 2, "0x56")
   