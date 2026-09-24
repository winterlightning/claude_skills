"""Round muzzle and pointed ear above recovery cone; two visible neck edges.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e8a4e2f0-e683-57b4-a6bb-145c10b5efac'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dog-wearing-recovery-cone/20260924T093128Z-thuan-mac/reference/pet cone_e8a4e2f0-e683-57b4-a6bb-145c10b5efac.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dog-wearing-recovery-cone'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('pet cone',)
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
        poly('cone',(6,30),(42,14),(36,34),(20,42),(6,30))
        path('head',(14,26),[('L',(14,20)),('A',(22,14),8,6,True),('L',(22,6)),('A',(34,18),12,12,True)])
        join('head','cone')
        line('neck',(36,34),(42,42));join('neck','cone')
