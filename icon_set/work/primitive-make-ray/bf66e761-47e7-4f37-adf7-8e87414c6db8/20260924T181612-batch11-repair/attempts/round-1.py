"""Road Bicycle
Plan: Two equal wheels, triangular road frame, saddle and drop bar.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: Lucide bike construction examined; source road-bike frame retained.
Reduction: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bf66e761-47e7-4f37-adf7-8e87414c6db8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tandem bike_bf66e761-47e7-4f37-adf7-8e87414c6db8.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'single-rider-road-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
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
        self.add_polyline('frame',(12,32),(20,14),(28,32),(12,32),(32,14),(36,32))
        for p in ('rear','front'):self.relate('connect','frame',p)
        self.add_line('saddle',(16,8),(24,8));self.add_line('seatpost',(20,8),(20,14));self.relate('connect','saddle','seatpost');self.relate('connect','frame','seatpost')
        path('handle',(29,8),[('L',(36,8)),('A',(40,12),4,4,True)]);self.add_line('stem',(32,8),(32,14));self.relate('connect','stem','handle');self.relate('connect','stem','frame')
