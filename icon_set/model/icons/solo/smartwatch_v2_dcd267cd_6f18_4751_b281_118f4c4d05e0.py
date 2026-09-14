# Variant of smartwatch; parent file remains unchanged.
'Smartwatch: independent spacing revision.\n\nSmaller square face and open wrapping strap edges; remove narrow inner strap returns.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from __future__ import annotations
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dcd267cd-6f18-4751-b281-118f4c4d05e0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/watch_dcd267cd-6f18-4751-b281-118f4c4d05e0.svg'
AUTHOR = 'gpt-6'

class SmartwatchVariant2(Solo48):
    """A square smartwatch case with an open strap sweeping right.

    The source draws four separate runs of sampled points: two long outer strap
    edges sweeping from the case's left side around to the right, and two short
    inner edges that converge with them at each strap tip. The case keeps the
    source's proportions -- half the canvas wide, corner radius one sixth of
    its width -- and its position left of centre so the strap has room.

    Each strap edge begins on a case wall and the two edges of a strap share
    their tip, so the whole drawing is one connected component, exactly as in
    the source. That is also what keeps the spacing engine from reading a
    strap's own width as a clearance failure.
    """
    icon_id = 'smartwatch-v2'
    variant_of = 'smartwatch'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    category = 'objects/device'
    aliases = ('watch', 'wearable', 'smart-watch')
    keywords = ('watch', 'wearable', 'device', 'strap', 'band', 'time')

    def build(self):
        self.add_polyline('case-top',(9, 15),(12, 15),(21, 15),closed=False)
        self.add_arc('ne',(21, 15),(24, 18),radius_x=3,radius_y=3,sweep=True)
        self.add_line('right',(24, 18),(24, 30))
        self.add_arc('se',(24, 30),(21, 33),radius_x=3,radius_y=3,sweep=True)
        self.add_polyline('case-bottom',(21, 33),(12, 33),(9, 33),closed=False)
        self.add_arc('sw',(9, 33),(6, 30),radius_x=3,radius_y=3,sweep=True)
        self.add_line('left',(6, 30),(6, 18))
        self.add_arc('nw',(6, 18),(9, 15),radius_x=3,radius_y=3,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'case-top']
        self.contours = [c for c in self.contours if c.contour_id != 'case-bottom']
        self.add_contour('case','case-top-1','case-top-2','ne','right','se','case-bottom-1','case-bottom-2','sw','left','nw',closed=True)
        self.add_line('top-stem',(12, 15),(12, 12))
        self.add_arc('top-rise',(12, 12),(18, 6),radius_x=6,radius_y=6,sweep=True)
        self.add_line('top-run',(18, 6),(30, 6))
        self.add_arc('top-fall',(30, 6),(42, 18),radius_x=12,radius_y=12,sweep=True)
        self.add_contour('top-strap','top-stem','top-rise','top-run','top-fall',closed=False)
        self.add_line('bottom-stem',(12, 33),(12, 36))
        self.add_arc('bottom-fall',(12, 36),(18, 42),radius_x=6,radius_y=6,sweep=False)
        self.add_line('bottom-run',(18, 42),(30, 42))
        self.add_arc('bottom-rise',(30, 42),(42, 30),radius_x=12,radius_y=12,sweep=False)
        self.add_contour('bottom-strap','bottom-stem','bottom-fall','bottom-run','bottom-rise',closed=False)
        self.relate('connect','case','top-strap')
        self.relate('connect','case','bottom-strap')
