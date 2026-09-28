"""Couple Beside Heart Shaped Balloon
Plan: Two small human figures beside attached heart balloon
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: human_ref/full_body_ref.png; exact detached head gap.
Reduction: Reduce bodies to clear round-ended limbs and dress outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb01aec5-8d69-470f-9cde-ccfb72c0af02'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dating couple balloon_bb01aec5-8d69-470f-9cde-ccfb72c0af02.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'couple-beside-heart-shaped-balloon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('couple', 'people', 'balloon', 'heart', 'string', 'together', 'celebration')

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
        for name,x in [('a',8),('b',22)]:
            path('head-'+name,(x-2,15),[('A',(x+2,15),2,2,True),('A',(x-2,15),2,2,True)],True)
            self.add_line('torso-'+name,(x,25),(x,34))
            path('legs-'+name,(x-4,40),[('L',(x,34)),('L',(x+4,40))]);self.relate('connect','legs-'+name,'torso-'+name)
            self.mark_human_figure(name,head='head-'+name,torso='torso-'+name,torso_junction='start')
        path('arms',(8,25),[('L',(16,26)),('L',(22,25)),('L',(34,28)),('L',(38,20))]);self.relate('connect','arms','torso-a');self.relate('connect','arms','torso-b')
        path('balloon',(38,20),[('C',(32,12),(34,16),(32,16)),('C',(35,8),(32,10),(33,8)),('C',(38,10),(37,8),(38,10)),('C',(41,8),(38,10),(39,8)),('C',(44,12),(43,8),(44,10)),('C',(38,20),(44,16),(42,16))],True)
        self.relate('connect','arms','balloon')

# Final review: Two full figures use radius-2 circular heads at y15 and torso junction y25: exactly 8 centerline / 4 ink units; simplify dress and shirt to shared human limbs, preserve held heart balloon.
