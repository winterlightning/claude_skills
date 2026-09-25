"""Rounded rain cloud with a prominent central dome and three equally spaced slanted drops."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='1b0e7b77-0101-4ff8-b82d-4b17ff5d13e2'
SOURCE_PATH='pictographic-primitives/_uncategorized_11/cloud rain_1b0e7b77-0101-4ff8-b82d-4b17ff5d13e2.svg'
AUTHOR='gpt-6'
PLAN='Rounded rain cloud with a prominent central dome and three equally spaced slanted drops.'
CONSTRUCTION_REFERENCE='cloud-rain original and atomic-debug: dominant cloud lobe and regular rain series.'
OMISSIONS='No omissions.'
class Drawing(Solo48):
    icon_id='cloud-with-rain'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('cloud', 'rain')

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
        self.path('cloud',(14,28),[('C',(6,22),(8,28),(6,26)),('C',(14,16),(6,17),(10,14)),('A',(34,16),10,10,True),('C',(42,22),(38,14),(42,17)),('C',(34,28),(42,26),(40,28)),('L',(14,28))],True)
        for i,x in enumerate((16,27,38)):self.add_line(f'rain-{i}',(x,37),(x-3,42))

# Keyshape rationale: SQUARE balances a tall cloud dome above three rain strokes.
# Visual review: Taller central dome with three equally spaced slanted drops.
