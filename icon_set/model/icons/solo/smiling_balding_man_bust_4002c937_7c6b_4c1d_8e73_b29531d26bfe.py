"""Smiling Elderly Man.

Plan: Avatar centered x24, circular jaw radius12 cy16, jaw bottom28, shoulder top32: exact0 ink gap. Bounds (8,4)-(40,44).
Construction: Shared human_ref/user.svg: circular face, broad curved shoulders; avatar contact uses the current zero ink gap rule.
Reduction: Bald dome, two side hair tufts and smile retained; ears and tiny eye marks omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4002c937-7c6b-4c1d-8e73-b29531d26bfe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/37-4002c937-7c6b-4c1d-8e73-b29531d26bfe.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'smiling-balding-man-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ()
    keywords = ('smiling', 'balding', 'man', 'bust')

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
        self.add_arc('face',(12,16),(36,16),radius_x=12,radius_y=12,sweep=False)

        path('crown',(12,16),[('A',(24,4),12,12,True),('A',(36,16),12,12,True)]);join('face','crown')
        line('hair-left',(12,16),(10,10));line('hair-right',(36,16),(38,10));join('crown','hair-left');join('crown','hair-right')

        path('smile',(21,16),[('C',(27,16),(22,19),(26,19))])
        self.add_arc('body-left',(8,44),(20,32),radius_x=12,radius_y=12,sweep=True)
        line('body-top',(20,32),(28,32))
        self.add_arc('body-right',(28,32),(40,44),radius_x=12,radius_y=12,sweep=True)
        join('body-top','body-left');join('body-top','body-right');join('face','body-top')
