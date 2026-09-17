"""Barbecue Spatula and Fork."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80c8c0d1-f1c1-5175-aa1d-de1426015110'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barbecue set_80c8c0d1-f1c1-5175-aa1d-de1426015110.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'barbecue-spatula-and-fork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('barbecue', 'spatula', 'fork', 'utensil', 'grilling', 'cooking', 'tool')

    def build(self):
        # Plan: Upright spatula and two-tine fork share handle proportions and baseline. Single spatula slot; Lucide utensils for joined shafts. Bounds (6,6)-(42,42).
        self.add_polyline('spatula',(6,6),(24,6),(24,24),(15,24),(6,24),closed=True)
        self.add_line('slot',(15,14),(15,16))
        self.add_line('shaft-0',(15,24),(15,32))
        self.relate('connect','shaft-0','spatula')
        self.add_line('fork-left',(34,6),(34,20))
        self.add_arc('fork-bl',(34,20),(38,24),radius_x=4,sweep=False)
        self.add_arc('fork-br',(38,24),(42,20),radius_x=4,sweep=False)
        self.add_line('fork-right',(42,20),(42,6))
        self.add_contour('fork','fork-left','fork-bl','fork-br','fork-right')
        self.add_line('shaft-1',(38,24),(38,32));self.relate('connect','shaft-1','fork')
        for i,x in enumerate((15,38)):
            self.add_arc(f'h-tl-{i}',(x,32),(x-4,36),radius_x=4,sweep=False)
            self.add_line(f'h-l-{i}',(x-4,36),(x-4,38))
            self.add_arc(f'h-b-{i}',(x-4,38),(x+4,38),radius_x=4,sweep=False)
            self.add_line(f'h-r-{i}',(x+4,38),(x+4,36))
            self.add_arc(f'h-tr-{i}',(x+4,36),(x,32),radius_x=4,sweep=False)
            self.add_contour(f'handle-{i}',f'h-tl-{i}',f'h-l-{i}',f'h-b-{i}',f'h-r-{i}',f'h-tr-{i}',closed=True)
            self.relate('connect',f'shaft-{i}',f'handle-{i}')
