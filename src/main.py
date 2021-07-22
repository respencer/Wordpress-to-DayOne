import os


def parseData():
    input_file = open("personal_data.xml", "r")
    content = input_file.read()

    output_date_file = open("dateTime.txt", "w")
    file_count = 0
    tag_count = 0

    while True:
        if "<item>" in content:
            file_count += 1
            output_text_file = open("files/" + str(file_count) + ".txt", "w")
            print(file_count)

            # print(len(content))
            file_content = content[content.index("<item>") : content.index("</item>")]
            # print(file_content)

            try:
                title = file_content[
                    file_content.index("<title>") + 7 : file_content.index("</title>")
                ]
            except ValueError:
                title = ""
            print(title)

            try:
                file_content = file_content[file_content.index("</title>") :]
            except ValueError:
                file_content = file_content[file_content.index("<title/>") :]
            text = file_content[
                file_content.index("<content:encoded>")
                + 26 : file_content.index("</content:encoded>")
                - 3
            ]
            # print(text)

            file_content = file_content[file_content.index("</content:encoded>") :]
            dateTime = file_content[
                file_content.index("<wp:post_date_gmt>")
                + 18 : file_content.index("</wp:post_date_gmt>")
            ]
            # print(dateTime + "\n")

            file_content = file_content[file_content.index("</wp:post_date_gmt>") :]

            tags = []
            while '<category domain="post_tag"' in file_content:
                file_content = file_content[
                    file_content.index('<category domain="post_tag"') :
                ]
                tags.append(
                    file_content[
                        file_content.index("<![CDATA")
                        + 9 : file_content.index("</category>")
                        - 3
                    ]
                )
                tag_count += 1

                file_content = file_content[file_content.index("</category>") :]

            # print(tags)

            tags_string = " ".join(["#" + i for i in tags])
            # print(tags_string)

            output_text_file_content = title + "\n\n" + text + "\n\n" + tags_string
            # print(output_text_file_content)

            output_date_file.write(dateTime + "\n")
            output_text_file.write(output_text_file_content)
            output_text_file.close()

            content = content[content.index("</item>") + 5 :]
            print("\n..................\n")
        else:
            output_date_file.close()
            print(file_count)
            print(tag_count)
            break


def makeDayOneEntries():
    file_path = os.getcwd() + "/files/"
    file_names = os.listdir(file_path)

    input_date_file = open("dateTime.txt", "r")

    for file in sorted(file_names):
        dateTime = input_date_file.readline()
        dateTime = dateTime[:-1]
        # print(dateTime)

        # print('dayone2 -d="' + dateTime + '" new < ' + file_path + file)
        os.system('dayone2 -d="' + dateTime + '" new < ' + file_path + file)


if __name__ == "__main__":
    parseData()
    makeDayOneEntries()
