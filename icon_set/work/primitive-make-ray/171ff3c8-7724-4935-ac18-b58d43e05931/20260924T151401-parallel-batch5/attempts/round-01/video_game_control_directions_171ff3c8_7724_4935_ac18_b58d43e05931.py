"""Video game control directions.
Symbol plan: A at left, B above right and directional cross below right; shared B pitch8. Bounds4,8..44,40.
Omissions: Button rings and D-pad outline/center circle omitted; letter identities and relative grouping retained.
Construction references: Lucide gamepad-2: simple plus control; supplied reference for A/B arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='171ff3c8-7724-4935-ac18-b58d43e05931'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/video game control directions_171ff3c8-7724-4935-ac18-b58d43e05931.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='video-game-control-directions'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('video', 'game', 'control', 'directions')

    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            kind,end,*args=op
            if at==end: continue
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,at,end)
            elif kind=='A': self.add_arc(m,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            else: self.add_bezier(m,at,(args[0],args[1],end))
            members.append(m);at=end
        if closed and at!=start:
            self.add_line(n+'-close',at,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        ops=[('L',(x,t)) for x in sorted(top) if l+k<x<r-k]
        ops += [('L',(r-k,t)),('A',(r,t+k),k,k,True)]
        ops += [('L',(r,y)) for y in sorted(right) if t+k<y<b-k]
        ops += [('L',(r,b-k)),('A',(r-k,b),k,k,True)]
        ops += [('L',(x,b)) for x in sorted(bottom,reverse=True) if l+k<x<r-k]
        ops += [('L',(l+k,b)),('A',(l,b-k),k,k,True)]
        ops += [('L',(l,y)) for y in sorted(left,reverse=True) if t+k<y<b-k]
        ops += [('L',(l,t+k)),('A',(l+k,t),k,k,True)]
        self.path(n,(l+k,t),ops,True)

    def build(self):
        # Rounded A owns an ample counter and shared bar junctions.
        self.path('a-sides',(4,40),[('L',(4,32)),('L',(4,22)),('A',(16,22),6,6,True),('L',(16,32)),('L',(16,40))])
        self.add_line('a-bar',(4,32),(16,32));self.relate('connect','a-sides','a-bar')
        # Equal B bowls: an8-unit pitch and a shared middle rail.
        self.add_polyline('b-stem',(28,8),(28,16),(28,24))
        self.path('b-upper',(28,8),[('L',(34,8)),('A',(34,16),4,4,True),('L',(28,16))])
        self.path('b-lower',(28,16),[('L',(34,16)),('A',(34,24),4,4,True),('L',(28,24))])
        self.relate('connect','b-stem','b-upper');self.relate('connect','b-stem','b-lower');self.relate('connect','b-upper','b-lower')
        self.add_polyline('pad-horizontal',(28,36),(36,36),(44,36))
        self.add_polyline('pad-vertical',(36,32),(36,36),(36,40));self.relate('connect','pad-horizontal','pad-vertical')
