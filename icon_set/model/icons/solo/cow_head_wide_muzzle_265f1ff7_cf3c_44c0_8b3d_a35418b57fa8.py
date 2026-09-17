"""Horned Cow Head.
Plan: Mirrored cow head with broad lower muzzle, horns and outward ears. Extrema (6,6)-(42,42).
Reference: Supplied source; no useful exact Lucide match. Coherent curves and shared attachment points.
Reduction: Eye dots and nostrils omitted where they would crowd the muzzle; broad face, horns and ears retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265f1ff7-cf3c-44c0-8b3d-a35418b57fa8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/milk cow_265f1ff7-cf3c-44c0-8b3d-a35418b57fa8.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'cow-head-wide-muzzle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('horned', 'cow', 'head')

    def build(self):

        self.add_polyline('face',(14,30),(14,16),(24,16),(34,16),(34,30))
        self.add_arc('muzzle-top',(14,30),(34,30),radius_x=10,radius_y=4)
        self.add_arc('muzzle-right',(34,30),(34,42),radius_x=6)
        self.add_line('muzzle-bottom',(34,42),(14,42))
        self.add_arc('muzzle-left',(14,42),(14,30),radius_x=6)
        self.add_contour('muzzle','muzzle-top','muzzle-right','muzzle-bottom','muzzle-left',closed=True)
        self.relate('connect','face','muzzle')
        for side in (-1,1):
            x=24+side*10
            self.add_bezier(f'horn-{side}',(x,16),((x+side*6,16),(x+side*8,10),(x+side*8,6)))
            self.relate('connect','face',f'horn-{side}')
            self.add_polyline(f'ear-{side}',(x,16),(x+side*8,20),(x+side*8,24))
            self.relate('connect','face',f'ear-{side}');self.relate('connect',f'horn-{side}',f'ear-{side}')
