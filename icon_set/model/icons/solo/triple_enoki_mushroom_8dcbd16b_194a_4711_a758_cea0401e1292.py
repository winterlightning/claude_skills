"""Triple Enoki Mushroom."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dcbd16b-194a-4711-a758-cea0401e1292'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom enoki_8dcbd16b-194a-4711-a758-cea0401e1292.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triple-enoki-mushroom'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('triple', 'enoki', 'mushroom')

    def build(self):
        # Plan: Three enoki mushrooms with round caps and long slender stems meeting near the base. Small circle caps and shared converging stem node. Outlined stems reduced to single strokes; no useful exact Lucide match.
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

        for j,(cx,cy) in enumerate(((11,20),(24,7),(37,20))):
         path('cap-'+str(j),(cx,cy+3),[('A',(cx,cy-3),3,3,True),('A',(cx,cy+3),3,3,True)],True)
        line('stem-center',(24,10),(24,44));join('stem-center','cap-1')
        path('stem-left',(11,23),[('L',(11,29)),('C',(17,37),(11,33),(14,34)),('L',(24,44))]);join('stem-left','cap-0');join('stem-left','stem-center')
        path('stem-right',(37,23),[('L',(37,29)),('C',(31,37),(37,33),(34,34)),('L',(24,44))]);join('stem-right','cap-2');join('stem-right','stem-center')
