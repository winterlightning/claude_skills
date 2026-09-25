"""A bicycle with two equal wheels, saddle and handlebar.
Plan: HRECT_L accommodates the wide wheel pair and upper frame.
Reduction: Removed crowded lower frame tubes, pedal and drop-bar curl; retained an open V frame and both wheels.
Construction: Lucide bike: equal circles, joined frame, saddle and handlebar.
Layout: Source filename says tandem but the supplied image shows one ordinary bicycle; no extra seat or rider added."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf66e761-47e7-4f37-adf7-8e87414c6db8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tandem bike_bf66e761-47e7-4f37-adf7-8e87414c6db8.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'single-rider-road-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bicycle', 'bike', 'road', 'cycle', 'wheel', 'frame', 'saddle', 'handlebar')

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
        circle('rear',12,32,8);circle('front',36,32,8)
        self.add_polyline('frame',(12,24),(12,12),(24,20),(36,12),(36,24))
        self.add_polyline('saddle',(8,12),(12,12),(16,12))
        self.add_polyline('handle',(36,12),(32,8),(40,8))
        for part in ('rear','front','saddle','handle'): self.relate('connect','frame',part)
