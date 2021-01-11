import warnings
warnings.filterwarnings("ignore") # FIXME The empty slice warnings don't really matter, but this shouldn't be here

def randomcolor(eps=.1):
    """
    Randomly chooses an RGB color, rounding each of R, G and B to the nearest <eps>.
    """
    r = round(random()/eps)*eps
    g = round(random()/eps)*eps
    b = round(random()/eps)*eps
    return (r,g,b)


def color_grid_random(boxes, grid):
    """
    Randomly color a grid, choosing a random color for each box.
    """

    for b in boxes:
        c = randomcolor()
        grid[b.x:b.x+b.w,b.y:b.y+b.h,0] = c[0]
        grid[b.x:b.x+b.w,b.y:b.y+b.h,1] = c[1]
        grid[b.x:b.x+b.w,b.y:b.y+b.h,2] = c[2]
    return grid


def color_grid_from_image(boxes, grid, image):
    """
    Color a grid based on an image.
    For each box, take the mean color inside that box in the image and use that.
    """
    # Process image to 0-1
    image = image / 255
    for b in boxes:
        if len(image[b.x:b.x+b.w,b.y:b.y+b.h,0]) != 0:
            grid[b.x:b.x+b.w,b.y:b.y+b.h,0] = image[b.x:b.x+b.w,b.y:b.y+b.h,0].mean()
            grid[b.x:b.x+b.w,b.y:b.y+b.h,1] = image[b.x:b.x+b.w,b.y:b.y+b.h,1].mean()
            grid[b.x:b.x+b.w,b.y:b.y+b.h,2] = image[b.x:b.x+b.w,b.y:b.y+b.h,2].mean()
    return grid
