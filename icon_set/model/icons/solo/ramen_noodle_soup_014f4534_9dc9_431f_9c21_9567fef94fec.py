"""Ramen Noodle Soup Bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '014f4534-9dc9-431f-9c21-9567fef94fec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/noodle ramen bowl_014f4534-9dc9-431f-9c21-9567fef94fec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ramen-noodle-soup'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('ramen', 'noodle', 'soup')

    def build(self):
        # Plan: Lucide soup: rounded bowl. One arched noodle mound and a loose upturned strand; nested noodle line omitted.
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

        path('bowl',(4,24),[('L',(10,24)),('L',(30,24)),('L',(44,24)),('C',(24,40),(44,33),(35,40)),('C',(4,24),(13,40),(4,33))],True)
        path('noodles',(10,24),[('A',(30,24),10,10,True)]);join('noodles','bowl')
        path('strand',(30,24),[('C',(36,16),(36,24),(36,20)),('A',(44,8),8,8,True)]);join('strand','bowl');join('strand','noodles')
