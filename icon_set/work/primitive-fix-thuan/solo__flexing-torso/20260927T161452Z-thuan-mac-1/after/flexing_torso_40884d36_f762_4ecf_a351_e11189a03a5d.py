"""Strong Bodybuilder Flexing Arms.

Plan: Headless muscular torso with mirrored raised forearms and flexed biceps; bounds (4,8)-(44,40).
Construction: human_ref/full_body_ref.png: coherent limb construction; intentional headless strength subject follows source.
Reduction: Finger folds and muscle creases omitted; two broad raised forearms and tapered torso retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '40884d36-f762-4ecf-a351-e11189a03a5d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flexing-torso/20260927T161452Z-thuan-mac-1/reference/tough guy_40884d36-f762-4ecf-a351-e11189a03a5d.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'flexing-torso'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('flexing', 'torso')

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
        # Round the two raised fists while keeping the mirrored flex pose.
        path('torso',(16,40),[
            ('L',(14,28)),('C',(4,24),(8,29),(4,28)),
            ('L',(6,12)),('C',(10,8),(6,9),(8,8)),('L',(12,8)),
            ('C',(16,12),(14,8),(16,9)),('L',(16,20)),
            ('C',(24,20),(18,18),(21,20)),('C',(32,20),(27,20),(30,18)),
            ('L',(32,12)),('C',(36,8),(32,9),(34,8)),('L',(38,8)),
            ('C',(42,12),(40,8),(42,9)),('L',(44,24)),
            ('C',(34,28),(44,28),(40,29)),('L',(32,40)),('L',(16,40))],True)
