from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='07459f9b-1db4-4f1f-aeee-4e5113b2f2f4'
SOURCE_PATH='pictographic-primitives/other/briefcase dollar_07459f9b-1db4-4f1f-aeee-4e5113b2f2f4.svg'
AUTHOR='gpt-6'
PLAN='Case with handle, geometric S dollar with separated top and bottom stems. Lucide dollar-sign informs currency terminals; diagonal waist opens compact lobes. Taller envelope gives room to handle and mark.'
class Drawing(Solo48):
    icon_id='briefcase-dollar'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('briefcase', 'dollar')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.path('case',(12,12),[('L',(16,12)),('L',(32,12)),('L',(36,12)),('A',(40,16),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,16)),('A',(12,12),4,4,True)],True)
        self.add_polyline('handle',(16,12),(16,4),(32,4),(32,12));self.relate('connect','handle','case')
        self.path('dollar',(28,22),[('L',(24,22)),('L',(22,22)),('A',(20,24),2,2,False),('L',(28,32)),('A',(26,34),2,2,True),('L',(24,34)),('L',(20,34))])
        self.add_line('stem-top',(24,21),(24,22));self.add_line('stem-bottom',(24,34),(24,35))
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
