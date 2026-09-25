"""Sole silhouette with round toe contours and broad reflexology regions.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
No useful exact Lucide match inspected; supplied reference guided the geometric reconstruction.
Human reference: icon_set/references/human_ref/full_body_ref.png; hand/foot contour only, no detached head.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='190a87c0-f140-4783-889d-2b08bb653fa3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__foot-reflexology-map-190a87c0/20260924T093128Z-thuan-mac/reference/massage map foot_190a87c0-f140-4783-889d-2b08bb653fa3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='foot-reflexology-map-190a87c0-solo'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'health'
    aliases=()
    keywords=('massage map foot',)
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
        path('sole',(10,14),[('A',(16,4),6,10,True),('A',(22,10),6,6,True),('A',(30,10),4,4,True),('A',(38,18),8,8,True),('L',(36,24)),('L',(34,32)),('A',(24,44),10,12,True),('A',(10,32),14,12,True),('L',(10,24)),('L',(10,14))],True)
        path('arch',(10,24),[('C',(24,20),(16,24),(20,24)),('C',(36,24),(28,24),(32,24))]);join('arch','sole')
        line('heel',(10,32),(34,32));join('heel','sole')
