"""A hanging spider with rounded abdomen, smaller overlapping head and the three curved leg pairs shown in its reference. Bounds (6,6)-(42,42). Mirrored legs share parameters and exact body nodes.
Construction reference: Lucide bug: mirrored appendages; original has three visible leg pairs.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='380869ce-057f-4cbf-be51-92de0ec1f4e3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spider-on-thread/20260924T100518Z-thuan-mac/reference/spider_380869ce-057f-4cbf-be51-92de0ec1f4e3.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='spider-on-thread'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('spider',)
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
        path('body',(20,34),[('C',(14,24),(16,32),(14,28)),('A',(16,18),10,10,True),('A',(24,14),10,10,True),('A',(32,18),10,10,True),('A',(34,24),10,10,True),('C',(28,34),(34,28),(32,32))])
        path('head',(20,34),[('A',(24,32),5,5,True),('A',(28,34),5,5,True),('A',(29,37),5,5,True),('A',(24,42),5,5,True),('A',(19,37),5,5,True),('A',(20,34),5,5,True)],True);join('head','body')
        line('thread',(24,6),(24,14));join('thread','body')
        for side in (-1,1):
         def p(x,y):return (x if side==-1 else 48-x,y)
         for j,(start,c1,c2,end) in enumerate([((16,18),(12,14),(9,15),(6,18)),((14,24),(10,23),(8,26),(6,29)),((20,34),(14,32),(11,37),(10,42))]):
          name=f'leg-{side}-{j}'
          path(name,p(*start),[('C',p(*end),p(*c1),p(*c2))]);join(name,'body')
