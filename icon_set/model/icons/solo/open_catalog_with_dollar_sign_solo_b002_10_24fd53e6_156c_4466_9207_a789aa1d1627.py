"""Open Catalog with Dollar Sign.
Plan: Open catalog with text lines and existing dollar glyph; glyph reuse handled separately.
Centerline envelope: (4,8)-(44,40).
Final reduction/review: INCOMPLETE: dollar glyph reuse cannot yet fit the page under SOLO48 grid and spacing constraints; book draft preserved.
Keyshape: HRECT_L; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide newspaper; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '24fd53e6-156c-4466-9207-a789aa1d1627'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/workflow coaching product catalog_24fd53e6-156c-4466-9207-a789aa1d1627.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-002/references/workflow coaching product catalog_24fd53e6-156c-4466-9207-a789aa1d1627.svg'
AUTHOR = 'gpt-6'
REQUIRED_TYPEFACE_GLYPH = 'symbol-dollar'
TYPEFACE_SOURCE = 'icon_set/typeface/glyphs.json'
INCOMPLETE_REASON = 'Existing dollar glyph uses fractional cubic coordinates and spans 46 units vertically; legal placement in the narrow catalog page is unresolved without altering glyph geometry or violating SOLO48 grid/clearance.'

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
    aliases = ()
    keywords = ('open', 'catalog', 'with', 'dollar', 'sign')

    def build(self):
        s = self
        s.add_polyline('book',(4,8),(14,8),(24,14),(34,8),(44,8),(44,34),(34,34),(24,40),(14,34),(4,34),closed=True)
        s.add_line('spine',(24,14),(24,40));join(s,'book','spine')
        s.add_line('text',(12,22),(16,24))
