"""A robot spider with circular upper body, open lower body, and three angular leg pairs from the source. Bounds (6,6)-(42,42). Mirrored six-leg series preserves source topology.
Construction reference: Lucide bug: mirrored leg construction; reference two-body arrangement restored.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0b45fbf3-0b8c-5fad-b623-5d57b7e45c82'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spider-with-round-body/20260924T100518Z-thuan-mac/reference/robot spider_0b45fbf3-0b8c-5fad-b623-5d57b7e45c82.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='spider-with-round-body'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('robot', 'spider')
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
        path('upper',(18,24),[('A',(14,16),10,10,True),('A',(24,6),10,10,True),('A',(34,16),10,10,True),('A',(30,24),10,10,True),('A',(18,24),10,10,True)],True)
        path('lower-left',(18,24),[('C',(14,30),(15,26),(14,28)),('C',(16,36),(14,33),(15,35)),('L',(18,38))]);join('lower-left','upper')
        path('lower-right',(30,24),[('C',(34,30),(33,26),(34,28)),('C',(32,36),(34,33),(33,35)),('L',(30,38))]);join('lower-right','upper')
        for side in (-1,1):
         def p(x,y):return (x if side==-1 else 48-x,y)
         for j,points in enumerate([[(18,24),(10,18),(6,24)],[(14,30),(8,30),(6,38)],[(16,36),(14,38),(14,42)]]):
          name=f'leg-{side}-{j}';poly(name,*[p(*v) for v in points]);join(name,'upper' if j==0 else ('lower-left' if side==-1 else 'lower-right'))
