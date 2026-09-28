"""Person and Business Growth Chart.
Plan: Presentation scene: person at left, rising chart at right. Shared human_ref/user.svg bust proportions and 8-unit head clearance.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Presenter bust, board stand and rising arrow retained. Head r4, center(12,23), shoulder apex(12,35): gap8 / ink4.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide panels-top-left; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aca4af14-d513-5480-b973-52f14722c981'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-and-business-growth-chart-solo-b002-12/20260927T145836Z-thuan-mac-1/reference/customer relationship management performance metrics_aca4af14-d513-5480-b973-52f14722c981.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-002/references/customer relationship management performance metrics_aca4af14-d513-5480-b973-52f14722c981.svg'
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
    icon_id = 'person-and-business-growth-chart-solo-b002-12'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('person', 'and', 'business', 'growth', 'chart')

    def build(self):
        s = self
        # The source shows a presenter bust below the board, not a walking stick figure.
        circle(s,'head',12,23,4)
        s.add_bezier('shoulder-left',(6,42),((6,38),(8,35),(12,35)))
        s.add_bezier('shoulder-right',(12,35),((16,35),(18,38),(18,42)))
        s.add_line('bust-base',(18,42),(6,42))
        s.add_contour('bust','shoulder-left','shoulder-right','bust-base',closed=True)
        s.add_polyline('board',(24,6),(42,6),(42,34),(34,34),(30,34))
        s.add_line('board-post',(34,34),(34,42))
        s.add_line('board-foot',(30,42),(38,42))
        join(s,'board','board-post');join(s,'board-post','board-foot')
        s.add_line('growth-series',(28,25),(33,16))
        s.add_polyline('growth-tip',(29,16),(33,16),(33,20))
        join(s,'growth-series','growth-tip')
