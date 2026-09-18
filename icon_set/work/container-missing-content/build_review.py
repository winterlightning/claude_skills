"""Build the current complete review instead of the superseded partial gallery."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name("build_final_gallery.py")), run_name="__main__")
