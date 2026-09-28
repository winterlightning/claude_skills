"""Spaghetti on Fork."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21cd9183-a949-443f-9aa0-592ab7600755'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pasta fork_21cd9183-a949-443f-9aa0-592ab7600755.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spaghetti-wrapped-fork'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('spaghetti', 'wrapped', 'fork')

    def build(self):
        # Plan: Horizontal fork with a broad wrapped noodle loop and one hanging strand. Lucide utensils informs the rounded fork and shared tine junctions. Outlined handle and repeated pasta loops reduced to single strokes and one loop. Horizontal orientation retained.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('fork',(42,18),[('L',(18,18)),('A',(13,23),5,5,False),('A',(18,28),5,5,False),('L',(42,28))])
        line('handle',(6,23),(13,23));join('handle','fork')
        path('noodle',(24,28),[('L',(24,11)),('A',(34,11),5,5,True),('L',(34,32)),('C',(24,42),(34,40),(30,42)),('L',(18,42))]);join('noodle','fork')
