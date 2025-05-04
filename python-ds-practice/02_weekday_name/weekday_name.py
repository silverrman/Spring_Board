def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # Create a list of weekday names with index 0 set to None
    # This makes the list 1-indexed, so day_of_week directly matches the index
    # Note: In this implementation, Sunday is day 1 (not Monday as in some systems)
    days = [None, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Check if the day_of_week is within the valid range (1-7)
    if 1 <= day_of_week <= 7:
        # Return the corresponding day name using list indexing
        return days[day_of_week]
    else:
        # Return None for invalid day numbers
        return None
    
    # Time complexity: O(1) - constant time lookup in a list
    # Space complexity: O(1) - fixed size list regardless of input