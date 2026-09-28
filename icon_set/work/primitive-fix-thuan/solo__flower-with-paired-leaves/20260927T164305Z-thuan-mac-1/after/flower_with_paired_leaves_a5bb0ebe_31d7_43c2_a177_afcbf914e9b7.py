"""Simple Flower with Leaves.

Plan: Two rounded V petals on a cup bloom, straight stem and two pointed leaves. Extremes8,4,40,44.
Construction: Lucide flower-2 original/atomic-debug: bloom and paired leaf owners attached to stem.
Reduction: Keep the two petals and two outlined leaves; shift leaves lower for clear spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a5bb0ebe-31d7-43c2-a177-afcbf914e9b7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flower-with-paired-leaves/20260927T164305Z-thuan-mac-1/reference/flower enemy_a5bb0ebe-31d7-43c2-a177-afcbf914e9b7.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'flower-with-paired-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('flower', 'with', 'paired', 'leaves')

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
        path('bloom',(8,10),[('C',(12,4),(8,6),(8,4)),('L',(24,12)),('L',(36,4)),('C',(40,10),(40,4),(40,6)),('C',(24,20),(40,16),(31,20)),('C',(8,10),(17,20),(8,16))],True)
        line('stem',(24,20),(24,44));join('bloom','stem')
        # Raise the leaf pair to the middle of the stem, as in the source.
        path('leaf-left',(24,36),[('L',(8,27)),('L',(8,34)),('C',(24,36),(9,38),(17,38))],True);join('stem','leaf-left')
        path('leaf-right',(24,36),[('L',(40,27)),('L',(40,34)),('C',(24,36),(39,38),(31,38))],True);join('stem','leaf-right');join('leaf-left','leaf-right')
