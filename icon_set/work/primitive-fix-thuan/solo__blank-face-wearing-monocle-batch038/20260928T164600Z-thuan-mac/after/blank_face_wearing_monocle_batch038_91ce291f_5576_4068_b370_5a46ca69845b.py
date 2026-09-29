"""blank-face-wearing-monocle-batch038: Restored a circular head, enlarged the monocle, and carried its cord below the face. The cord crosses the circular face at a shared junction.
Plan: subject-owned contours, shared connection points, mirrored repeated shapes.
Construction: inspected Lucide glasses original and atomic-debug; coherent curves and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '91ce291f-5576-4068-b370-5a46ca69845b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__blank-face-wearing-monocle-batch038/20260928T164600Z-thuan-mac/reference/face monocle_91ce291f-5576-4068-b370-5a46ca69845b.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'blank-face-wearing-monocle-batch038'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('blank', 'face', 'wearing', 'monocle', 'batch038')

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

        # Human construction reference: human_ref/user.svg circular head; no body is present.
        path('face',(24,4),[('A',(44,24),20,20,True),('A',(36,40),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        circle('monocle',29,20,7)
        poly('cord',(36,20),(36,40),(36,44));join('cord','monocle');join('cord','face')


Revision.exception = {'reason': 'Preserve the full circular face and a large recognizable monocle. The hanging cord deliberately extends outside the radial keyshape but remains inset inside the 48px canvas. Lens-to-face visible clearance is 2.60px; cord crosses the face at a real shared junction. These features remain distinct in both themes at native 48px.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': '77dea010dcdb16a64bf9b15544b3c571292eae456adec52d82fbe1673df4b4ff'}
