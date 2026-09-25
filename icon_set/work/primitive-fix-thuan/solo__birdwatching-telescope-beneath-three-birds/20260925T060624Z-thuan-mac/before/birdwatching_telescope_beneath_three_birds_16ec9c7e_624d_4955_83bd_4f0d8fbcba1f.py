"""Birdwatching Telescope Beneath Three Birds
Plan: Telescope points upper-right on a tripod, with three V birds spread overhead.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful exact Lucide match; simple barrel and three shared tripod endpoints.
Reduction: Reduced stepped barrel to one outline; preserved three birds and three legs.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16ec9c7e-624d-4955-83bd-4f0d8fbcba1f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bird watching 2_16ec9c7e-624d-4955-83bd-4f0d8fbcba1f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'birdwatching-telescope-beneath-three-birds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/optics'
    aliases = ()
    keywords = ('telescope', 'birdwatching', 'birds', 'tripod', 'observation', 'nature', 'sky')

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
        self.add_polyline('scope',(6,26),(38,18),(42,30),(26,34),(10,38),closed=True)
        self.add_polyline('tripod',(14,42),(26,34),(38,42))
        self.add_line('center-leg',(26,34),(26,42))
        self.relate('connect','tripod-1','center-leg');self.relate('connect','tripod-2','center-leg')
        for leg in ['tripod-1','tripod-2','center-leg']:
            for edge in ['scope-3','scope-4']:self.relate('connect',leg,edge)
        for j,x in enumerate([9,24,39]):self.add_polyline(f'bird-{j}',(x-3,6),(x,9),(x+3,6))
