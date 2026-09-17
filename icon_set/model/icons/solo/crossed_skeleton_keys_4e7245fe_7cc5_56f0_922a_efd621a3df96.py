"""Crossed Skeleton Keys.
Plan: Two equal bows and crossing diagonal stems mirror x24; one widely separated terminal tooth per stem. Ink (4,4)-(44,44).
Reference construction: key-round.
Reduction: Keep one tooth per key instead of two to maintain clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4e7245fe-7cc5-56f0-922a-efd621a3df96'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/login keys_4e7245fe-7cc5-56f0-922a-efd621a3df96.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'crossed-skeleton-keys'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('crossed', 'skeleton', 'keys')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,cx,s in [('left',11,1),('right',37,-1)]:
         pts=[(cx,6),(cx+5*s,11),(cx+3*s,15),(cx,16),(cx-5*s,11),(cx,6)]
         for j,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'{label}-bow-{j}',a,b,radius_x=5,sweep=(s==1))
         self.add_contour(label+'-bow',*(f'{label}-bow-{j}' for j in range(5)),closed=True)
         self.add_polyline(label+'-stem',(cx+3*s,15),(24,25),(35 if s==1 else 13,36),(41 if s==1 else 7,42))
         self.relate('connect',label+'-bow',label+'-stem')
         self.add_line(label+'-tooth',(35 if s==1 else 13,36),(40 if s==1 else 8,31))
         self.relate('connect',label+'-tooth',label+'-stem')
        self.relate('connect','left-stem','right-stem')
