"""Circular transformation tool, resumed for saved batch-025.
Symbol plan: open circular disc with a shared radial arm, round handle endpoint,
diagonal control arrow and two detached curved rotation cues.
VRECT_L centerline bounds: (8,4)-(40,44). Rebalanced on the SOLO48 integer grid.
Reduction: widen the disc opening; use the round cap for the tiny handle ring;
shorten outer arrowheads and remove crowded return strokes. The asymmetry
preserves the distinct radial controls and surrounding rotation cues.
Lucide repeat-2 original and atomic-debug informed separated turning arrows.
Validation and release QA pass; reviewed at native 48px in light and dark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3f7ad31-1cbe-40ca-b4de-da206b319982'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/transform shrink_e3f7ad31-1cbe-40ca-b4de-da206b319982.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-005/references/transform shrink_e3f7ad31-1cbe-40ca-b4de-da206b319982.svg'
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
    icon_id = 'circular-transformation-tool-solo-b005-11'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('circular', 'transformation', 'tool')

    def build(self):
        # Open disc, radial handle/arrow, and two independent rotation arrows.
        # VRECT_L extrema x8/40 and y4/44; no profile exceptions.
        self.add_arc('disc-top',(32,25),(12,25),radius_x=10,sweep=False)
        self.add_arc('disc-lower-left',(12,25),(14,31),radius_x=10,sweep=False)
        self.add_contour('disc','disc-top','disc-lower-left')
        self.add_polyline('radial',(38,25),(32,25),(22,25),(34,39))
        self.relate('connect','radial','disc')
        self.add_dot('handle',(38,25))
        self.relate('connect','handle','radial')
        self.add_polyline('radial-tip',(26,39),(34,39),(34,33))
        self.relate('connect','radial','radial-tip')
        self.add_bezier('rotation-top',(16,4),((28,4),(35,6),(40,12)))
        self.add_polyline('rotation-top-tip',(40,4),(40,12),(35,12))
        self.relate('connect','rotation-top','rotation-top-tip')
        self.add_bezier('rotation-bottom',(19,44),((16,44),(12,44),(8,42)))
        self.add_polyline('rotation-bottom-tip',(8,37),(8,42),(16,42))
        self.relate('connect','rotation-bottom','rotation-bottom-tip')
