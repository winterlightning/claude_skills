'oval-light-bulb: Use an elongated glass bulb that narrows naturally into a distinct screw base and rounded contact. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a686616-2bfa-4c53-a2f5-9bfd97179c20'
SOURCE_PATH = 'pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg'
AUTHOR = 'gpt-6'


class OvalLightBulb(Solo48):
    icon_id = 'oval-light-bulb'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "other", "primitives-generate")
    aliases = ()
    keywords = ('bulb', 'light', 'lamp', 'idea', 'illumination', 'electricity')

    def build(self):
        # Symbol plan: Use an elongated glass bulb that narrows naturally into a distinct screw base and rounded contact.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('glass',(18,34),[('C',(10,18),(18,29),(10,28)),('A',(38,18),14,14,True),('C',(30,34),(38,28),(30,29)),('L',(18,34))],True)
        path('base',(18,34),[('L',(18,38)),('A',(24,44),6,6,False),('A',(30,38),6,6,False),('L',(30,34))]);join('glass','base')
