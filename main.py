#         _.---._    /\\
#      ./'       "--`\//
#    ./     Ethan    o \
#   /./\  )______   \__ \
#  ./  / /\ \   | \ \  \ \
#     / /  \ \  | |\ \  \7
#      "     "    "  "

from tqdm import tqdm

import typer


app = typer.Typer()

@app.command()
def animate(input: str = typer.Argument(..., help="Input file (png, jpg, etc)"),
            frames: int = typer.Option(300, help="Number of frames in output gif"),
            duration: int = typer.Option(100, help="Duration of each frame in output gif (ms)"),
            splits: int = typer.Option(2000, help="Number of times to split the image"),
            out: str="./output.gif",
            orientation: str = "alternating"
    ):
    """
    From the given image, produce a gif with glitch effects.
    """
    # TODO call a bunch of utils stuff here
    print("Testing")

if __name__ == "__main__":
    app()
