"""Restore bass waist, continuous rounded body and long diagonal neck.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
No useful exact Lucide match inspected; supplied reference guided the geometric reconstruction.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='084164fe-fde8-45f3-af63-b15e617e7641'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__double-bass-diagonal/20260924T093128Z-thuan-mac/reference/contrabass_084164fe-fde8-45f3-af63-b15e617e7641.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='double-bass-diagonal'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('contrabass',)
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
        path('body',(28,18),[('C',(18,20),(24,12),(18,12)),('C',(12,24),(18,26),(14,26)),('C',(6,32),(8,20),(6,26)),('C',(18,42),(6,38),(12,42)),('C',(26,34),(26,42),(30,38)),('C',(30,28),(22,30),(26,28)),('C',(28,18),(38,28),(36,22))],True)
        poly('neck',(28,18),(40,6),(42,8));join('body','neck')
