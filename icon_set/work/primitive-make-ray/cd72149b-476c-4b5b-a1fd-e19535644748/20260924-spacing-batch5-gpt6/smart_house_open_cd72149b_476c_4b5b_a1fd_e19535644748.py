"""Smart house and opening chevrons with wireless arc above. Lucide house-wifi informs coherent house contour. Omit inner wireless arc to reserve a full band above roof.
Plan: shared dimensions and attachment nodes; exact VRECT_L envelope."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cd72149b-476c-4b5b-a1fd-e19535644748'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smart house open_cd72149b-476c-4b5b-a1fd-e19535644748.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smart-house-open'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smart house open',)
    def build(self):
        self.add_arc('wireless',(16,8),(32,8),radius_x=8,radius_y=4)
        self.add_polyline('house',(8,28),(24,17),(40,28),(40,44),(8,44),closed=True)
        for side in (0,1):
            def p(x,y):return (48-x if side else x,y)
            self.add_polyline(f'open-{side}',p(20,30),p(17,33),p(20,36))

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
