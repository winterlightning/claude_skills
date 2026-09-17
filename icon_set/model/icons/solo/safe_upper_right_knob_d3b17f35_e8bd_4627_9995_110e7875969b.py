"""Security Storage Safe Box.
Plan: Wide rounded safe with upper-right knob, left hinge and short feet. Extrema (4,8)-(44,40).
Reference: Lucide vault: rounded cabinet and sparse door hardware.
Reduction: Inset border reduced to one left hinge line; offset knob retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3b17f35-e8bd-4627-9995-110e7875969b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/saving safe_d3b17f35-e8bd-4627-9995-110e7875969b.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'safe-upper-right-knob'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ()
    keywords = ('security', 'storage', 'safe', 'box')

    def build(self):

        self.add_line('cabinet-top',(8,8),(40,8))
        self.add_arc('cabinet-tr',(40,8),(44,12),radius_x=4)
        self.add_line('cabinet-right',(44,12),(44,32))
        self.add_arc('cabinet-br',(44,32),(40,36),radius_x=4)
        self.add_line('cabinet-base',(40,36),(8,36))
        self.add_arc('cabinet-bl',(8,36),(4,32),radius_x=4)
        self.add_line('cabinet-left',(4,32),(4,12))
        self.add_arc('cabinet-tl',(4,12),(8,8),radius_x=4)
        self.add_contour('cabinet',*[f'cabinet-{s}' for s in ('top','tr','right','br','base','bl','left','tl')],closed=True)

        self.add_arc('knob-a',(31,17),(31,23),radius_x=3)
        self.add_arc('knob-b',(31,23),(31,17),radius_x=3)
        self.add_contour('knob','knob-a','knob-b',closed=True)

        self.add_line('hinge',(14,18),(14,26))
        for i,x in enumerate((8,40)):
            self.add_line(f'foot-{i}',(x,36),(x,40));self.relate('connect','cabinet',f'foot-{i}')
