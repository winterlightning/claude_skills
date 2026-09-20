"""Single Eyed Cloud.

Plan: Soft lobed cloud creature with one large concentric eye. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Preserve cloud lobes and single ring eye/pupil.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '736f147c-5c65-480e-94f1-32e97daa683c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/49-736f147c-5c65-480e-94f1-32e97daa683c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'single-eyed-cloud-creature'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('single', 'eyed', 'cloud', 'creature')

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
        path('cloud',(6,24),[('C',(11,11),(6,15),(6,10)),('C',(24,6),(14,6),(18,6)),('C',(37,11),(30,6),(34,6)),('C',(42,24),(42,10),(42,15)),('C',(37,37),(42,33),(42,38)),('C',(24,42),(34,42),(30,42)),('C',(11,37),(18,42),(14,42)),('C',(6,24),(6,38),(6,33))],True)
        circle('eye',24,24,9);self.add_dot('pupil',(24,24))
