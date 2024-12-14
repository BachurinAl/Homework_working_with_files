import glob


def line_counting_files():
    d = {}
    for file in glob.glob('*txt'):
        with open(file, 'r', encoding='utf-8') as f:
            string = len(f.readlines())
            f.seek(0)
            d[file] = [string, f.read().strip()]

    with open('result.txt', 'w', encoding='utf-8') as f:
        d = sorted(d.items(), key=lambda x: x[1])
        for i in d:
            f.write(i[0] + '\n')
            for j in i[1]:
                f.write(str(j) + '\n')


line_counting_files()