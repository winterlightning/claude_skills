"""A sprinter calf and shoe pressed against a triangular starting block, with smooth ankle and rounded rear calf. Bounds (4,8)-(44,40). Intentional diagonal leg posture preserved.
Construction reference: Human full_body_ref.png: smooth continuous limb strokes; original owns cropped calf and shoe.
Omissions: Small shoe stripes omitted for spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fd54e74f-7aee-43cc-86b5-fbb93b1d273c'
SOURCE_PATH='pictographic-primitives/sports/running ready starting block_fd54e74f-7aee-43cc-86b5-fbb93b1d273c.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='sprinter-starting-block'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases=()
    keywords=('running', 'ready', 'starting', 'block')
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
        path('leg',(24,8),[('L',(35,15)),('C',(39,24),(40,18),(41,20)),('C',(23,40),(34,32),(28,39)),('L',(15,40)),('C',(10,33),(10,40),(9,37)),('C',(12,22),(11,29),(12,26)),('L',(11,20)),('L',(4,15))])
        poly('block',(23,40),(38,29),(44,40),(23,40),closed=True);join('leg','block')
