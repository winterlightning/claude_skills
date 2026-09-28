"""A domed vehicle headlight with three diagonal beams. HRECT_L bounds (4,8)-(44,40); repeated beams share step12.
Construction reference: Lucide headset: smooth rounded outer housing; source owns lamp shape.
Omissions: Short partial fourth beam omitted to avoid a crowded junction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '60239e6a-5e58-4c70-a436-9fa4c1208587'
SOURCE_PATH = 'pictographic-primitives/transportation/adaptive light 1_60239e6a-5e58-4c70-a436-9fa4c1208587.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='adaptive-headlight'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases=()
    keywords=('adaptive', 'light', '1')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('lamp',(26,8),[('C',(44,24),(36,8),(44,15)),('C',(26,40),(44,33),(36,40)),('C',(26,8),(24,32),(24,16))],True)
        for i in range(3):line(f'beam-{i}',(4,14+12*i),(16,8+12*i))
