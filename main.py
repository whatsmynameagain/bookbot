
def count_words(input):
    split = input.split()
    return len(split)


def count_characters(input):
    counts = {}
    for char in input:
        lowercase = char.lower()
        if lowercase.isalpha():
            if lowercase in counts:
                counts[lowercase] += 1
            else:
                counts[lowercase] = 1
    return counts


def convert_dict_to_listdict(dict):
    dictlist = []
    for key, value in dict.items():
        tempdict = { 
            "name" : f"{key}",
            "count" :  value,
        }
        dictlist.append(tempdict)
    return dictlist


def _sort(_list):

    def sort_count(dict):
        return dict["count"]
    
    _list.sort(reverse=True, key=sort_count)
    
    return _list


def report(_listdict, _filename, _file_contents):
    print(f"---Report of '{_filename}'---\n")
    print(f"{count_words(_file_contents)} words total in the file")
    print("")
    for x in _listdict:
        print(f"Character '{x["name"]}' was found {x["count"]} times")


def main():
    file_contents = None
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        file_contents = f.read()
    characters_dict = count_characters(file_contents)
    listdict = convert_dict_to_listdict(characters_dict)
    report(_sort(listdict), filename, file_contents)


if __name__ == '__main__':
    main()



