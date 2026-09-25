"""Stack of Spring Rolls."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2b68499-c753-44d3-a700-fb019d713669'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/exotic food rolls_b2b68499-c753-44d3-a700-fb019d713669.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spring-roll-stack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('spring', 'roll', 'stack')

    def build(self):
        # Plan: Two cylindrical spring rolls with exposed round ends, stacked vertically with a slight horizontal offset. Shared curved end-ring construction; source pile and plate reduced to two separated rolls to preserve clear end faces. No useful exact Lucide match.
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

        path('lower',(15,30),[('L',(33,30)),('A',(40,37),7,7,True),('A',(33,44),7,7,True),('L',(15,44)),('A',(15,30),7,7,True)],True)
        path('end-lower',(33,30),[('A',(33,44),7,7,False)]);join('end-lower','lower')
        path('upper',(19,4),[('L',(33,4)),('A',(40,11),7,7,True),('A',(33,18),7,7,True),('L',(19,18)),('A',(19,4),7,7,True)],True)
        path('end-upper',(33,4),[('A',(33,18),7,7,False)]);join('end-upper','upper')
