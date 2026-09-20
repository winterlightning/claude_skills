"""Beer Mug and Bread Loaf.

Plan: Beer mug behind domed bread, foam top and right handle. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit scoring and tiny foam lobes; shared attachment points preserve occlusion by bread.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/34-f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'beer-mug-with-bread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('beer', 'mug', 'with', 'bread')

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
        path('mug',(16,26),[('L',(16,14)),('A',(16,6),4,4,True),('C',(25,8),(19,6),(22,6)),('C',(34,10),(30,6),(34,6)),('L',(34,18)),('L',(34,30)),('L',(34,38)),('A',(30,42),4,4,True),('L',(26,42))])
        path('handle',(34,18),[('L',(42,18)),('L',(42,30)),('L',(34,30))]);join('mug','handle')
        path('bread',(6,42),[('L',(6,36)),('A',(16,26),10,10,True),('A',(26,36),10,10,True),('L',(26,42)),('L',(6,42))],True);join('mug','bread')
