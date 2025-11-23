shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    def add_item(item):
        shopping_list.append(item)
        return f'Item "{item}" added to the shopping list.'
    def remove_item(item):
        try:
            shopping_list.remove(item)
            return f'Item "{item}" removed from the shopping list.'
        except ValueError:
            return f'Item "{item}" not found in the shopping list.'
    def view_list():
        if not shopping_list:
            return "The shopping list is empty."
        return "Shopping List:\n" + "\n".join(f"- {item}" for item in shopping_list)

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice ==  "1":
            item = input("Enter the item to add: ")
            print(add_item(item))
        elif choice == "2":
            item = input("Enter the item to remove: ")
            print(remove_item(item))
        elif choice == "3":
            print(view_list())
        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else :
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()