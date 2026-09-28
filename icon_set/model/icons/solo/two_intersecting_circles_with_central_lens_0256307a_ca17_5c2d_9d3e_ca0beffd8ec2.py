"""Two Overlapping Circles.

Plan: Two overlapping circle-like outlines, represented as four genuinely intersecting open branches; bounds (4,8)-(44,40). Mirrored lens branches retain a regular overlap.
Construction reference: No useful exact Lucide match; paired tangent elliptical quadrants.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0256307a-ca17-5c2d-9d3e-ca0beffd8ec2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/boolean or_0256307a-ca17-5c2d-9d3e-ca0beffd8ec2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-intersecting-circles-with-central-lens'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('two', 'overlapping', 'circles')

    def build(self):
        for side in (-1,1):
         def p(x,y): return (24+side*x,y)
         path(self,f'outer-{side}',p(0,12),('A',8,4,side>0,p(8,8)),('A',12,16,side>0,p(20,24)),('A',12,16,side>0,p(8,40)),('A',8,4,side>0,p(0,36)))
         path(self,f'inner-{side}',p(0,12),('A',8,12,side>0,p(8,24)),('A',8,12,side>0,p(0,36)))
        contacts(self)
