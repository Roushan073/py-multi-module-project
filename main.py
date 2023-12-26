from reader import file_reader
from writer import file_writer

if __name__ == '__main__':
    fr = file_reader.FileReader("./data/test.txt")
    fw = file_writer.FileWriter("output.txt", "a")

    fr.read()
    fw.write("data")
