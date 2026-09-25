"""Hourglass; standalone reconstruction of the supplied reference.
Construction: Lucide hourglass informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e18d2c2-7d24-5496-89e8-d0168131b9c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hourglass'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('hourglass', 'time', 'timer', 'glass', 'chambers', 'waist')

    def build(self):
        # Plan: paired S-curves share a vertical tangent at the open waist.
        # VRECT_L extremes x=8/40, y=4/44; round-ended projecting rails.
        axis=24
        for side,sign in (("left",-1),("right",1)):
            x=axis+sign*12
            waist=axis+sign*5
            self.add_line(side+"-upper",(x,4),(x,10))
            self.add_bezier(side+"-glass",(x,10),
                ((x,18),(waist,18),(waist,24)),
                ((waist,30),(x,30),(x,38)))
            self.add_line(side+"-lower",(x,38),(x,44))
            self.add_contour(side,side+"-upper",side+"-glass",side+"-lower")
        for end,y in (("top",4),("bottom",44)):
            self.add_polyline(end,(8,y),(12,y),(36,y),(40,y))
            for side in ("left","right"):
                self.relate("connect",end,side)
