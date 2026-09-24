"""Capsule mouse and two curved right-click waves.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='35453f6e-cd21-46fc-9fb9-1211c1c34319'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__double-right-click-mouse-solo-b003-04/20260924T093128Z-thuan-mac/reference/right double click mouse_35453f6e-cd21-46fc-9fb9-1211c1c34319.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='double-right-click-mouse-solo-b003-04'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('right double click mouse',)
    def build(self):
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                k,end,*args=c; name=f'{n}-{j}'
                if k=='L': self.add_line(name,here,end)
                elif k=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif k=='C': self.add_bezier(name,here,(args[0],args[1],end))
                here=end; members.append(name)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('mouse',(6,28),[('A',(18,16),12,12,True),('A',(30,28),12,12,True),('L',(30,30)),('A',(6,30),12,12,True),('L',(6,28))],True)
        poly('button',(18,16),(18,28),(30,28));join('button','mouse')
        path('wave-inner',(26,6),[('C',(31,13),(29,7),(31,10))])
        path('wave-outer',(38,6),[('C',(42,22),(42,12),(42,18))])
