"""Chisel Carving Wood.

Plan: Diagonal capsule grip and shaft contact a wavy carved wood surface. Keep one clear recess, drop fine grain line. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93d527dc-470b-58d5-8ae9-b6db1ca51be0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/wood carving_93d527dc-470b-58d5-8ae9-b6db1ca51be0.svg'
AUTHOR = 'gpt-6'


class ChiselCarvingWood(Solo48):
    icon_id = 'chisel-carving-wood'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('chisel', 'carving', 'wood')

    def build(self):
        self.add_arc('handle-top',(33,8),(41,14),radius_x=5)
        self.add_line('handle-r',(41,14),(38,18))
        self.add_arc('handle-bottom-r',(38,18),(31,19),radius_x=5)
        self.add_arc('handle-bottom-l',(31,19),(30,12),radius_x=5)
        self.add_line('handle-l',(30,12),(33,8))
        self.add_contour('handle','handle-top','handle-r','handle-bottom-r','handle-bottom-l','handle-l',closed=True)

        self.add_line('shaft',(31,19),(22,34))
        self.add_line('wood-top-left',(6,30),(14,30))
        self.add_arc('cut-left',(14,30),(22,34),radius_x=8,radius_y=4,sweep=False)
        self.add_arc('cut-right',(22,34),(30,30),radius_x=8,radius_y=4,sweep=False)
        self.add_polyline('wood-base',(30,30),(42,30),(42,42),(6,42),(6,30))
        self.add_contour('wood','wood-top-left','cut-left','cut-right','wood-base-1','wood-base-2','wood-base-3','wood-base-4',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='wood-base']
        self.relate('connect','handle','shaft')
        self.relate('connect','shaft','wood')
