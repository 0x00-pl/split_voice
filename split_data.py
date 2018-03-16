import decode_inf
import os

def main(base_path):
    inf_path = os.path.join(base_path, 'inf.d')
    voice_path = os.path.join(base_path, 'voice.d')
    output_base = os.path.join(base_path, 'output')
    os.makedirs(output_base, exist_ok=True)

    info = decode_inf.get_data(open(inf_path))
    data = open(voice_path, 'rb').read()

    for [name, start, length] in info:
        print(name, start, length)
        v = data[start: start+length]
        v_path = os.path.join(output_base, name)
        with open(v_path, 'wb') as f:
            f.write(v)


if __name__ == '__main__':
    main('.')
