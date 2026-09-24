"""Balanced crossed x and smooth superscript two.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1195ed25-2865-5967-8377-ba7934eebadd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__exponential/20260924T093128Z-thuan-mac/reference/exponential_1195ed25-2865-5967-8377-ba7934eebadd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='exponential'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('exponential',)
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
        poly('x-a',(6,22),(15,32),(24,42));poly('x-b',(6,42),(15,32),(24,22));join('x-a','x-b')
        path('two',(30,10),[('C',(36,6),(30,8),(32,6)),('A',(42,12),6,6,True),('C',(33,22),(42,16),(35,19)),('L',(42,22))])
