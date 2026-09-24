"""Smooth upward accelerating arc with aligned broken tail and arrowhead.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1f61f1a6-7004-4899-8bf1-688257e3f936'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__fast-up/20260924T093128Z-thuan-mac/reference/fast up_1f61f1a6-7004-4899-8bf1-688257e3f936.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='fast-up'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('fast up',)
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
        path('shaft',(22,34),[('C',(38,8),(32,28),(38,18))])
        poly('head',(32,14),(38,8),(44,14));join('shaft','head')
        line('dash-1',(4,40),(5,40));line('dash-2',(13,38),(14,38))
