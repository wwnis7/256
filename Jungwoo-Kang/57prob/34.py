# There are 5 employees:
# John Smith
# Jackie Jackson
# Chris Jones
# Amanda Cullen
# Jeremy Goodwin
# Enter an employee name to remove: Chris Jones
# There are 4 employees:
# John Smith
# Jackie Jackson
# Amanda Cullen
# Jeremy Goodwin

List=['John Smith','Jackie Jackson','Chris Jones','Amanda Cullen','Jeremy Goodwin']
print(f'There are {len(List)} employees:')
for i in List:
    print(i)

remove=input('Enter an employee name to remove: ')
List.remove(remove)
print(f'There are {len(List)} employees:')
for i in List:
    print(i)