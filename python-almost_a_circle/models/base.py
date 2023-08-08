class Base:
    """
    The base class that manages the id attribute for all future classes.

    Attributes:
        __nb_objects (int): A private class attribute that stores the count of created objects.
        id (int): A public instance attribute representing the unique ID of the object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): The ID for the instance. If None, an ID is generated automatically.

        Attributes:
            id (int): The unique ID assigned to the instance.
        """
        if id is not None:
            # If id is provided, use it as the instance's id
            self.id = id
        else:
            # If id is not provided, generate a new id and increment __nb_objects
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
