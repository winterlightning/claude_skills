"""Simple Raw Potato Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80c1ab1c-29cc-52bc-b57d-32dddb19091b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/potato_80c1ab1c-29cc-52bc-b57d-32dddb19091b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-raw-potato'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('simple', 'raw', 'potato')

    def build(self):
        # Plan: Irregular potato with a gently indented shoulder and three scattered eyes. Smooth lobed contour and open interior; short source curves reduced to dots. No useful exact Lucide match.
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

        path('potato',(27,4),[('C',(40,19),(36,4),(40,10)),('C',(22,44),(40,35),(33,44)),('C',(8,30),(12,44),(8,39)),('C',(17,16),(8,23),(13,21)),('C',(27,4),(21,11),(20,4))],True)
        for n,p in enumerate(((29,15),(20,26),(27,32))):self.add_dot('eye-'+str(n),p)
