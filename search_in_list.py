def known_persons(raw_known_person=[]):
    return raw_known_person.split(",")

def search_person(search_person_input, known_persons_list):
    if search_person_input in known_persons_list:
        print("You know {}".format(search_person_input))
    else:
        print("You don't know {}".format(search_person_input))

def main():
    raw_known_person = input("Enter the list of known persons (separate by comma):")
    known_persons_list = known_persons(raw_known_person)
    search_person_input = input("Enter the name of person to be searched:")
    search_person(search_person_input, known_persons_list)

if __name__ == '__main__':
    main()
