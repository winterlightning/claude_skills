"""Round mining helmet with a raised tapering central ridge and broad shallow curved brim."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='cefdcc61-2ed2-5460-9530-e110178b2c81'
SOURCE_PATH='pictographic-primitives/construction/safety helmet mine_cefdcc61-2ed2-5460-9530-e110178b2c81.svg'
AUTHOR='gpt-6'
PLAN='Round mining helmet with a raised tapering central ridge and broad shallow curved brim.'
CONSTRUCTION_REFERENCE='hard-hat original and atomic-debug: raised ridge separated from dome shoulders.'
OMISSIONS='No defining features omitted.'
class Drawing(Solo48):
    icon_id='mine-safety-helmet'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('safety', 'helmet', 'mine')

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
        self.path('ridge',(18,20),[('L',(16,14)),('L',(16,11)),('A',(19,8),3,3,True),('L',(29,8)),('A',(32,11),3,3,True),('L',(32,14)),('L',(30,20))])
        self.path('dome-l',(8,28),[('C',(16,14),(8,23),(10,17))]);self.path('dome-r',(32,14),[('C',(40,28),(38,17),(40,23))])
        self.path('brim',(4,28),[('L',(8,28)),('L',(40,28)),('L',(44,28)),('A',(4,28),20,12,True)],True)
        for a,b in [('ridge','dome-l'),('ridge','dome-r'),('dome-l','brim'),('dome-r','brim')]:self.relate('connect',a,b)

# Keyshape rationale: HRECT_L balances the tapered ridge and curved brim.
# Visual review: Tapered central ridge restored above the shell; curved brim deepened for clearance.
