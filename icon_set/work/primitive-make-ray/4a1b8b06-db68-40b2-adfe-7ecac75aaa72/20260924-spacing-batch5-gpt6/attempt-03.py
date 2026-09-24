"""Shoemaker apron bust and separate shoe. Human user.svg proportions; exact head gap 18 to 26. Apron seams merged into garment silhouette.
Plan: shared dimensions and attachment nodes; exact SQUARE envelope."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4a1b8b06-db68-40b2-adfe-7ecac75aaa72'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shoemaker_4a1b8b06-db68-40b2-adfe-7ecac75aaa72.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='shoemaker'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('shoemaker',)
    def build(self):
        self.circle('head',16,12,6)
        self.add_arc('torso',(16,26),(6,36),radius_x=10,sweep=False)
        self.add_line('side-left',(6,36),(6,42))
        self.add_line('base',(6,42),(18,42))
        self.add_line('side-right',(18,42),(18,26))
        self.add_line('top',(18,26),(16,26))
        self.add_contour('body','torso','side-left','base','side-right','top',closed=True)
        self.add_polyline('shoe',(27,30),(35,34),(42,34),(42,42),(27,42),closed=True)
        self.mark_human_figure('shoemaker',head='head',torso='torso',torso_junction='start')

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
