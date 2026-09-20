"""Butler with Bowtie.

Plan: Butler avatar: headr7 at24,11, shoulder plateauy22 =>4 centerline/0 ink gap. Two full bowtie lobes fit lower torso.
Construction: Human user.svg: shared round head and curved shoulders; icon-avatar head/body contact.
Reduction: Slightly smaller circular head reserves full bowtie openings; sleeve seams omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f673664b-85b3-410d-a058-e07884f97429'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/22-f673664b-85b3-410d-a058-e07884f97429.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'manservant'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ()
    keywords = ('manservant',)

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
        self.add_arc('head-top',(17,11),(31,11),radius_x=7)
        self.add_arc('face',(31,11),(17,11),radius_x=7)
        self.add_contour('head','head-top','face',closed=True)
        line('body-left',(8,44),(8,30))
        self.add_arc('body-shoulder-left',(8,30),(16,22),radius_x=8)
        line('body-top',(16,22),(32,22))
        self.add_arc('body-shoulder-right',(32,22),(40,30),radius_x=8)
        line('body-right',(40,30),(40,44))
        self.add_contour('body-shoulders','body-shoulder-left','body-top','body-shoulder-right');join('head','body-shoulders');join('body-left','body-shoulders');join('body-right','body-shoulders')
        poly('body-bow-left',(16,31),(16,44),(24,37),closed=True)
        poly('body-bow-right',(32,31),(32,44),(24,37),closed=True);join('body-bow-left','body-bow-right')
