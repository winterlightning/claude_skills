"""Traditional Mooncake Pastry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef696155-2215-5e20-a509-364d7cf8de72'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mooncake top_ef696155-2215-5e20-a509-364d7cf8de72.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'traditional-mooncake-pastry'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('traditional', 'mooncake', 'pastry')

    def build(self):
        # Plan: Top-view mooncake with scalloped crust and a bold curled groove. The inner ring and small petal series are reduced to one open spiral to preserve the embossed decoration at 48 pixels. The repeated crust has rotational balance; no useful exact Lucide match.
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

        commands=[]
        def turn(p,n):
            x,y=p
            for _ in range(n):x,y=48-y,x
            return x,y
        quarter=[((32,8),(30,6),(29,8)),((38,10),(34,6),(36,6)),((40,16),(42,12),(42,14)),((42,24),(40,19),(42,18))]
        for n in range(4):
            for end,c1,c2 in quarter:commands.append(('C',turn(end,n),turn(c1,n),turn(c2,n)))
        path('crust',(24,6),commands,True)

        path('scroll',(15,24),[('A',(24,15),9,9,True),('A',(33,24),9,9,True),('A',(24,33),9,9,True),('L',(24,24))])
