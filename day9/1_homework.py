class Table:

    def __init__(self, eat, drink, put):
        self._eat = eat
        self._drink = drink
        self._put = put

    @property
    def eat(self):
        return self._eat

    @property
    def drink(self):
        return self._drink

    @property
    def put(self):
        return self._put

    @eat.getter
    def eat(self, eat):
        self._eat = eat

    @drink.getter
    def drink(self, drink):
        self._drink = drink

    @drink.getter
    def put(self, put):
        self._put = put

    def now_on_the_table(self):
        return f"Now {self._eat}, {self._drink} and {self._put} on the table"

    def move(self):
        return 'Move me!'

class Chair:

    def __init__(self, height, color, weight):
        self._height = height
        self._color = color
        self._weight = weight

    @property
    def height(self):
        return self._height

    @property
    def color(self):
        return self._color

    @property
    def weight(self):
        return self._weight

    @height.getter
    def height(self, height):
        self._height = height

    @height.getter
    def color(self, color):
        self._color = color

    @height.getter
    def weight(self, weight):
        self._weight = weight

    def big_chair(self):
        return f"This chair have {self._height}cm height, {self._weight}kg weight and {self._color} color"

    def stand_on(self):
        return f"Please, stand on this {self._color} chair"


class Mirror:

    def __init__(self, color, made_in, size):
        self._color = color
        self._made_in = made_in
        self._size = size

    @property
    def color(self):
        return self._color

    @property
    def made_in(self):
        return self._made_in

    @property
    def size(self):
        return self._size

    @color.getter
    def color(self, color):
        self._color = color

    @made_in.getter
    def made_in(self, made_in):
        self._made_in = made_in

    @size.getter
    def size(self, size):
        self._size = size

    def about_mirror(self):
        return f"This {self._color} mirror with size {self._size} was made in {self._made_in}"

    def motivation(self):
        return 'You looks so pretty'

class Floor:
    def __init__(self, material, area, form):
        self._material = material
        self._area = area
        self._form = form

    @property
    def material(self):
        return self._material

    @property
    def area(self):
        return self._area

    @property
    def form(self):
        return self._form

    @material.getter
    def material(self, material):
        self._material = material

    @area.getter
    def area(self, area):
        self._area = area

    @form.getter
    def form(self, form):
        self._form = form

    def this_floor(self):
        return f"This floor is made from {self._material}, and have {self._area}sq.m area with {self._form} form"

    def lie_down(self):
        return f"You can lie down on this {self._material} floor"

class Wall:
    def __init__(self, material, wallpaper, doorway):
        self._material = material
        self._wallpaper = wallpaper
        self._doorway = doorway

    @property
    def material(self):
        return self._material

    @property
    def wallpaper(self):
        return self._wallpaper

    @property
    def doorway(self):
        return self._doorway

    @material.getter
    def material(self, material):
        self._material = material

    @wallpaper.getter
    def wallpaper(self, wallpaper):
        self._wallpaper = wallpaper

    @doorway.getter
    def doorway(self, doorway):
        self._doorway = doorway

    def this_wall(self):
        return f"This room have {self._material} walls, {self._wallpaper} wallpaper and {self._doorway} doorway"

    def good_wallpaper(self):
        return f"This {self._material} walls looks great!"



table = Table("Potato", "Soda", "Phone")
print(table.now_on_the_table())

chair = Chair(105, 'white', 5)
print(chair.big_chair())

mirror = Mirror('white', 'Germany', '100x50')
print(mirror.about_mirror())

floor = Floor('wood', '10', "rectangular")
print(floor.this_floor())

wall = Wall('concrete', 'red', 'two')
print(wall.this_wall())
