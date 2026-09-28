"""Sitting squirrel with smoothly curled bushy tail, upright ear, projecting muzzle and rounded haunch; Lucide squirrel informs connected organic contour flow."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4582abe5-3297-4fa0-961e-cfe5747d887e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__squirrel/20260924T105724Z-thuan-mac/reference/squirrel_4582abe5-3297-4fa0-961e-cfe5747d887e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'squirrel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('squirrel',)

    def build(self):
        # Plan: Sitting squirrel with smoothly curled bushy tail, upright ear, projecting muzzle and rounded haunch; Lucide squirrel informs connected organic contour flow.
        def path(n, start, steps, closed=False):
            p=start; ids=[]
            for i,s in enumerate(steps):
                name=f'{n}-{i}'; kind,end,*args=s
                if kind=='L': self.add_line(name,p,end)
                elif kind=='A': self.add_arc(name,p,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(name,p,(args[0],args[1],end))
                ids.append(name); p=end
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path('tail',(6,16),[('C',(14,6),(6,9),(8,6)),('C',(22,16),(21,6),(22,10)),('C',(18,28),(22,21),(20,24)),('C',(24,42),(15,33),(19,39))])
        path('back',(6,16),[('C',(9,26),(6,20),(9,22)),('C',(6,34),(9,30),(6,30)),('C',(16,42),(6,40),(10,42)),('L',(24,42))]);join('tail','back')
        path('neck',(18,28),[('C',(28,18),(22,24),(28,24)),('L',(28,10)),('A',(36,10),4,4,True),('C',(42,14),(40,10),(42,10)),('C',(34,24),(42,20),(39,24)),('L',(34,28))]);join('tail','neck')
        path('haunch',(34,28),[('C',(42,35),(39,28),(42,31)),('C',(36,42),(42,40),(40,42)),('L',(24,42))]);join('haunch','tail');join('haunch','back');join('haunch','neck')
