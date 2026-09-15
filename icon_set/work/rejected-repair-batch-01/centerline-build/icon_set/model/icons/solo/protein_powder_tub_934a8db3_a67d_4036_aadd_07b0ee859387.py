"""Protein powder tub, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='934a8db3-a67d-4036-aadd-07b0ee859387'
SOURCE_PATH='pictographic-primitives/sports/protein_934a8db3-a67d-4036-aadd-07b0ee859387.svg'
AUTHOR='gpt-6'

class ProteinPowderTub(Solo48):
    icon_id='protein-powder-tub'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('protein', 'powder', 'tub')
    def build(self) -> None:
        # VRECT_L centerline extremes (8, 4, 40, 44).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        self.add_polyline('lid',(12,14),(12,4),(36,4),(36,14),closed=True)
        self.add_line('top',(12,14),(36,14))
        arc('shoulder-right',(36,14),(40,18),4)
        self.add_line('right',(40,18),(40,38))
        arc('bottom-right',(40,38),(34,44),6)
        self.add_line('bottom',(34,44),(14,44))
        arc('bottom-left',(14,44),(8,38),6)
        self.add_line('left',(8,38),(8,18))
        arc('shoulder-left',(8,18),(12,14),4)
        self.add_contour('jar','top','shoulder-right','right','bottom-right','bottom','bottom-left','left','shoulder-left',closed=True)
        self.relate('connect','lid','jar')
        for side,x in [('left',18),('right',30)]:
            self.add_line(side+'-upper',(x,25),(x,29))
            self.add_line(side+'-lower',(x,29),(x,33))
            self.add_contour(side+'-weight',side+'-upper',side+'-lower')
        self.add_line('bar',(18,29),(30,29))
        self.relate('connect','bar','left-weight')
        self.relate('connect','bar','right-weight')
