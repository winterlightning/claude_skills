"""Simple Classic Key.

Plan: Centerline6,6,42,42. Lower-left round bow radius10; upper-right single shaft with two equal teeth on shared nodes.
Construction: No useful direct Lucide match; round bow with single-stroke shaft and repeated teeth.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42e97a5b-5209-4677-a990-d97a3b5141d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/17-42e97a5b-5209-4677-a990-d97a3b5141d1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'classic-key'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('classic', 'key')

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
        path('bow',(26,32),[('A',(6,32),10,10,True),('A',(16,22),10,10,True),('A',(22,24),10,10,True),('A',(26,32),10,10,True)],True)
        poly('shaft',(22,24),(30,16),(34,12),(40,6),(42,8))
        line('tooth-inner',(30,16),(36,22));
        join('bow','shaft');join('shaft','tooth-inner')
