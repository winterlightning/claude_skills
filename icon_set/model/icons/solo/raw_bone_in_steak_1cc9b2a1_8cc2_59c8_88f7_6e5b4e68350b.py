"""Raw Bone-in Steak."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cc9b2a1-8cc2-59c8-88f7-6e5b4e68350b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barbecue steak_1cc9b2a1-8cc2-59c8-88f7-6e5b4e68350b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raw-bone-in-steak'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('raw', 'bone', 'in', 'steak')

    def build(self):
        # Plan: Supplied steak: asymmetric kidney-shaped meat outline and off-center circular bone. Thickness contour omitted to remove internal crowding; oval bone simplified to a circle. No useful exact Lucide match.
        # Envelope: HRECT_L; visible ink (2, 6, 46, 42) on SOLO48.

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

        path('top',(4,30),[('C',(26,8),(4,17),(14,8)),('C',(44,24),(38,8),(44,14)),('C',(34,40),(44,34),(40,40)),('C',(22,34),(28,40),(26,34)),('C',(12,40),(18,34),(18,40)),('C',(4,30),(6,40),(4,36))],True)
        oval('bone',29,22,4,4)
