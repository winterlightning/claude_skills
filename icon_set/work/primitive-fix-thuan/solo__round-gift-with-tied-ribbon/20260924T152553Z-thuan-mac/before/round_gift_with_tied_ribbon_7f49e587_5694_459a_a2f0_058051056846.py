"""Circular Gift Box With Bow.

Plan: Round gift with bow occupying top half and crossing ribbons below; circle r20. Actual bow/ribbon junction24,24.
Construction: Lucide gift: shared bow attachment.
Reduction: Omitted upper vertical ribbon and tails to make room for paired bow loops.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f49e587-5694-459a-a2f0-058051056846'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/39-7f49e587-5694-459a-a2f0-058051056846.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'round-gift-with-tied-ribbon'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('round', 'gift', 'with', 'tied', 'ribbon')

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
        circle('box',24,24,20)
        line('ribbon-v',(24,24),(24,44));join('ribbon-v','box')
        line('ribbon-left',(4,24),(24,24));join('ribbon-left','box');join('ribbon-left','ribbon-v')
        line('ribbon-right',(24,24),(44,24));join('ribbon-right','box');join('ribbon-right','ribbon-v');join('ribbon-left','ribbon-right')
        path('bow',(17,17),[('C',(24,24),(17,11),(24,17)),('C',(31,17),(24,17),(31,11)),('C',(24,24),(37,17),(31,24)),('C',(17,17),(17,24),(11,17))],True)
        join('bow','ribbon-left');join('bow','ribbon-right');join('bow','ribbon-v')
