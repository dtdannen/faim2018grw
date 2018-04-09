
filename = 'email-names-similarity-search.txt'
new_filename = 'processed-email-names-similarity-search.txt'
with open(filename, 'r', encoding="utf-8") as f:
    with open(new_filename, 'w',encoding="utf-8") as f_new:
        for line in f.readlines():
            line.strip()
            line_parts = line.split()
            name = ''
            for i in range(len(line_parts)-1):
                name += '{} '.format(line_parts[i])
            f_new.write('{} <{}>\n'.format(name,line_parts[-1]))
        f_new.flush()

print("Done!")