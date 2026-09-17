"""Three Chive Stalks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e71d276-ac6b-4afe-b7ce-e33fe8be5089'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chive_8e71d276-ac6b-4afe-b7ce-e33fe8be5089.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-chive-stalk'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('three', 'chive', 'stalk')

    def build(self):
        # Plan: Three chive stalks with small oval buds, the middle bud highest. Mirrored side stems curve gently outward. Bud tips simplified into open ovals at native size; Lucide wheat informs the sparse upright structure.
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

        for name,cx,cy,rx,ry in [('left',11,25,3,5),('center',24,9,4,5),('right',37,25,3,5)]:
         path(name+'-bud',(cx,cy+ry),[('A',(cx,cy-ry),rx,ry,True),('A',(cx,cy+ry),rx,ry,True)],True)
        line('center-stem',(24,14),(24,44));join('center-stem','center-bud')
        path('left-stem',(11,30),[('C',(14,44),(14,34),(14,39))]);join('left-stem','left-bud')
        path('right-stem',(37,30),[('C',(34,44),(34,34),(34,39))]);join('right-stem','right-bud')
