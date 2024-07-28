# try:
#     open('config.txt')
# except IndexError[2]:
#     print("The file doesn't exist.")
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()