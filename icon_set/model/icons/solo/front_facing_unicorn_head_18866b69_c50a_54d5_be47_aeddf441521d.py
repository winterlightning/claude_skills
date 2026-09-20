"""Front Facing Unicorn Head.

Plan: Long horse head with pointed horn and ears, eye pair and rounded muzzle. Extremes8,4,40,44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit muzzle divider; use solid strokes for the paired ears and horn, retaining the long horse face and paired eyes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18866b69-c50a-54d5-be47-aeddf441521d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/06-18866b69-c50a-54d5-be47-aeddf441521d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'front-facing-unicorn-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('front', 'facing', 'unicorn', 'head')

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
        path('face',(11,22),[('L',(11,31)),('A',(24,44),13,13,False),('A',(37,31),13,13,False),('L',(37,22)),('L',(32,16)),('L',(24,16)),('L',(16,16)),('L',(11,22))],True)
        line('horn',(24,16),(24,4));join('face','horn')
        line('ear-left',(16,16),(8,10));join('face','ear-left')
        line('ear-right',(32,16),(40,10));join('face','ear-right')
        for x in (20,28):self.add_dot(f'eye-{x}',(x,26))
