"""Deer has a rounded horizontal body, longer visible legs, smooth upright neck, projecting muzzle and curved antlers. Related Lucide animal outlines informed coherent curves."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a6ff6a0a-a017-4795-b53f-e68479e6966b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-deer/20260924T105724Z-thuan-mac/reference/deer body_a6ff6a0a-a017-4795-b53f-e68479e6966b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-deer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('standing', 'deer')

    def build(self):
        # Plan: Deer has a rounded horizontal body, longer visible legs, smooth upright neck, projecting muzzle and curved antlers. Related Lucide animal outlines informed coherent curves.
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
        path('body',(14,24),[('L',(26,24)),('A',(32,18),6,6,False),('L',(32,14)),('L',(36,14)),('L',(42,20)),('A',(38,24),4,4,True),('L',(38,26)),('A',(30,34),8,8,True),('L',(14,34)),('A',(14,24),8,5,True)],True)
        for name,x in [('rear',14),('front',30)]:
            line(name+'-leg',(x,34),(x,42));join('body',name+'-leg')
        path('antlers',(24,6),[('A',(32,14),8,8,False),('A',(40,6),8,8,False)]);join('antlers','body')
