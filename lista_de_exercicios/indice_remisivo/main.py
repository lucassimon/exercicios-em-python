from index import Index

if __name__ == '__main__':

    keywords = input(
        "Enter the keywords (comma separeted: programming, be, to, hero: "
    )

    if not keywords:
        exit()

    index = Index(keywords)

    filename = input(
        "\nPut the file in this root directory and enter the file name: "
    )

    if not filename:
        exit()

    count = 1

    keywords = index.get_keywords()
    keywords.sort()

    with open(filename) as f:
        # Utilize um método eficiente para verificar se uma
        # palavra lida do texto pertence ao índice.
        # TODO: Improve 2 loops

        for line in f:
            words = line.split()
            for i in keywords:
                if index.verify(i, words):
                    index.add(i, count)

            count += 1

    word = input(
        "\nSet a word to search in this index: "
    )

    print('------------------------\n')
    index.search(word)

    print('------------------------\n')
    index.show()
    print('------------------------\n')
