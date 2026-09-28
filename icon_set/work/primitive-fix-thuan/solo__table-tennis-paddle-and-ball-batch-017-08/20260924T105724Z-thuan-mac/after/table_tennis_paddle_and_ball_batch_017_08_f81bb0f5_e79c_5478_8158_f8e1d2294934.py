"""Paddle and ball: replace the angular triangular handle with a continuous rounded paddle shoulder and diagonal rounded grip. Lucide drumstick informs smooth head-to-handle contour transitions; face seam omitted for clarity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f81bb0f5-e79c-5478-8158-f8e1d2294934'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__table-tennis-paddle-and-ball-batch-017-08/20260924T105724Z-thuan-mac/reference/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'table-tennis-paddle-and-ball-batch-017-08'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('table', 'tennis', 'paddle', 'and', 'ball', 'batch', '017', '08')

    def build(self):
        # Plan: Paddle and ball: replace the angular triangular handle with a continuous rounded paddle shoulder and diagonal rounded grip. Lucide drumstick informs smooth head-to-handle contour transitions; face seam omitted for clarity.
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
        path('paddle',(10,18),[('A',(23,6),13,12,True),('A',(36,18),13,12,True),('A',(23,30),13,12,True),('C',(18,32),(21,30),(20,30)),('L',(12,42)),('C',(6,38),(9,42),(6,41)),('L',(6,34)),('L',(12,28)),('C',(10,18),(12,24),(10,23))],True)
        circle('ball',38,38,4)
