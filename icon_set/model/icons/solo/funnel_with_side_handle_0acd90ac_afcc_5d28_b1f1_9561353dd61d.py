"""Funnel with Side Handle.
Plan: An elliptical open rim feeds sloped sides and a rounded outlet; the side handle shares rim and shoulder junctions. Ink (6,2)-(42,46).
Reference construction: funnel.
Reduction: Use one generous handle loop and a rounded outlet; retain the oval open rim.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0acd90ac-afcc-5d28-b1f1-9561353dd61d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/filter_0acd90ac-afcc-5d28-b1f1-9561353dd61d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'funnel-with-side-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('funnel', 'with', 'side', 'handle')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('rim-top',(8,10),(32,10),radius_x=12,radius_y=6)
        self.add_arc('rim-bottom',(32,10),(8,10),radius_x=12,radius_y=6)
        self.add_contour('rim','rim-top','rim-bottom',closed=True)
        self.add_polyline('left',(8,10),(16,30),(16,40))
        self.add_arc('outlet',(16,40),(24,40),radius_x=4,sweep=False)
        self.add_polyline('right',(24,40),(24,30),(32,10))
        self.relate('connect','left','rim');self.relate('connect','right','rim');self.relate('connect','left','outlet');self.relate('connect','right','outlet')
        self.add_bezier('handle',(32,10),((36,10),(40,14),(40,22)),((40,34),(28,36),(24,30)))
        self.relate('connect','handle','rim');self.relate('connect','handle','right')
