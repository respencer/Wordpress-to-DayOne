import os
import feedparser


def parseData():
    content = feedparser.parse("personal_data.xml")

    output_date_file = open("dateTime.txt", "w")
    file_count = 0
    tag_count = 0

    for item in content.entries:
        file_count += 1
        output_text_file = open("files/" + str(file_count) + ".txt", "w")
        print(file_count)

        # print(item)

        title = item.title
        print(title)

        text = item.content[0]["value"]
        # print(text)

        dateTime = item.wp_post_date_gmt
        # print(dateTime + "\n")

        tags = []
        try:
            for tag in item.tags:
                if tag["scheme"] == "post_tag":
                    tags.append(tag["term"])
                    tag_count += 1
            # print(tags)

            tags_string = " ".join(["#" + i for i in tags])
            # print(tags_string)
        except AttributeError:
            pass

        output_text_file_content = title + "\n\n" + text + "\n\n" + tags_string
        # print(output_text_file_content)

        output_date_file.write(dateTime + "\n")
        output_text_file.write(output_text_file_content)
        output_text_file.close()

        print("\n..................\n")

    output_date_file.close()
    print(file_count)
    print(tag_count)


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
