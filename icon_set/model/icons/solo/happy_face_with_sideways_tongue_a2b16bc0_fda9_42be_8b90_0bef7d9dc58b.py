"""Squinting Face with Tongue Out.

Plan: Happy arched eyes and right-sided tongue inside round face; radius20 centered24.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Lower face rim opened where the tongue protrudes; Eye arches shortened to leave room for the sideways tongue.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2b16bc0-fda9-42be-8b90-0bef7d9dc58b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/18-a2b16bc0-fda9-42be-8b90-0bef7d9dc58b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'happy-face-with-sideways-tongue'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('happy', 'face', 'with', 'sideways', 'tongue')

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
        self.add_arc('face',(8,36),(40,36),radius_x=20,radius_y=20,sweep=True,large_arc=True)
        path('eye-left',(16,18),[('A',(20,18),2,2,True)]);path('eye-right',(28,18),[('A',(32,18),2,2,True)])
        path('smile',(14,27),[('C',(22,28),(16,29),(20,29)),('L',(30,27))])
        path('tongue',(22,28),[('L',(22,38)),('A',(30,38),4,4,False),('L',(30,27))]);join('smile','tongue')
