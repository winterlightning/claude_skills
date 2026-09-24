"""Flamingo with arched back, long S neck, beak and bent leg.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0eedad4e-672e-40c7-9399-bd5db48d8049'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__flamingo/20260924T093128Z-thuan-mac/reference/wild bird flamingo_0eedad4e-672e-40c7-9399-bd5db48d8049.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='flamingo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('wild bird flamingo',)
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
        path('bird',(8,28),[('C',(24,24),(12,16),(20,18)),('L',(24,10)),('A',(36,10),6,6,True),('L',(40,12)),('L',(32,12)),('L',(32,24)),('A',(20,34),12,10,True),('L',(8,28))],True)
        line('leg',(20,34),(20,44));join('bird','leg')
        poly('bent-leg',(20,34),(12,40),(20,40));join('bird','bent-leg');join('leg','bent-leg')
