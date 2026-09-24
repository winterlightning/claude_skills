"""Round dog head and muzzle above a cupped human hand; remove angular fist.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='511ea518-3b8b-552d-b9df-827c71ed2c6b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dog-paw-on-hand/20260924T093128Z-thuan-mac/reference/dog training giving hand paw_511ea518-3b8b-552d-b9df-827c71ed2c6b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dog-paw-on-hand'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('dog training giving hand paw',)
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
        path('dog',(42,30),[('L',(42,16)),('A',(26,16),8,10,False),('L',(18,16)),('A',(24,24),6,8,False),('L',(28,24)),('L',(28,34))])
        path('hand',(6,30),[('L',(12,30)),('L',(20,34)),('L',(32,34)),('A',(32,42),4,4,True),('L',(20,42)),('L',(6,38))])
        join('dog','hand')
