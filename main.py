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
def animate(input: str, frames: int = 300, duration: int = 100,  splits: int = 2000, out: str="./output.gif", orientation: str = "alternating"):
    """
    From the given image, produce a gif with glitch effects.
    """
    # TODO call a bunch of utils stuff here
