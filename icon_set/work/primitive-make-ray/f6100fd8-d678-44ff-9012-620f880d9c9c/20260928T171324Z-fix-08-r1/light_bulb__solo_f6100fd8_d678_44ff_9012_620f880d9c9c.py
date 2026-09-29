"""Restored a taller circular globe, smooth narrowing neck and rounded closed socket."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f6100fd8-d678-44ff-9012-620f880d9c9c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__light-bulb-f6100fd8-d678-44ff-9012-620f880d9c9c-solo/20260928T171324Z-thuan-mac/reference/light bulb_f6100fd8-d678-44ff-9012-620f880d9c9c.svg'
AUTHOR='gpt-6'
PLAN='Restored a taller circular globe, smooth narrowing neck and rounded closed socket.'
CONSTRUCTION_REFERENCE='Lucide lightbulb: circular glass transitioning to a narrow socket; source retains a closed base.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='light-bulb-f6100fd8-d678-44ff-9012-620f880d9c9c-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('light', 'bulb', 'f6100fd8', 'd678', '44ff', '9012', '620f880d9c9c', 'solo')

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
        # Shared axis24, circular upper globe radius16, mirrored necks and equal socket corners.
        self.path('bulb',(8,20),[('A',(40,20),16,16,True),('C',(30,36),(40,29),(31,29)),('L',(30,40)),('A',(26,44),4,4,True),('L',(22,44)),('A',(18,40),4,4,True),('L',(18,36)),('C',(8,20),(17,29),(8,29))],True)
        self.add_line('socket-seam',(18,36),(30,36));self.relate('connect','bulb','socket-seam')
