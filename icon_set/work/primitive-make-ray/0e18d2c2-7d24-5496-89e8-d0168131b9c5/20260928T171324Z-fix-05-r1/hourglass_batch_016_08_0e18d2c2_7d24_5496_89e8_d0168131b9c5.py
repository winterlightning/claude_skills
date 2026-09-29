"""Opened the waist, restored curved chambers and added short projecting top and bottom caps."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0e18d2c2-7d24-5496-89e8-d0168131b9c5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hourglass-batch-016-08/20260928T171324Z-thuan-mac/reference/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
AUTHOR='gpt-6'
PLAN='Opened the waist, restored curved chambers and added short projecting top and bottom caps.'
CONSTRUCTION_REFERENCE='Lucide hourglass: paired chambers and projecting caps; source: continuous open waist.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='hourglass-batch-016-08'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('hourglass', 'batch', '016', '08')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):
        self.path('glass',(12,4),[('L',(36,4)),('L',(36,12)),('C',(28,24),(36,18),(28,19)),('C',(36,36),(28,29),(36,30)),('L',(36,44)),('L',(12,44)),('L',(12,36)),('C',(20,24),(12,30),(20,29)),('C',(12,12),(20,19),(12,18)),('L',(12,4))],True)
        for y in (4,44):
            for a,b in ((8,12),(36,40)):
                n=f'cap-{y}-{a}';self.add_line(n,(a,y),(b,y));self.relate('connect','glass',n)
