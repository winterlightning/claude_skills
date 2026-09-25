"""Balanced justice scale with two enlarged deep bowls and matching triangular suspensions."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='098c5b62-8287-467b-95c6-c1b202763219'
SOURCE_PATH='pictographic-primitives/business/scale_098c5b62-8287-467b-95c6-c1b202763219.svg'
AUTHOR='gpt-6'
PLAN='Balanced justice scale with two enlarged deep bowls and matching triangular suspensions.'
CONSTRUCTION_REFERENCE='scale original and atomic-debug: matched suspended bowls and shared post.'
OMISSIONS='No omissions. Pan width increases from 10 to 12 and depth from 6 to 8 centerline units.'
class Drawing(Solo48):
    icon_id='balanced-scales-large-pans'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('scale',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.add_polyline('post',(24,8),(24,12),(24,40))
        self.add_polyline('beam',(10,12),(24,12),(38,12));self.relate('connect','post','beam')
        self.add_polyline('base',(16,40),(24,40),(32,40));self.relate('connect','post','base')
        for i,cx in enumerate((10,38)):
            n=f'pan-{i}'
            self.add_polyline(n+'-suspension',(cx-6,26),(cx,12),(cx+6,26))
            self.path(n+'-bowl',(cx+6,26),[('A',(cx-6,26),6,8,True),('L',(cx+6,26))],True)
            self.relate('connect',n+'-suspension','beam');self.relate('connect',n+'-suspension',n+'-bowl')

# Keyshape rationale: HRECT_L gives matching enlarged pans room on either side of the post.
# Visual review: Matched bowls are 20% wider and 33% deeper than the previous drawing.
