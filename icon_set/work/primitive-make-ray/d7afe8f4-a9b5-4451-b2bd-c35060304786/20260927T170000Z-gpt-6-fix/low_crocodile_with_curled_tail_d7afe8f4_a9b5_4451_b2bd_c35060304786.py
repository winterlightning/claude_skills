"""Low Crocodile with Curled Tail
Plan: Long right-facing snout, raised eye mound, bent leg and curled tail.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Tiny teeth and extra legs omitted for clear silhouette."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd7afe8f4-a9b5-4451-b2bd-c35060304786'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__low-crocodile-with-curled-tail/20260927T164353Z-thuan-mac-1/reference/crocodile_d7afe8f4-a9b5-4451-b2bd-c35060304786.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'low-crocodile-with-curled-tail'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('crocodile', 'reptile', 'animal', 'snout', 'tail', 'wildlife', 'legs')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('crocodile',(4,29),[
            ('C',(16,14),(4,20),(9,14)),('L',(29,14)),
            ('A',(37,14),4,4,True),('L',(44,14)),('L',(44,22)),
            ('L',(40,30)),('L',(30,30)),('L',(32,38)),
            ('L',(24,38)),('L',(21,30)),('L',(12,30)),
            ('C',(12,38),(5,29),(6,36)),('C',(4,29),(6,38),(4,34))
        ],True)
        self.add_line('mouth',(44,22),(34,22))
        self.relate('connect','crocodile','mouth')
