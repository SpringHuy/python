import sys

def rlines():
    f = open(sys.argv[1], mode='rt', encoding='utf8')
    for line in f: 
        sys.stdout.write(line)
    f.close()


def afile():
    fi = open("file.txt", "wt")
    fi.write("tuoi hong tho ngay, duoi mai truong. Au tho da di qua roi, de lai trong toi mot noi buon. Noi len tieng yeu lang tham anh danh cho em.\n\n")
    fi.close()

    fi = open("file.txt", "rt", encoding="utf8")
    print(fi.read())
    fi.close()

    fi = open("file.txt", "at")
    fi.writelines(
        ["tuoi hong tho ngay, duoi mai truong.\n",
        "Au tho da di qua roi, de lai trong toi mot noi buon.\n",
        "Noi len tieng yeu lang tham anh danh cho em.\n"]
        )
    fi.close()

    fi = open("file.txt", "rt", encoding="utf8")
    print(fi.readlines())
    fi.close()


def main():
    rlines()
    #afile()

if __name__ == '__main__':
    main()
