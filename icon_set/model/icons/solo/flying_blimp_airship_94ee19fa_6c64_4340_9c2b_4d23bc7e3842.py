"""A long rounded balloon envelope, rear triangular tail fins and an attached hanging gondola."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='94ee19fa-6c64-4340-9c2b-4d23bc7e3842'
SOURCE_PATH='pictographic-primitives/_uncategorized_01/airship_94ee19fa-6c64-4340-9c2b-4d23bc7e3842.svg'
AUTHOR='gpt-6'
PLAN='Restored a rounded balloon envelope with a pointed rear, two distinct triangular fins and an attached gondola below the forward half. The fins are no longer fused into a rocket-like silhouette.'
CONSTRUCTION_REFERENCE='No useful local Lucide airship match; supplied reference owns pointed tail and rounded balloon proportions.'
OMISSIONS='No defining parts omitted. Gondola moved forward slightly to clear the lower tail fin. Directional asymmetry is intentional.'
class Drawing(Solo48):
    icon_id='flying-blimp-airship'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('airship',)
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')

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
        self.path('envelope',(8,22),[('C',(16,14),(10,20),(12,16)),('C',(24,12),(18,13),(20,12)),('A',(44,22),20,10,True),('A',(36,30),20,10,True),('A',(24,32),20,10,True),('C',(16,30),(20,32),(18,31)),('C',(8,22),(12,28),(10,24))],True)
        self.add_polyline('upper-fin',(16,14),(4,8),(8,22));self.relate('connect','upper-fin','envelope')
        self.add_polyline('lower-fin',(8,22),(4,36),(16,30));self.relate('connect','lower-fin','envelope')
        self.path('gondola',(24,32),[('L',(26,40)),('L',(34,40)),('L',(36,30))]);self.relate('connect','gondola','envelope')
