"""arrow-down-after-two-opposing-bends: Widened the upper bend, balanced both arrowhead arms and kept clearance from the middle shaft.
Plan: subject-owned contours, shared connection points, mirrored repeated shapes.
Construction: inspected Lucide corner-down-right original and atomic-debug; coherent curves and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '80755080-33d0-42e7-9bca-68d0d18ad221'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-down-after-two-opposing-bends/20260928T164600Z-thuan-mac/reference/diagram dash wave down_80755080-33d0-42e7-9bca-68d0d18ad221.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'arrow-down-after-two-opposing-bends'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'down', 'after', 'two', 'opposing', 'bends')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for i,(kind,end,*args) in enumerate(steps):
                eid=f'{name}-{i}';members.append(eid)
                if kind=='L':self.add_line(eid,here,end)
                elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        def poly(name,*pts):self.add_polyline(name,*pts,closed=pts[0]==pts[-1])
        def join(a,b):self.relate('connect',a,b)

        path('shaft',(4,8),[('L',(4,32)),('A',(20,32),8,8,False),('L',(20,16)),('A',(36,16),8,8,True),('L',(36,32))])
        poly('head',(28,24),(36,32),(44,24));join('head','shaft')
