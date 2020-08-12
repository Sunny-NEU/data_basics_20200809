import json
def convert_file_format(input_file_path: str, output_file_path: str,
                        input_format: str = 'csv', output_format: str = 'json'):
    with open(input_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    print()
    for i in range(1, len(lines)):
        line=[int(j) if j.isdigit() else j for j in lines[i].split(',')]
        lines[i] = dict(zip(lines[0].split(','), line))

    f1 = open(output_file_path, 'w', encoding='utf-8')
    json.dump(lines[1:], f1, ensure_ascii=False, indent=4)
    f1.close()
# convert_file_format('./student.csv','./student.json','csv','json')


