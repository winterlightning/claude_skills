"""Small left-facing fish with a smooth body, gill divider, modest paired fins, and forked tail. The source sets the direction and identifying features."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd9eb1be5-4fde-486e-a74d-a5906997b2f2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__small-fish-facing-left/20260927T172707Z-thuan-mac-1/reference/anchovy_d9eb1be5-4fde-486e-a74d-a5906997b2f2.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'small-fish-facing-left'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('fish', 'anchovy', 'aquatic', 'fins', 'tail', 'gill', 'sea')

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

        # Slender anchovy body and modest paired fins replace the heavy spikes.
        path('fish',(4,24),[('C',(20,18),(8,19),(13,18)),('L',(26,14)),('L',(28,18)),('C',(34,20),(31,18),(33,19)),('L',(44,10)),('L',(40,24)),('L',(44,38)),('L',(34,28)),('C',(28,30),(33,29),(31,30)),('L',(26,34)),('L',(20,30)),('C',(4,24),(13,30),(8,29))],True)
        path('gill',(20,18),[('L',(20,30))]);self.relate('connect','fish','gill')
