"""Two facing square brackets.
Plan: Mirrored open bracket contours derive from a shared axis and radius.
Construction: square-chevron-left: rounded outer corner construction
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'db17be1c-0953-4814-9bc2-733e7e3fec97'
SOURCE_PATH = 'icon_set/work/todo-references/square brackets_db17be1c-0953-4814-9bc2-733e7e3fec97.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-brackets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'brackets')

    def build(self):
        for side in (0,1):
            def p(x,y):return (48-x if side else x,y)
            n=f'bracket-{side}'
            self.add_line(n+'-top',p(14,6),p(10,6))
            self.add_arc(n+'-upper',p(10,6),p(6,10),radius_x=4,sweep=bool(side))
            self.add_line(n+'-side',p(6,10),p(6,38))
            self.add_arc(n+'-lower',p(6,38),p(10,42),radius_x=4,sweep=bool(side))
            self.add_line(n+'-bottom',p(10,42),p(14,42))
            self.add_contour(n,*(n+s for s in ('-top','-upper','-side','-lower','-bottom')))

    def box(self,name,l=6,t=6,r=42,b=42,rad=4):
        mx,my=(l+r)//2,(t+b)//2
        pts=[(mx,t),(r-rad,t),(r,t+rad),(r,my),(r,b-rad),(r-rad,b),(mx,b),(l+rad,b),(l,b-rad),(l,my),(l,t+rad),(l+rad,t)]
        for i in range(12):
            a,z=pts[i],pts[(i+1)%12]
            if i in (1,4,7,10):self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(12)),closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def arrow(self,name,start,tip,a,b):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',a,tip,b)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')
