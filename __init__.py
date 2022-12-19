from all_ import *

class Sprite(object):
    pass

class Scene(object):
    def __init__(self, name:str, bg:pygame.Surface,
            type_:enums.SceneType) -> type(None):
        """Create a scene.

        Must make sure there is a scene when you creating a sprite.
        Args:
        name: The name of the scene.
        bg: The background of the scene.
        type_: The type of the scene.
        fps: The FPS of the scene.

        """
        self.name=name
        self.bg=bg
        self.width=bg.get_width()
        self.height=bg.get_height()
        self.type_=type_
        self.sprites:List[Union[type(None), Sprite]]=[]
        self.removed=[]
        pass
    def add_sprite(self, sprite:Sprite):
        """Add a sprite.
        
        Args:
        sprite: Which sprite will be add.

        Returns:
        A integer for the new sprite's position.
        """
        if not isinstance(sprite, Sprite):
            raise TypeError("Argument 'sprite' must be a Sprite, "
                "not %s." % type(sprite).__name__)
            pass
        if self.removed:
            pos=self.removed.pop()
            self.sprite[pos]=sprite
            return pos
        self.sprites.append(sprite)
        return len(self.sprites)-1
    def update(self):
        """Update scene and get its surface.

        Returns:
        The surface (pygame.Surface).
        """
        surface=self.bg.copy()
        surface.lock()
        for sprite in self.sprites:
            if sprite is None:
                pass # Ignore removed sprite.
            surface.blit(sprite.update(), (sprite.x, sprite.y))
            pass
        surface.unlock()
        return surface
    def removesprite(self, handle):
        """Remove a sprite.

        Args:
        handle: The handle of the sprite will be removed.
        """
        self.sprites[handle]=None
        self.removed.append(handle)
        pass
    pass

class Sprite(object):
    def __init__(self, name:str, shapes:List[pygame.Surface], scene:Scene,
            isplayer:bool=False, heart:Number=-1, maxheart:Number=-1) -> type(None):
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
        self.shapes=shapes
        self.isplayer=isplayer
        self.heart=heart
        self.handles={}
        self.x=0
        self.y=0
        self.shapeno=0
        pass
    def heartchange(self, modifys:Number=0, isattack:bool=True) -> type(None):
        """Change the sprite's heart.

        Args:
        modifys: What it changes.
        isattack: Is it an attack. (If it is, then it reverse.)
        
        Raises:
        TypeError: Wrong type.
        """
        if not isinstance(isattack, bool):
            raise TypeError("Argument 'isattack' must be a boolean, "
                "not %s" % type(isattack).__name__)
            pass
        if not isinstance(modifys, Number):
            raise TypeError("Argument 'isattack' must be a boolean, "
                "not %s" % type(isattack).__name__)
            pass
        if self.heart==-1:
            return
        if isattack:
            modifys=-modifys
            pass
        self.heart+=modifys
        pass
    def bindhandle(self, handlename:str, bindfunction:Callable) -> type(None):
        """Bind handles to a function.

        If it was binded, then overwrite it.
        Args:
        handlename: The name of handles.
        bindfunctions: The functions when the event start.
        Raises:
        TypeError: Wrong parameter type.
        """
        if not callable(bindfunction):
            raise TypeError("Argument bindfunction' must be a callable, "
                    "not %s." % type(bindfunction).__name__)
            pass
        if not isinstance(handlename, str):
            raise TypeError("Argument 'handlename' must be a string, "
                    "not %s." % type(handlename).__name__)
            pass

        self.handles[handlename]=bindfunction
        pass
    def update(self):
        return self.shapes[self.shapeno]
    pass
