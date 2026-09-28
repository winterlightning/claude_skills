"""Open Catalog with Dollar Sign.
Plan: Open catalog with a short text mark and hand-drawn currency curve.
Centerline envelope: (4,8)-(44,40).
Final reduction/review: the currency curve fits the right page at native size.
Keyshape: HRECT_L; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide newspaper; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '24fd53e6-156c-4466-9207-a789aa1d1627'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-catalog-with-dollar-sign-solo-b002-10/20260927T133654Z-thuan-mac-1/reference/workflow coaching product catalog_24fd53e6-156c-4466-9207-a789aa1d1627.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-002/references/workflow coaching product catalog_24fd53e6-156c-4466-9207-a789aa1d1627.svg'
AUTHOR = 'gpt-6'

def circle(s,n,x,y,r):
    s.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
    s.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
    s.add_contour(n,n+'-a',n+'-b',closed=True)

def box(s,n,l,t,r,b,k=3,nodes=()):
    pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k),(l+k,t)]
    members=[]
    for i,(a,z) in enumerate(zip(pts,pts[1:])):
        if a==z: continue
        if i%2:
            q=f'{n}-{i}';s.add_arc(q,a,z,radius_x=k);members.append(q)
        else:
            dx,dy=z[0]-a[0],z[1]-a[1]
            cuts=sorted([p for p in nodes if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy],key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy)
            seq=[a]+cuts+[z]
            for j,(u,v) in enumerate(zip(seq,seq[1:])):
                q=f'{n}-{i}-{j}';s.add_line(q,u,v);members.append(q)
    s.add_contour(n,*members,closed=True)

def join(s,a,b):
    s.relate('connect',a,b)

def arrow(s,n,a,z,w=7):
    s.add_line(n+'-shaft',a,z)
    dx,dy=z[0]-a[0],z[1]-a[1]
    if dy==0: pts=((z[0]-(w if dx>0 else -w),z[1]-w),z,(z[0]-(w if dx>0 else -w),z[1]+w))
    elif dx==0: pts=((z[0]-w,z[1]-(w if dy>0 else -w)),z,(z[0]+w,z[1]-(w if dy>0 else -w)))
    else: pts=((z[0]-(w if dx>0 else -w),z[1]),z,(z[0],z[1]-(w if dy>0 else -w)))
    s.add_polyline(n+'-tip',*pts);join(s,n+'-shaft',n+'-tip')

class GeneratedSolo(Solo48):
    icon_id = 'open-catalog-with-dollar-sign-solo-b002-10'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('open', 'catalog', 'with', 'dollar', 'sign')

    def build(self):
        s = self
        # Shift the fold left to reserve a legible right page for the dollar.
        s.add_polyline('book',(4,8),(12,8),(20,10),(32,8),(44,8),
                       (44,34),(32,34),(20,40),(12,34),(4,34),closed=True)
        s.add_line('spine',(20,10),(20,40));join(s,'book','spine')
        s.add_line('text',(12,22),(12,26))
        # A single continuous currency curve survives the small right page.
        s.add_bezier('dollar-s',(35,17),((30,17),(29,19),(34,21)),
                     ((36,23),(36,25),(33,25)))
