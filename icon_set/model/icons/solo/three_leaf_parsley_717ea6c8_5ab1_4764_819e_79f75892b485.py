"""Three Leaf Parsley Herb Sprig."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '717ea6c8-5ab1-4764-819e-79f75892b485'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/parsley_717ea6c8-5ab1-4764-819e-79f75892b485.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-leaf-parsley'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('three', 'leaf', 'parsley')

    def build(self):
        # Plan: Parsley sprig with three broad lobed leaves on one upright stem. Shared axis and mirrored lower leaves; larger vertical separation keeps all three leaf interiors readable. Small serrations and secondary veins omitted; Lucide leaf informs the continuous silhouette.
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

        path('top',(24,20),[('C',(16,12),(18,20),(14,16)),('L',(20,12)),('L',(20,8)),('L',(24,4)),('L',(28,8)),('L',(28,12)),('L',(32,12)),('C',(24,20),(34,16),(30,20))],True)
        poly('stem',(24,44),(24,40),(24,20));join('stem','top')
        path('left',(24,40),[('C',(8,38),(16,44),(8,44)),('L',(12,34)),('L',(8,28)),('C',(20,30),(15,28),(18,27)),('C',(24,40),(24,31),(24,36))],True)
        path('right',(24,40),[('C',(40,38),(32,44),(40,44)),('L',(36,34)),('L',(40,28)),('C',(28,30),(33,28),(30,27)),('C',(24,40),(24,31),(24,36))],True)
        join('left','stem');join('right','stem')
