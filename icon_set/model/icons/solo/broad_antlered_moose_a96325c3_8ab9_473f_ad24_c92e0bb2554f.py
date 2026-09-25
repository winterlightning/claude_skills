"""Broad-Antlered Moose
Plan: Right-facing moose, drooping muzzle and broad upward-tined antler.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Antler tines reduced to three broad tips; tiny eye omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a96325c3-8ab9-473f-ad24-c92e0bb2554f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/moose body_a96325c3-8ab9-473f-ad24-c92e0bb2554f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-antlered-moose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('moose', 'antlers', 'animal', 'wildlife', 'mammal', 'standing')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        path('moose',(6,42),[('L',(6,29)),('C',(15,20),(6,23),(10,20)),('L',(26,20)),('C',(34,14),(28,16),(30,14)),('C',(42,24),(40,14),(42,19)),('C',(34,27),(42,31),(38,25)),('L',(32,42)),('L',(24,42)),('L',(24,31)),('L',(14,31)),('L',(14,42)),('L',(6,42))],True)
        path('antler',(34,14),[('L',(30,11)),('L',(15,11)),('C',(6,6),(8,11),(6,11))]);self.relate('connect','antler','moose')
        for x,y in ((16,6),(25,6)):self.add_line(f'tine-{x}',(x,11),(x,y));self.relate('connect',f'tine-{x}','antler')
