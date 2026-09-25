"""Upright blank door with paired round upper corners and a symmetric ground line."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='f3bcb648-33a4-4112-a9ca-00bcdf092bab'
SOURCE_PATH='pictographic-primitives/building/door left hand closed_f3bcb648-33a4-4112-a9ca-00bcdf092bab.svg'
AUTHOR='gpt-6'
PLAN='Symmetric door sides, equal rounded upper corners and a centered threshold replace the square, slightly uneven old frame.'
CONSTRUCTION_REFERENCE='door-closed original and atomic-debug: rounded upper corners, upright sides and level threshold.'
OMISSIONS='No omissions. No handle added because the reference is blank.'
class Drawing(Solo48):
    icon_id='closed-vertical-door'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('door', 'left', 'hand', 'closed')
    category = 'building'

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
        self.path('door',(10,44),[('L',(10,8)),('A',(14,4),4,4,True),('L',(34,4)),('A',(38,8),4,4,True),('L',(38,44))])
        self.add_polyline('ground',(8,44),(10,44),(38,44),(40,44));self.relate('connect','door','ground')
