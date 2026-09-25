"""Poseidon Holding Trident.

Plan: Crowned robed Poseidon holds tall three-prong trident at right. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit robe fold and tiny crown band; preserve robed figure physically gripping trident, not a status combination.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82fdb403-45fe-4e25-9e15-98892046ca82'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/35-82fdb403-45fe-4e25-9e15-98892046ca82.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'poseidon-holding-trident'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('poseidon', 'holding', 'trident')

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
        circle('head',13,10,4)
        line('torso',(13,22),(13,23));self.mark_human_figure('poseidon',head='head',torso='torso',torso_junction='start')
        poly('robe',(6,42),(13,23),(25,42),closed=True);join('torso','robe')
        poly('arm',(13,23),(24,30),(34,30));join('torso','arm');join('robe','arm')
        poly('trident',(26,6),(26,15),(34,20),(42,15),(42,6))
        poly('shaft',(34,6),(34,20),(34,30),(34,42));join('trident','shaft');join('arm','shaft')
