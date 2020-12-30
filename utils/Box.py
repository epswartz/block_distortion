class Box:

    def __init__(self, x, y, w, h, split_orient=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        if (x + w > X_SIZE) or (y + h > Y_SIZE):
            raise ValueError

        # For "alternating" option on we track which orient was used to create box.
        self.split_orient = split_orient

    def __str__(self):
        return f"({self.x},{self.y},{self.w},{self.h})"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        """
        Because I want to use this with heapq to get the BIGGEST box, this is actually returning
        whether the current box is BIGGER than the other one.
        """
        return self.area() > other.area()

    def area(self):
        return self.w*self.h

    def rand_split(self, orient="random"):
        """
        Splits the box, returning two new boxes in a tuple.
        """
        if orient == "random":
            orientation = randint(0,1)
        elif orient == "alternating":
            orientation = int(not self.split_orient)
        elif orient == "horizontal":
            orientation = 1
        elif orient == "vertical":
            orientation = 0
        else:
            raise ValueError("orient must be 'random', 'horizontal', 'vertical', or 'alternating'.")

        if orientation == 0: # Vertical cut
            cut = round(random()*self.h)
            box1 = Box(self.x, self.y, self.w, cut, split_orient=orientation)
            box2 = Box(self.x, self.y+cut, self.w, self.h-cut, split_orient=orientation)
        else: # Horizontal cut
            cut = round(random()*self.w)
            box1 = Box(self.x, self.y, cut, self.h, split_orient=orientation)
            box2 = Box(self.x+cut, self.y, self.w-cut, self.h, split_orient=orientation)

        return (box1, box2)

