"""Prehistoric Woolly Mammoth.

Plan: Left-facing mammoth with arched back, hanging trunk, forward tusk, two legs and tail. Bounds4,8,44,40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Use one prominent tusk and omit tiny eye; preserve trunk, high back, legs and tail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7f76942-5429-5bfb-a03f-aa82345155cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/38-a7f76942-5429-5bfb-a03f-aa82345155cf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'mammoth-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('mammoth', 'in', 'profile')

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
        path('body',(12,40),[('L',(12,30)),('L',(12,20)),('C',(24,8),(12,12),(17,8)),('C',(40,24),(33,8),(40,16)),('L',(40,40))])
        path('trunk',(12,20),[('L',(4,20)),('L',(4,32)),('A',(12,40),8,8,False)]);join('body','trunk')
        path('belly',(12,30),[('C',(31,31),(18,33),(25,33)),('L',(31,40))]);join('body','belly')
        path('tusk',(12,20),[('C',(4,10),(4,20),(4,16))]);join('body','tusk');join('trunk','tusk')
        line('tail',(40,24),(44,32));join('body','tail')
