"""Tropical Pineapple Fruit."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '575218d7-af4a-47a7-9b63-fa8d41a637dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pineapple_575218d7-af4a-47a7-9b63-fa8d41a637dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tropical-pineapple-fruit'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('tropical', 'pineapple', 'fruit')

    def build(self):
        # Plan: Pineapple with a broad oval body and three pointed crown leaves. Mirrored body and crown with shared attachment nodes. Smooth fruit body follows the source; no crosshatching added. No useful exact Lucide match.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

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

        path('fruit',(14,22),[('C',(24,20),(16,20),(20,20)),('C',(34,22),(28,20),(32,20)),('C',(40,31),(38,22),(40,26)),('C',(24,44),(40,42),(33,44)),('C',(8,31),(15,44),(8,42)),('C',(14,22),(8,26),(10,22))],True)
        poly('crown',(14,22),(10,10),(19,14),(24,4),(29,14),(38,10),(34,22));join('crown','fruit')
