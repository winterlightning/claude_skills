"""Circular globe inside curved meridian with stable pedestal.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
No useful exact Lucide match inspected; supplied reference guided the geometric reconstruction.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a5e62027-4155-4c3f-9eea-0fcf4e0f687b'
SOURCE_PATH = 'pictographic-primitives/maps/earth model 1_a5e62027-4155-4c3f-9eea-0fcf4e0f687b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='earth-model-1'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='maps'
    aliases=()
    keywords=('earth model 1',)
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
        circle('globe',18,14,10)
        path('meridian',(34,4),[('C',(40,20),(38,8),(40,14)),('A',(24,36),16,16,True),('C',(8,32),(18,36),(12,35))])
        line('stem',(24,36),(24,44));poly('base',(12,44),(24,44),(36,44));join('stem','base');join('stem','meridian')
