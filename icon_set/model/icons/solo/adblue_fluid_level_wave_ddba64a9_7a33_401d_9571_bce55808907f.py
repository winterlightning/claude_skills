"""Fluid-level wave component of the text-led AdBlue indicator reference.

CIRCLE is a radial envelope: endpoints (4,24)/(44,24) reach radius20;
the shallow wave stays within that envelope without increasing its height.
One contour owns four equal alternating cubic lobes, defined by a 10-unit
step and common control offsets. Tangents match across every shared knot.
The supplied reference contributes the single wave beneath AD / BLUE.
Lucide wind contributes smooth curve flow in a single pen-down run; no
local Lucide wave reference was found. No droplet or tank is invented.

Text reuse/layout brief: exact uppercase lines 'AD' then 'BLUE', both
left-aligned, with this wave spanning the width below the second line.
Reuse preferred glyph paths from icon_set/typeface/glyphs.json:
AD = letter-a-uppercase, letter-d-uppercase;
BLUE = letter-b-uppercase, letter-l-uppercase, letter-u-uppercase,
letter-e-uppercase. Preserve the two-line arrangement. Text is separate
from this SOLO48 wave component; this SVG alone is not an AdBlue wordmark.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "ddba64a9-7a33-401d-9571-bce55808907f"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/adblue indicator 1_ddba64a9-7a33-401d-9571-bce55808907f.svg"
AUTHOR = "gpt-6"


class AdblueFluidLevelWave(Solo48):
    icon_id = "adblue-fluid-level-wave"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/uncategorized"
    aliases = ("AdBlue indicator wave", "fluid-level wave")
    keywords = ("adblue", "fluid", "level", "indicator", "wave", "liquid")

    def build(self):
        start_x, baseline, step = 4, 24, 10
        handles = []
        for index in range(4):
            x = start_x + index*step
            amplitude = 6 if index % 2 == 0 else -6
            handles.append(((x+3, baseline+amplitude),
                            (x+step-3, baseline+amplitude),
                            (x+step, baseline)))
        self.add_bezier("fluid-wave", (start_x, baseline), *handles)
