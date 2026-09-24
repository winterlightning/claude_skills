"""Two Intersecting Circles.

Plan: Two overlapping circle-like outlines, represented as four genuinely intersecting open branches; bounds (4,8)-(44,40). A short angular inner segment preserves the source irregularity.
Construction reference: No useful exact Lucide match; paired tangent elliptical quadrants.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ea7a2587-afc3-5980-b5c6-35471cead545'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/boolean and_ea7a2587-afc3-5980-b5c6-35471cead545.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'intersecting-circles-with-angular-inner-segment'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    aliases = ()
    keywords = ('two', 'intersecting', 'circles')

    def build(self):
        for side in (-1,1):
         def p(x,y): return (24+side*x,y)
         path(self,f'outer-{side}',p(0,12),('A',8,4,side>0,p(8,8)),('A',12,16,side>0,p(20,24)),('A',12,16,side>0,p(8,40)),('A',8,4,side>0,p(0,36)))
         if side == 1:
          path(self,'inner-angular',p(0,12),('L',p(6,18)),('A',8,12,True,p(0,36)))
         else:
          path(self,'inner-left',p(0,12),('A',8,12,False,p(8,24)),('A',8,12,False,p(0,36)))
        contacts(self)
