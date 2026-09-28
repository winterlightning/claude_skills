"""Satellite dish with a single smooth parabolic bowl, angled receiver, rounded pedestal and separated signal arc. Lucide satellite-dish informs the diagonal feed and coherent bowl."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6c185482-97c6-496c-a205-3d684b0ecf72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__transmitting-satellite-dish/20260924T105724Z-thuan-mac/reference/antenna_6c185482-97c6-496c-a205-3d684b0ecf72.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'transmitting-satellite-dish'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('transmitting', 'satellite', 'dish')

    def build(self):
        # Plan: Satellite dish with a single smooth parabolic bowl, angled receiver, rounded pedestal and separated signal arc. Lucide satellite-dish informs the diagonal feed and coherent bowl.
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
        path('dish',(8,16),[('C',(4,24),(5,18),(4,21)),('A',(12,32),8,8,False),('C',(24,32),(16,34),(21,34)),('L',(16,24)),('L',(8,16))],True)
        poly('stand',(12,32),(8,40),(26,40),(24,32));join('stand','dish')
        line('feed',(16,24),(24,19));circle('receiver',26,19,2);join('dish','feed')
        # Receiver link reaches its left cardinal point exactly.
        join('feed','receiver')
        path('signal',(26,8),[('A',(44,26),18,18,True)])
