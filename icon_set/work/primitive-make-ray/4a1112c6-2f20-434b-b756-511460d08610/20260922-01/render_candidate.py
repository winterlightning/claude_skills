"""Export this standalone attempt without registering or building it."""
import importlib.util
import json
from pathlib import Path
import cairosvg
from PIL import Image

SOURCE_ICON_ID = "4a1112c6-2f20-434b-b756-511460d08610"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/aerial yoga bow pose_4a1112c6-2f20-434b-b756-511460d08610.svg"
AUTHOR = "gpt-6"

def export():
    folder = Path(__file__).parent
    source = folder / "aerial_yoga_bow_pose_4a1112c6_2f20_434b_b756_511460d08610.py"
    spec = importlib.util.spec_from_file_location("aerial_candidate", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    icon = module.AerialYogaBowPose()
    report = icon.validate_icon()
    (folder / "validation.txt").write_text(report.describe() + "\n")
    svg = icon.to_svg()
    (folder / "aerial-yoga-bow-pose.svg").write_text(svg)
    for theme, background in (("light", "white"), ("dark", "#161616")):
        for size in (48, 480):
            output = folder / f"preview-{theme}-{size}.png"
            cairosvg.svg2png(bytestring=svg.encode(), write_to=str(output), output_width=size, output_height=size, background_color="white")
            if theme == "dark":
                # Theme the raster, leaving the emitted SVG byte-for-byte intact.
                from PIL import ImageOps
                raster = Image.open(output).convert("RGB")
                raster = ImageOps.colorize(ImageOps.grayscale(raster), black="#eeeeee", white=background)
                raster.save(output)
    sheet = Image.new("RGB", (960, 544), "#dddddd")
    for x, theme in ((0, "light"), (480, "dark")):
        sheet.paste(Image.open(folder / f"preview-{theme}-480.png"), (x, 64))
        sheet.paste(Image.open(folder / f"preview-{theme}-48.png"), (x + 216, 8))
    sheet.save(folder / "review-sheet.png")
    print(report.describe())

if __name__ == "__main__":
    export()
