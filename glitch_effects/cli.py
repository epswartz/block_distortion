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
from effects import *
from utils import write_frames_to_gif

app = typer.Typer()


@app.command()
def animate(
    image_path: str = typer.Argument(..., help="Input file (png, jpg, etc)"),
    frames: int = typer.Option(30, "--frames", "-f", help="Number of frames in output gif"),
    duration: int = typer.Option(100, "--duration", "-d", help="Duration of each frame in output gif (ms)"),
    splits: int = typer.Option(2000, "--splits", "-s", help="Number of times to split the image (higher makes a 'smoother' looking image)"),
    out: str = typer.Option("./output.gif", "--out", "-o", help="Name of output file (gif)")
):
    """
    Produce a gif with glitch effects.
    """

    im = imread(image_path)
    print(splits)
    images = animate_image(im, frames, splits, progress=True)
    write_frames_to_gif(out, images, duration, progress=True)


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

    glitched = glitch_image(im, splits)
    with console.status(f"Writing output to {out}"):
        imsave(out, grid)

if __name__ == "__main__":
    app()
