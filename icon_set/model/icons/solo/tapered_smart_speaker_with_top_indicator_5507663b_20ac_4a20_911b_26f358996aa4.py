"""Smart Home Speaker.

Symbol plan: Tapered smart speaker with elliptical top and rounded base. Shared x=24 axis and paired walls. Lucide speaker informs rounded enclosure; supplied source owns tapered cylindrical shape. Keep top indicator; enlarge top ellipse to clear mark. Lower seam retained.
Keyshape VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5507663b-20ac-4a20-911b-26f358996aa4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/google home_5507663b-20ac-4a20-911b-26f358996aa4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tapered-smart-speaker-with-top-indicator'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('smart', 'home', 'speaker')

    def build(self):
        self.add_arc('top-upper',(12,13),(36,13),radius_x=12,radius_y=9)
        self.add_arc('top-lower',(36,13),(12,13),radius_x=12,radius_y=9)
        self.add_contour('top','top-upper','top-lower',closed=True)
        self.add_line('wall-right',(36,13),(40,34));self.add_line('right-bottom',(40,34),(40,38))
        self.add_arc('br',(40,38),(34,44),radius_x=6);self.add_line('bottom',(34,44),(14,44))
        self.add_arc('bl',(14,44),(8,38),radius_x=6);self.add_line('left-bottom',(8,38),(8,34))
        self.add_line('wall-left',(8,34),(12,13))
        self.add_contour('body','wall-right','right-bottom','br','bottom','bl','left-bottom','wall-left');self.relate('connect','body','top')
        self.add_line('seam',(8,34),(40,34));self.relate('connect','seam','body')
        self.add_line('indicator',(23,13),(25,13))
