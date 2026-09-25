"""fish-bowl: Symmetric glass bowl with a flat rim and waterline; a small smooth fish faces right inside.
Lucide construction: fish; original and atomic-debug inspected.
Omissions: Tiny eye omitted.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a12a46a8-8ec0-50ee-9332-2e08aade7d73'
SOURCE_PATH = 'pictographic-primitives/pets/fish bowl_a12a46a8-8ec0-50ee-9332-2e08aade7d73.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'fish-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('fish', 'bowl')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('bowl',(10,6),[('L',(38,6)),('C',(42,14),(40,8),(42,10)),('L',(42,24)),('A',(24,42),18,18,True),('A',(6,24),18,18,True),('L',(6,14)),('C',(10,6),(6,10),(8,8))],True)
        line('water',(6,14),(42,14));join('water','bowl')
        path('fish',(20,26),[('C',(26,22),(22,23),(24,22)),('C',(32,26),(28,22),(30,23)),('C',(26,30),(30,29),(28,30)),('C',(20,26),(24,30),(22,29))],True)
        poly('tail',(17,22),(20,26),(17,30));join('tail','fish')
