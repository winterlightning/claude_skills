"""A thermometer has a narrow upright tube with a rounded top and a broad circular bulb at its base. A short vertical column stands inside the tube above a tiny bulb-center point."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35927974-2629-44d6-b1c5-b8e9cce40d6f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/thermometer_35927974-2629-44d6-b1c5-b8e9cce40d6f.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'vertical-temperature-measurement-gauge-batch-032'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('vertical-temperature-measurement-gauge',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Thermometer with round lower bulb and narrow tube; extrema (10,4)-(38,44).

        self.add_arc('cap',(15,13),(33,13),radius_x=9)
        self.add_line('tube-right',(33,13),(33,26))
        self.add_bezier('bulb-right',(33,26),((36,28),(38,30),(38,34)),((38,40),(32,44),(24,44)))
        self.add_bezier('bulb-left',(24,44),((16,44),(10,40),(10,34)),((10,30),(12,28),(15,26)))
        self.add_line('tube-left',(15,26),(15,13))
        self.add_contour('outline','cap','tube-right','bulb-right','bulb-left','tube-left',closed=True)
        self.add_line('mercury',(24,14),(24,34))
