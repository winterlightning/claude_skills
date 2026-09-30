'The rejected masked person resembles a hood and lacks natural shoulders beneath the pointed bandana.\nSymbol plan: Restore a circular upper head, a pointed face covering and broad shoulder curves.\nConstruction: Shared human bust reference and Lucide user-round: circular head proportions over balanced shoulders; the covering replaces the hidden jaw.\nOmissions: Omit the hair part and facial marks to preserve the large bandana.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3ae3206f-bd57-4113-91e0-f3d1229102a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-pointed-bandana-face-cover/20260929T125815Z-thuan-mac/reference/man riot 1_3ae3206f-bd57-4113-91e0-f3d1229102a9.svg'
AUTHOR = 'gpt-6'

def path(m,n,start,*steps,closed=False):
    names=[]; here=start
    for j,(kind,end,*args) in enumerate(steps):
        k=f'{n}-{j}'
        if kind=='L':m.add_line(k,here,end)
        elif kind=='C':m.add_bezier(k,here,(args[0],args[1],end))
        elif kind=='A':m.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        names.append(k);here=end
    m.add_contour(n,*names,closed=closed)
def circle(m,n,x,y,r):
    path(m,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)

class Drawing(Solo48):
    icon_id = 'person-with-pointed-bandana-face-cover'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'with', 'pointed', 'bandana', 'face', 'cover')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'head',(12,24),('L',(12,18)),('A',(36,18),12,12,True),('L',(36,24)))
        poly('mask',((12,24),(24,20),(36,24),(30,30),(24,36),(18,30),(12,24)))
        join('head','mask')
        path(m,'left-shoulder',(18,30),('C',(6,42),(8,30),(6,35)))
        path(m,'right-shoulder',(30,30),('C',(42,42),(40,30),(42,35)))
        join('mask','left-shoulder');join('mask','right-shoulder')
