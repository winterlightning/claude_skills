"""A beetle with rounded divided wing covers, separate domed head, two antennae and three leg pairs. Bounds (6,6)-(42,42). Shared bilateral parameters preserve symmetry.
Construction reference: Lucide bug: domed head, divided rounded body and mirrored limbs.
Omissions: Tiny leg bends simplified."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2c75d81b-ef5b-4152-b873-e02ec0753a82'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/bugs_2c75d81b-ef5b-4152-b873-e02ec0753a82.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='beetle-with-divided-wing-covers'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/misc"
    aliases=()
    keywords=('bugs',)
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
        path('body',(14,22),[('C',(16,18),(14,20),(15,19)),('C',(24,16),(18,16),(21,16)),('C',(32,18),(27,16),(30,16)),('C',(34,22),(33,19),(34,20)),('L',(34,32)),('A',(30,40),10,10,True),('A',(24,42),10,10,True),('A',(18,40),10,10,True),('A',(14,32),10,10,True),('L',(14,22))],True)
        path('head',(16,18),[('L',(16,14)),('C',(20,8),(16,11),(18,9)),('C',(24,6),(21,7),(22,6)),('C',(28,8),(26,6),(27,7)),('C',(32,14),(30,9),(32,11)),('L',(32,18))]);join('head','body')
        line('wing-seam',(24,16),(24,42));join('wing-seam','body')
        for side in (-1,1):
         def p(x,y):return (x if side==-1 else 48-x,y)
         path('antenna-'+str(side),p(20,8),[('C',p(14,6),p(18,6),p(16,6))]);join('antenna-'+str(side),'head')
         for j,points in enumerate([[(14,22),(10,22),(6,18)],[(14,30),(8,30),(6,32)],[(18,40),(10,38),(8,42)]]):
          name=f'leg-{side}-{j}';poly(name,*[p(*v) for v in points]);join(name,'body')
