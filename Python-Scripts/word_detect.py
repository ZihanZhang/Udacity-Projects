import urllib


def word_detect():
    file = open("/Users/ZihanZhang/Desktop/quotes.txt")
    contents = file.read()
    print(contents)
    file.close()
    bad_detect(contents)


def bad_detect(checkcontents):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + checkcontents)
    output = connection.read()
    # print(output)
    connection.close()
    if "true" in output:
        print("bad words")
    elif "false" in output:
        print("all ok")
    else:
        print("Error")


word_detect()
