from all_ import *

class Scene(object):
    def __init__(self, name:str, type_, fps:int=60) -> type(None):
        """Create a scene.

        Must make sure there is a scene when you creating a sprite.
        Args:
        name: The name of the scene.

        """
        self.name=name
        self.type_=type_
        self.fps=fps
        pass
    pass

class Sprite(object):
    def __init__(self, name:str, shapes:List[pygame.Surface], scene:Scene,
            isplayer:bool=False, heart:int=-1, maxheart:int=-1) -> type(None):
        """Setup a sprite.

        Args:
        name: The name of the sprite.
        shapes: The shapes of the sprite. Must be a list of Surfaces.
        isplayer: Is the sprite a player.
        heart: The heart of the player. -1 means infinite.
        maxheart: The maximum of the heart of the player.
            -1 means infinite.

        Raises:
        TypeError: Wrong type of arguments.
        ValueError: The argument 'heart' or 'maxheart'
            was negative except for -1, or 'heart' is greater than 'maxheart'.
        """
        if not isinstance(name, str):
            raise TypeError("Argument 'name' must be a string,"
                "not %s." % type(name).__name__ )
            pass
        if not isinstance(shapes, list):
            raise TypeError("Argument 'shapes' must be a list of Surfaces,"
                "not %s." % type(name).__name__ )
            pass
        elif not all([isinstance(i, pygame.Surface) for i in shapes]):
            raise TypeError("There is a wrong type in list 'shapes',"
                    "must be all Surfaces.")
            pass
        if not isinstance(isplayer, bool):
            raise TypeError("Argument 'isplayer' must be a boolean,"
                "not %s." % type(name).__name__ )
            pass
        if not isinstance(heart, int):
            raise TypeError("Argument 'heart' must be a integer,"
                "not %s." % type(name).__name__ )
            pass
        if not isinstance(maxheart, int):
            raise TypeError("Argument 'maxheart' must be a interger,"
                "not %s." % type(name).__name__ )
            pass

        if heart<-1:
            raise ValueError("Argument 'heart' is a negative except for -1.")
        if maxheart<-1:
            raise ValueError("Argument 'maxheart' is a negative except for -1.")
        if heart>maxheart or (maxheart != -1 and heart==-1):
            raise ValueError("'heart' was greater than 'maxheart'.")
        self.name=name
        self.isplayer=isplayer
        self.heart=heart
        pass
    def heartchange(self, modifys:int=0, isattack:bool=True) -> type(None):
        """Change the sprite's heart.

        Args:
        modifys: What it changes.
        isattack: Is it an attack. (If it is, then it reverse.)
        """
        if isattack:
            modifys=-modifys
            pass
        self.heart+=modifys
        pass
