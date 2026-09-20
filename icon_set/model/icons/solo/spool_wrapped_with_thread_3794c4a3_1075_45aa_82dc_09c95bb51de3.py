"""Spool of Thread.

Plan: Upright thread spool with top and bottom hubs and one diagonal wrap; bounds (8,4)-(40,44).
Construction: Lucide spool: structural hubs and broad diagonal thread runs.
Reduction: Fine strands reduced to one broad diagonal thread run.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3794c4a3-1075-45aa-82dc-09c95bb51de3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/07-3794c4a3-1075-45aa-82dc-09c95bb51de3.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'spool-wrapped-with-thread'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('spool', 'wrapped', 'with', 'thread')

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
        path('body',(8,12),[('L',(16,12)),('L',(28,12)),('L',(32,12)),('L',(32,36)),('L',(28,36)),('L',(16,36)),('L',(8,36)),('L',(8,12))],True)
        poly('top-hub',(16,12),(16,4),(28,4),(28,12));poly('bottom-hub',(16,36),(16,44),(28,44),(40,44));join('body','top-hub');join('body','bottom-hub')
        line('thread',(8,28),(32,20));join('body','thread')
