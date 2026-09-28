"""Smooth sitting dog with lifted forepaw, muzzle, pointed ear and curved tail.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide dog: coherent rounded animal contours.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='520f29cc-1cbb-4177-b8b8-89624c81e125'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dog-offering-paw/20260924T093128Z-thuan-mac/reference/dog giving hand paw_520f29cc-1cbb-4177-b8b8-89624c81e125.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dog-offering-paw'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('dog giving hand paw',)
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
        path('dog',(28,18),[('C',(24,6),(28,12),(28,6)),('L',(20,12)),('L',(10,14)),('A',(16,22),6,8,False),('L',(20,22)),('L',(20,30)),('L',(12,26)),('C',(6,30),(8,24),(6,26)),('C',(10,34),(6,32),(8,33)),('L',(18,34)),('L',(26,34)),('C',(20,42),(24,40),(20,38)),('L',(32,42)),('A',(38,30),6,12,False),('L',(28,18))],True)
        path('tail',(38,30),[('A',(42,18),4,12,False)]);join('dog','tail')
