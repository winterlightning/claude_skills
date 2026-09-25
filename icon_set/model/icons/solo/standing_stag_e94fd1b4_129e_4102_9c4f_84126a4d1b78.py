"""Standing stag with smooth haunch and neck transition, curved antlers and long legs, following the complete side-facing reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e94fd1b4-129e-4102-9c4f-84126a4d1b78'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-stag/20260924T105724Z-thuan-mac/reference/deer body_e94fd1b4-129e-4102-9c4f-84126a4d1b78.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-stag-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('standing', 'stag')

    def build(self):
        # Plan: Standing stag with smooth haunch and neck transition, curved antlers and long legs, following the complete side-facing reference.
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
        path('body',(6,42),[('L',(6,32)),('A',(14,24),8,8,True),('L',(26,24)),('A',(32,18),6,6,False),('L',(32,16)),('L',(36,16)),('L',(42,20)),('A',(38,24),4,4,True),('L',(36,24)),('L',(36,34)),('L',(36,42))])
        line('belly',(6,34),(36,34));join('body','belly')
        path('tail',(14,24),[('A',(6,16),8,8,True)]);join('tail','body')
        path('antlers',(24,6),[('A',(32,14),8,8,False),('A',(40,6),8,8,False)])
        line('antler-stem',(32,14),(32,16));join('antler-stem','antlers');join('antler-stem','body')
