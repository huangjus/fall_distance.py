def fall_distance(seconds):
    """
        Calculates the distance fallen due to gravity in a specific time period.

        seconds:The time in seconds that the object has been falling.

        Returns:
        d: The distance in meters that the object has fallen in the given time.
    """

    d = (1/2) * 9.8 * seconds ** 2
    return d
