"""Clockwise circular return arrow with upward head at lower-left. Three tangent cardinal quarter arcs make a smooth shaft; bounds4,8 to44,40.
Construction reference: Lucide rotate-ccw: smooth circular shaft and open head, reversed direction.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'edd1a1a5-5b11-4ec8-9855-ec307205ccb2'
SOURCE_PATH = 'pictographic-primitives/arrows/dash circle large head_edd1a1a5-5b11-4ec8-9855-ec307205ccb2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'dash-circle-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('dash', 'circle', 'large', 'head')
    def build(self):
        self.path('shaft',(12,16),[('C',(28,8),(15,10),(21,8)),('A',(44,24),16,16,True),('A',(28,40),16,16,True),('A',(12,24),16,16,True)])
        self.add_polyline('head',(4,32),(12,24),(20,32));self.relate('connect','head','shaft')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
