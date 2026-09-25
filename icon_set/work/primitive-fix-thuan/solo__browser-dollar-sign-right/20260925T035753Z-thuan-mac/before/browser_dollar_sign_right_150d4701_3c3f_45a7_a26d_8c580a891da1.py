from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='150d4701-3c3f-45a7-a26d-8c580a891da1'
SOURCE_PATH='pictographic-primitives/other/browser dollar sign right_150d4701-3c3f-45a7-a26d-8c580a891da1.svg'
AUTHOR='gpt-6'
PLAN='Browser with right aligned dollar; Lucide dollar-sign terminals and rounded frame construction. Dollar diagonal waist opens lobes. Header title dots omitted for spacing.'
class Drawing(Solo48):
    icon_id='browser-dollar-sign-right'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('browser', 'dollar', 'sign', 'right')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('window',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,12)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,12)),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.add_line('header',(8,12),(40,12));self.relate('connect','header','window')
        self.path('dollar',(30,22),[('L',(26,22)),('L',(24,22)),('A',(22,24),2,2,False),('L',(30,32)),('A',(28,34),2,2,True),('L',(26,34)),('L',(22,34))])
        self.add_line('stem-top',(26,21),(26,22));self.add_line('stem-bottom',(26,34),(26,35))
        self.relate('connect','dollar','stem-top');self.relate('connect','dollar','stem-bottom')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start;members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='B':self.add_bezier(eid,at,(*args,end))
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,q=4):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
