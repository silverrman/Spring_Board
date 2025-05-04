def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    # This function manipulates a list by adding or removing elements from the beginning or end
    
    # Check if both command and location have valid values
    if command not in ["add", "remove"] or location not in ["beginning", "end"]:
        # Return None for invalid commands or locations
        return None
    
    # Handle the "remove" command
    if command == "remove":
        if location == "beginning":
            # Remove and return the first element (index 0) using pop
            return lst.pop(0)
        else:  # location == "end"
            # Remove and return the last element using pop
            # When pop() is called without an index, it removes the last element
            return lst.pop()
    
    # Handle the "add" command
    elif command == "add":
        if location == "beginning":
            # Insert the value at the beginning (index 0)
            lst.insert(0, value)
            # Return the modified list
            return lst
        else:  # location == "end"
            # Append the value to the end of the list
            lst.append(value)
            # Return the modified list
            return lst
            
    # Time complexity: O(n) for adding/removing at beginning (requires shifting elements)
    #                  O(1) for adding/removing at end
    # Space complexity: O(1) - operations are performed in-place
