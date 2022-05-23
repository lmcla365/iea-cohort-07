# Instructor solution
NUM_LISTS = 2
MENU_PROMPT = (
"""Which operation would you like to perform?
(A)dd, (R)emove, Re(V)erse, (D)isplay, or (Q)uit:""")
WHICH_LIST_PROMPT = f"Which list (1-{NUM_LISTS})?"

word_lists = []
for i in range(NUM_LISTS):
    word_lists.append([])
#word_lists = [[]] * NUM_LISTS
#print([id(w) for w in word_lists])

while True:
    op = input(MENU_PROMPT).strip().upper()
    if op in "ARV":
        which = int(input(WHICH_LIST_PROMPT)) - 1
        current_list = word_lists[which]
    # Add
    if op == "A":
        val = input("Enter a value to add:")
        current_list.append(val)
    # Remove
    if op == "R":
        by = input("By (I)ndex or by (V)alue?")
        if by == "I":
            i = int(input("Enter index to remove:"))
            current_list.pop(i)
        else:
            v = input("Enter a value to remove:")
            current_list.remove(v)
    # Reverse
    if op == "V":
        current_list.reverse()

    # Display
    if op == "D":
        for word_list in word_lists:
            print(word_list)

    # Quit
    if op == "Q":
        break
