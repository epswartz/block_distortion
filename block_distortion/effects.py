import numpy as np

from .splitting import *
from .utils import *
from .Box import Box
from .coloring import *

from rich.progress import track
from rich.console import Console

ORIENTATION = "alternating" # I may add this to the options but for now all the other options look like trash, so

# TODO I can just call distort_image in here.
def animate_image(
    image: np.ndarray,
    frames: int=100,
    splits: int=2000,
    progress: bool=False
):
    """
    Produce a gif with distortion effects. This function returns a list of frames, which you can write with write_frames_to_gif().

    Args:
        image: (W,H,3) or (W,H,4) np.ndarray
        frames: Number of frames in output gif
        splits: Number of times to split the image (higher makes a "smoother" looking image)
        progress: If True, prints a progress bar on stdout.

    Returns:
        list: List of (W,H,3) or (W,H,4) np.ndarrays representing frames of the gif.
    """

    X_SIZE, Y_SIZE, CHANNELS = image.shape
    init_box = Box(0, 0, X_SIZE, Y_SIZE)

    images = []
    r = range(frames)
    if progress:
        r = track(r, "Rendering Frames")
    for i in r:
        grid = np.zeros((X_SIZE, Y_SIZE, CHANNELS))
        boxes = always_largest_split(grid, init_box, n=splits, orient=ORIENTATION)
        grid = color_grid_from_image(boxes, grid, image)
        images.append(grid)

    return images


def distort_image(
    image: np.ndarray,
    splits: int=2000,
    progress: bool=False
):
    """
    Produce a single image with distortion effects. This function returns an np.ndarray which you can write to file with skimage.io.imsave().

    Args:
        image: (W,H,3) or (W,H,4) np.ndarray
        splits: Number of times to split the image (higher makes a "smoother" looking image)
        progress: If True, prints a progress bar on stdout.

    Returns:
        np.ndarray: (W,H,3) or (W,H,4) np.ndarray representing the distorted image.
    """
    X_SIZE, Y_SIZE, CHANNELS = image.shape
    init_box = Box(0, 0, X_SIZE, Y_SIZE)

    if progress:
        console = Console()
        with console.status("Processing image") as status:
            grid = np.zeros((X_SIZE, Y_SIZE, CHANNELS))
            boxes = always_largest_split(grid, init_box, n=splits, orient=ORIENTATION)
            grid = color_grid_from_image(boxes, grid, image)
    else:
        grid = np.zeros((X_SIZE, Y_SIZE, CHANNELS))
        boxes = always_largest_split(grid, init_box, n=splits, orient=ORIENTATION)
        grid = color_grid_from_image(boxes, grid, image)

    return grid
