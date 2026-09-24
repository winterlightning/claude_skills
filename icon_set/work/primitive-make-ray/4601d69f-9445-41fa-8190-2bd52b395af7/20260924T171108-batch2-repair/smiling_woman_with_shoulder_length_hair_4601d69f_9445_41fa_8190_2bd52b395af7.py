"""babe. Plan: SQUARE extremes (6,6)-(42,42); shared x=24 hair envelope and circular radius-9 jaw; shoulder apex y35 gives zero visible gap to jaw bottom y31 (4 centerline units). Human user.svg and its avatar construction rule inform circular jaw and broad shoulders. Small eyes and smile omitted to preserve clearance; source hair parting retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4601d69f-9445-41fa-8190-2bd52b395af7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/babe_4601d69f-9445-41fa-8190-2bd52b395af7.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    human_construction = "bust"
    icon_id = 'smiling-woman-with-shoulder-length-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('babe',)
    def path(self,n,start,steps,closed=False):
        here=start;members=[]
        for k,step in enumerate(steps):
            ident=f'{n}-{k}';members.append(ident)
            if len(step)==2:
                self.add_line(ident,here,step);here=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep);here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,q=0):
        if q==0:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        else:self.path(n,(l+q,t),[(r-q,t),((r,t+q),q,q,True),(r,b-q),((r-q,b),q,q,True),(l+q,b),((l,b-q),q,q,True),(l,t+q),((l+q,t),q,q,True)],True)
    def build(self):
        self.path('hair',(6,30),[(6,24),((24,6),18,18,True),((42,24),18,18,True),(42,30)])
        self.add_bezier('hairline',(15,22),((21,22),(25,19),(27,16)),((28,19),(30,21),(33,22)))
        self.add_arc('jaw-right',(33,22),(24,31),radius_x=9)
        self.add_arc('jaw-left',(24,31),(15,22),radius_x=9)
        self.add_contour('face','hairline','jaw-right','jaw-left',closed=True)
        self.path('body',(6,42),[((24,35),18,7,True),((42,42),18,7,True)])
        self.relate('connect','face','body')
