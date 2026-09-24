"""Anatomical ankle and continuous heel, arch and rounded toes; omit extraction specks.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='dcbbd8ae-d89f-5e3c-838f-3a4b9ef6294a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__foot-in-side-view-batch-012-09/20260924T093128Z-thuan-mac/reference/specialty feet_dcbbd8ae-d89f-5e3c-838f-3a4b9ef6294a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='foot-in-side-view-batch-012-09'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('specialty feet',)
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
        path('foot',(10,8),[('L',(10,20)),('C',(4,34),(10,28),(4,28)),('A',(10,40),6,6,False),('C',(16,38),(12,40),(14,39)),('C',(32,38),(22,34),(26,38)),('L',(38,38)),('A',(38,28),6,5,False),('C',(24,18),(32,28),(24,22)),('L',(24,8))])
