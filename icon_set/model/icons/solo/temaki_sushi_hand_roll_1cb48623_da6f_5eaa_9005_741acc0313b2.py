"""Temaki Sushi Hand Roll."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cb48623-da6f-5eaa-9005-741acc0313b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/asian food japanese assorted seafood in seaweed cone_1cb48623-da6f-5eaa-9005-741acc0313b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'temaki-sushi-hand-roll'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('temaki', 'sushi', 'hand', 'roll')

    def build(self):
        # Plan: Temaki sushi with rounded filling portions and overlapping diagonal seaweed edges. Shared seam intersection and rounded cone tip. Filling count reduced to two large lobes; no useful exact Lucide match.
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

        path('fillings',(8,18),[('C',(16,4),(8,8),(10,4)),('C',(24,12),(22,4),(24,6)),('C',(32,4),(24,6),(26,4)),('C',(40,18),(38,4),(40,8))])
        path('wrap',(8,18),[('L',(16,30)),('L',(18,40)),('C',(24,44),(19,44),(22,44)),('C',(30,40),(26,44),(29,44)),('L',(40,18))]);join('wrap','fillings')
        poly('seam',(40,18),(24,26),(16,30));join('seam','wrap')
        line('fold',(8,18),(24,26));join('fold','wrap');join('fold','seam')
