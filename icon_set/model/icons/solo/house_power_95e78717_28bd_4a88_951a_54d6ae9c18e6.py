"""Mirrored house outline enclosing an open curved power ring and separate vertical switch stroke."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='95e78717-28bd-4a88-951a-54d6ae9c18e6'
SOURCE_PATH='pictographic-primitives/other/house power_95e78717-28bd-4a88-951a-54d6ae9c18e6.svg'
AUTHOR='gpt-6'
PLAN='An open continuous curved ring replaces the squared-off U ends; the centered stem and rounded lower house corners have clear spacing. The ring is slightly flattened to fit below the roof.'
CONSTRUCTION_REFERENCE='house and power originals; power atomic-debug informs a continuous open ring.'
OMISSIONS='No defining features omitted.'
class Drawing(Solo48):
    icon_id='house-power'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('house', 'power')
    category='objects/general'

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
        self.path('house',(6,18),[('L',(24,6)),('L',(42,18)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,18))],True)
        self.add_arc('power-ring',(16,23),(32,23),radius_x=9,radius_y=6,large_arc=True,sweep=False)
        self.add_line('power-stem',(24,16),(24,20))
