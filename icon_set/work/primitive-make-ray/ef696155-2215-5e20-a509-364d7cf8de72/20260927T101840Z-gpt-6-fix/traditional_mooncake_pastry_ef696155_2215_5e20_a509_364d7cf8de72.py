"""Traditional Mooncake Pastry."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ef696155-2215-5e20-a509-364d7cf8de72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__traditional-mooncake-pastry/20260927T101610Z-thuan-mac-1/reference/mooncake top_ef696155-2215-5e20-a509-364d7cf8de72.svg'
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

        # The source shows radial pastry embossing, not a single curled numeral.
        path('petal-rosette',(24,16),[
            ('C',(29,19),(28,16),(31,17)),
            ('C',(32,24),(32,21),(32,22)),
            ('C',(29,29),(32,28),(31,31)),
            ('C',(24,32),(27,32),(26,32)),
            ('C',(19,29),(20,32),(17,31)),
            ('C',(16,24),(16,27),(16,26)),
            ('C',(19,19),(16,20),(17,17)),
            ('C',(24,16),(21,16),(22,16)),
        ],True)
