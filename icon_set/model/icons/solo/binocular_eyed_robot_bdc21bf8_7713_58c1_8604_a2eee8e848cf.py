"""Robot with Binocular Eyes.

Plan: Binocular robot head above tracked square body; two equal pupils. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Combine the binocular eye rims into one wide rounded head with paired pupils; retain short neck, rectangular body and two side tracks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdc21bf8-7713-58c1-8604-a2eee8e848cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/40-bdc21bf8-7713-58c1-8604-a2eee8e848cf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'binocular-eyed-robot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('binocular', 'eyed', 'robot')

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
        path('eyes',(6,15),[('A',(15,6),9,9,True),('L',(33,6)),('A',(42,15),9,9,True),('A',(33,24),9,9,True),('L',(24,24)),('L',(15,24)),('A',(6,15),9,9,True)],True)
        for x in (15,33):self.add_dot(f'pupil-{x}',(x,15))
        line('neck',(24,24),(24,33));join('eyes','neck')
        poly('body',(14,33),(24,33),(34,33),(34,42),(14,42),closed=True);join('body','neck')
        poly('track-left',(14,33),(6,33),(6,42),(14,42));join('body','track-left')
        poly('track-right',(34,33),(42,33),(42,42),(34,42));join('body','track-right')
