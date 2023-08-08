class Base:
    """
    The base class for managing id attributes.

    Attributes:
        __nb_objects (int): The total count of created objects.
        id (int): The unique ID of the object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): The ID for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
