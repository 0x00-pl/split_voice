import base64
import json

def get_data(lines):
    out = []
    for line64 in lines:
        line = base64.b64decode(line64)
        line_sep = line.split()
        if len(line_sep) > 3:
            [name, start, length, *ohers] = line_sep
            if int(length) > 0:
                out.append([name.decode('utf8'), int(start), int(length)])
            else:
                print('[waring]: bad index: ', line)
        else:
            print('[waring]: bad line: ', line, line64.strip())
    return out



if __name__ == '__main__':
    data = get_data(open('inf.d'))
    dataj = json.dumps(data)
    print(dataj)
