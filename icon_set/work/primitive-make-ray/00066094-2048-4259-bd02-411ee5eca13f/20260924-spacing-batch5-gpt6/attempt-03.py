"""Compass above SW label. Omit dial ticks and open the pointer to reduce small enclosed holes. No useful exact Lucide match; source direction retained.
Plan: shared dimensions and attachment nodes; exact VRECT_L envelope."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='00066094-2048-4259-bd02-411ee5eca13f'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/south west_00066094-2048-4259-bd02-411ee5eca13f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='south-west'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('south west',)
    def build(self):
        self.circle('dial',24,15,11)
        self.add_polyline('pointer',(22,15),(26,13),(24,17))
        self.add_bezier('s',(17,35),((8,30),(6,38),(13,39)),((21,40),(17,44),(8,43)))
        self.add_polyline('w',(25,34),(25,44),(32,40),(40,44),(40,34))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l=6,t=6,r=42,b=42,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        for k in range(8):
            if k%2:self.add_arc(f'{n}-{k}',pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(f'{n}-{k}',pts[k],pts[(k+1)%8])
        self.add_contour(n,*(f'{n}-{k}' for k in range(8)),closed=True)
    def cross(self,n,x,y,r):
        ids=[]
        for k,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            ident=f'{n}-{k}';self.add_line(ident,(x,y),(x+dx,y+dy));ids.append(ident)
        for k,a in enumerate(ids):
            for b in ids[k+1:]:self.relate('connect',a,b)
