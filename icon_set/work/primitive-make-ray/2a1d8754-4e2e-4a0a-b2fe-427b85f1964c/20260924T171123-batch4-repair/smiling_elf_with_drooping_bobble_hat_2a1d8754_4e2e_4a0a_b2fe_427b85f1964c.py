"""Smiling elf wearing a drooping bobble hat.
Plan: SQUARE fits the round jaw, broad ears and tall hat. Smooth circular jaw, integrated ears and deliberately asymmetric hat; reviewed at 48px in both themes.
Reduction: Tiny eyes and internal ear seams omitted to preserve open negative space.
Construction references: human_ref/user.svg for circular facial construction; no torso is depicted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2a1d8754-4e2e-4a0a-b2fe-427b85f1964c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/elf_2a1d8754-4e2e-4a0a-b2fe-427b85f1964c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'smiling-elf-with-drooping-bobble-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('elf', 'hat', 'ears', 'smile', 'christmas', 'face', 'bobble')

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
        # Ears belong to the outer face silhouette, without narrow enclosed seams.
        path('hat',(12,22),[('C',(26,6),(15,13),(19,6)),('C',(38,14),(30,6),(32,14))])
        circle('bobble',39,11,3);self.relate('connect','bobble','hat')
        path('face',(12,22),[('L',(6,24)),('C',(12,30),(6,28),(8,30)),('A',(24,42),12,12,False),('A',(36,30),12,12,False),('C',(42,24),(40,30),(42,28)),('L',(36,22)),('L',(12,22))],True)
        self.relate('connect','hat','face')
        path('smile',(21,31),[('A',(27,31),4,4,False)])