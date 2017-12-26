import os
import sys


def main(input_file, output_folder):
    write_buf = []
    with open(input_file, 'r', encoding='utf-8') as reader:
        for src_line in reader:
            src_line = src_line.strip()
            src_sents = src_line.split("##SENT##")
            string_buf = ""
            string_buf += 'null\n\n'
            for sent in src_sents:
                string_buf += '{0}\t\t\t0\n'.format(sent)
            string_buf += '\n'
            string_buf += 'null\n\nnull\n'
            write_buf.append(string_buf)
    for idx, item in enumerate(write_buf):
        of_name = '{0:06d}.summary'.format(idx)
        of_name = os.path.join(output_folder, of_name)
        with open(of_name, 'w', encoding='utf-8') as writer:
            writer.write(item)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
