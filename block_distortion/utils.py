# TODO function that takes frames and writes to gif
#1. PIL Image class conversion
#2. Write to GIF

from rich.progress import track
from rich.console import Console
from PIL import Image
import numpy as np

# Was possible to use imageio for this, but I found PIL to be 5-10x as fast, so used that.
def write_frames_to_gif(fname: str, frames, duration: int, progress=False):
    """
    Writes frames to GIF file.

    fname: Filename for output
    frames: List of (W,H,CHANNELS) np arrays
    duration: Duration of each frame in the gif
    """

    # Convert to PIL
    pil_images = []
    if progress:
        frames = track(frames, "Converting Frames")
    for f in frames:
        pim = Image.fromarray((f*255).astype(np.uint8))
        pim.info['transparency'] = 255
        pil_images.append(pim)

    # Write GIF, show status spinner with rich
    if progress:
        console = Console()
        with console.status(f"Writing GIF to {fname}") as status:
            # loop=0 means the gif just repeats forever, which is what I think everyone probably expects
            pil_images[0].save(fname, save_all=True, append_images=pil_images[1:], loop=0, duration=duration)
    else:
            pil_images[0].save(fname, save_all=True, append_images=pil_images[1:], loop=0, duration=duration)
