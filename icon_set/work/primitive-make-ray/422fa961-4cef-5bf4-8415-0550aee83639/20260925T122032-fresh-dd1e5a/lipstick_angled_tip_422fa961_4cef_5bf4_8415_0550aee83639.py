"""Upright lipstick with a straight angled cut, narrow stepped collar and tall rounded case."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='422fa961-4cef-5bf4-8415-0550aee83639'
SOURCE_PATH='pictographic-primitives/beauty/make up lipstick_422fa961-4cef-5bf4-8415-0550aee83639.svg'
AUTHOR='gpt-6'
PLAN='Upright lipstick with a straight angled cut, narrow stepped collar and tall rounded case.'
CONSTRUCTION_REFERENCE='No local Lucide lipstick match; supplied reference governs the angled tip and stepped case.'
OMISSIONS='No defining features omitted.'
class Drawing(Solo48):
    icon_id='lipstick-angled-tip'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('make', 'up', 'lipstick')

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
        self.box('case',10,26,38,44,4)
        self.add_polyline('collar',(14,26),(14,18),(16,18),(32,18),(34,18),(34,26));self.relate('connect','collar','case')
        self.path('lipstick',(16,18),[('L',(16,12)),('C',(20,8),(16,10),(18,9)),('L',(32,4)),('L',(32,18))]);self.relate('connect','lipstick','collar')

# Keyshape rationale: VRECT_M supports the upright case, collar and angled tip.
# Visual review: Straight angled tip and both case steps restored; intentional asymmetric tip.
