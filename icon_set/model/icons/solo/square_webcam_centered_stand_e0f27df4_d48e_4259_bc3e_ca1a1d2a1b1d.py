"""Square Digital Webcam.

Plan: Square webcam on central stem and foot, concentric optical detail; bounds (8,4)-(40,44).
Construction: Lucide webcam: central lens, short stem and flat foot.
Reduction: Tiny inner lens circle omitted; square camera housing retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0f27df4-d48e-4259-bc3e-ca1a1d2a1b1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/12-e0f27df4-d48e-4259-bc3e-ca1a1d2a1b1d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'square-webcam-centered-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('square', 'webcam', 'centered', 'stand')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('body',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,32)),('A',(36,36),4,4,True),('L',(24,36)),('L',(12,36)),('A',(8,32),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        circle('lens',24,20,7)
        line('stem',(24,36),(24,44));poly('foot',(12,44),(24,44),(36,44));join('body','stem');join('stem','foot')
