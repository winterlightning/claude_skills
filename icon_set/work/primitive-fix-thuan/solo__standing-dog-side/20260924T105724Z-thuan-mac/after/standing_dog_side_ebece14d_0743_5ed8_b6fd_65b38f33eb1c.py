"""Standing dog with low rounded skull and projecting muzzle, coherent rounded leg/body contour, and raised curved tail. Lucide dog informs rounded head construction; side pose preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ebece14d-0743-5ed8-b6fd-65b38f33eb1c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-dog-side/20260924T105724Z-thuan-mac/reference/dog_ebece14d-0743-5ed8-b6fd-65b38f33eb1c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-dog-side'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('standing', 'dog', 'side')

    def build(self):
        # Plan: Standing dog with low rounded skull and projecting muzzle, coherent rounded leg/body contour, and raised curved tail. Lucide dog informs rounded head construction; side pose preserved.
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
        path('body',(12,20),[('L',(26,20)),('A',(30,16),4,4,False),('L',(30,12)),('A',(34,8),4,4,True),('L',(36,8)),('A',(40,12),4,4,True),('L',(44,14)),('L',(44,20)),('L',(36,24)),('L',(36,38)),('A',(34,40),2,2,True),('L',(30,40)),('A',(28,38),2,2,True),('L',(28,30)),('L',(20,30)),('L',(20,38)),('A',(18,40),2,2,True),('L',(14,40)),('A',(12,38),2,2,True),('L',(12,28)),('L',(12,20))],True)
        path('tail',(12,20),[('A',(4,12),8,8,True),('L',(4,8))]);join('tail','body')
