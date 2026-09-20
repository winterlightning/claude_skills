"""Head of a Female Demon.

Plan: Female demon head with circular jaw, swept hair and large rising horns. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit small ear and inner hair seams; retain swept fringe, long hair and two horns.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6363560d-8de7-46cf-8cb9-dce62d507729'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/12-6363560d-8de7-46cf-8cb9-dce62d507729.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'horned-female-demon-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('horned', 'female', 'demon', 'head')

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
        path('face',(12,26),[('A',(36,26),12,12,False)])
        path('hair',(6,42),[('L',(12,26)),('L',(12,18)),('C',(24,16),(15,9),(21,11)),('C',(36,26),(24,22),(30,26)),('L',(42,42))]);join('face','hair')
        path('horn-left',(12,18),[('C',(6,6),(6,18),(6,12))]);join('hair','horn-left')
        path('horn-right',(36,26),[('C',(42,6),(42,20),(42,12))]);join('hair','horn-right')
