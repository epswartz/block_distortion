#         _.---._    /\\
#      ./'       "--`\//
#    ./     Ethan    o \
#   /./\  )______   \__ \
#  ./  / /\ \   | \ \  \ \
#     / /  \ \  | |\ \  \7
#      "     "    "  "

from rich.progress import track
from rich.console import Console

import typer

from skimage.io import imread, imsave
from glitch_utils.splitting import *
from glitch_utils.io import *
from glitch_utils.Box import Box
from glitch_utils.coloring import *

ORIENTATION = "alternating" # I may add this to the cli but for now all the other options look like trash, so

app = typer.Typer()

@app.command()
def animate(
    image_path: str = typer.Argument(..., help="Input file (png, jpg, etc)"),
    frames: int = typer.Option(30, "--frames", "-f", help="Number of frames in output gif"),
    duration: int = typer.Option(100, "--duration", "-d", help="Duration of each frame in output gif (ms)"),
    splits: int = typer.Option(2000, "--splits", "-s", help="Number of times to split the image"),
    out: str = typer.Option("./output.gif", "--out", "-o", help="Name of output file (gif)")
):
    """
    Produce a gif with glitch effects.
    """

    im = imread(image_path)

    X_SIZE, Y_SIZE, CHANNELS = im.shape
    init_box = Box(0, 0, X_SIZE, Y_SIZE)

    images = []
    for i in track(range(frames), "Rendering Frames"):
        grid = np.zeros((X_SIZE, Y_SIZE, CHANNELS))
        boxes = always_largest_split(grid, init_box, n=splits, orient=ORIENTATION)
        grid = color_grid_from_image(boxes, grid, im)
        images.append(grid)

    write_frames_to_gif(out, images, duration)

@app.command()
def single(
    image_path: str = typer.Argument(..., help="Input file (png, jpg, etc)"),
    splits: int = typer.Option(2000, "--splits", "-s", help="Number of times to split the image"),
    out: str = typer.Option("./output.gif", "--out", "-o", help="Name of output file (gif)")
):
    """
    Produce a single image with glitch effects.
    """
    im = imread(image_path)

    X_SIZE, Y_SIZE, CHANNELS = im.shape
    init_box = Box(0, 0, X_SIZE, Y_SIZE)

    console = Console()
    with console.status("Processing image") as status:
        grid = np.zeros((X_SIZE, Y_SIZE, CHANNELS))
        boxes = always_largest_split(grid, init_box, n=splits, orient=ORIENTATION)
        grid = color_grid_from_image(boxes, grid, im)

    with console.status(f"Writing output to {out}"):
        imsave(out, grid)

if __name__ == "__main__":
    app()
