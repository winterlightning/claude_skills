"""A beetle with rounded divided wing covers, separate domed head, two antennae and three leg pairs. Bounds (6,6)-(42,42). Shared bilateral parameters preserve symmetry.
Construction reference: Lucide bug: domed head, divided rounded body and mirrored limbs.
Omissions: Tiny leg bends simplified."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2c75d81b-ef5b-4152-b873-e02ec0753a82'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__beetle-with-divided-wing-covers/20260924T101756Z-thuan-mac/reference/bugs_2c75d81b-ef5b-4152-b873-e02ec0753a82.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='beetle-with-divided-wing-covers'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
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
        path('body',(14,22),[('A',(24,16),10,6,True),('A',(34,22),10,6,True),('L',(34,32)),('A',(24,42),10,10,True),('A',(14,32),10,10,True),('L',(14,22))],True)
        path('head',(17,18),[('L',(17,15)),('A',(31,15),7,7,True),('L',(31,18))]);join('head','body')
        line('wing-seam',(24,16),(24,42));join('wing-seam','body')
        for side in (-1,1):
         def p(x,y):return (x if side==-1 else 48-x,y)
         path('antenna-'+str(side),p(19,10),[('C',p(14,6),p(18,8),p(16,6))]);join('antenna-'+str(side),'head')
         for j,points in enumerate([[(14,22),(10,22),(6,18)],[(14,30),(8,30),(6,32)],[(18,40),(10,38),(8,42)]]):
          name=f'leg-{side}-{j}';poly(name,*[p(*v) for v in points]);join(name,'body')
