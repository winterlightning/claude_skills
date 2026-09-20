"""Soldier in Helmet.

Plan: Helmeted avatar centered24, circular jaw radius10 cy16; jaw26 shoulder30 exact0 ink gap. Bounds (8,4)-(40,44).
Construction: human_ref/user.svg: circular jaw and broad rounded shoulders; helmet brim integrated at jaw endpoints.
Reduction: V-neck, tiny pocket and arm seam omitted; central uniform fastening and helmet identify the soldier.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5829da22-ee07-4d27-bba0-429b29d189a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/03-5829da22-ee07-4d27-bba0-429b29d189a4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'helmeted-soldier-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ()
    keywords = ('helmeted', 'soldier', 'bust')

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
        self.add_arc('face',(14,16),(34,16),radius_x=10,radius_y=10,sweep=False)
        path('helmet',(12,16),[('A',(24,4),12,12,True),('A',(36,16),12,12,True),('L',(34,16)),('L',(14,16)),('L',(12,16))],True);join('face','helmet')
        self.add_arc('body-left',(8,42),(20,30),radius_x=12,radius_y=12,sweep=True)
        line('body-top',(20,30),(28,30));self.add_arc('body-right',(28,30),(40,42),radius_x=12,radius_y=12,sweep=True)
        line('body-side-left',(8,42),(8,44));line('body-side-right',(40,42),(40,44))
        join('body-left','body-top');join('body-right','body-top');join('body-left','body-side-left');join('body-right','body-side-right');join('face','body-top')
        line('body-seam',(24,30),(24,44));join('body-top','body-seam')
