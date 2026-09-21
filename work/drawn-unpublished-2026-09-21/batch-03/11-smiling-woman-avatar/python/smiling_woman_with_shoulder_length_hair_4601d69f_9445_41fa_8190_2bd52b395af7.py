"""Smiling Woman with Shoulder-Length Hair
Plan: Round-jawed woman with shoulder-length hair and curved shoulders.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: human_ref/user.svg: circular jaw and curved body; current avatar contact.
Reduction: Tiny eyes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4601d69f-9445-41fa-8190-2bd52b395af7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/babe_4601d69f-9445-41fa-8190-2bd52b395af7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-woman-with-shoulder-length-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'portrait', 'hair', 'smile', 'bust', 'face', 'person')

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
        path('hair',(8,28),[('L',(10,19)),('C',(24,4),(10,9),(16,4)),('C',(38,19),(32,4),(38,9)),('L',(40,28))])
        path('face',(14,17),[('C',(28,12),(19,17),(25,15)),('L',(34,18)),('L',(34,23)),('A',(24,33),10,10,True),('A',(14,23),10,10,True),('L',(14,17))],True)
        path('body',(8,44),[('A',(24,37),16,7,True),('A',(40,44),16,7,True)])
        self.relate('connect','hair','face');self.relate('connect','face','body')
        path('smile',(22,22),[('C',(26,22),(23,25),(25,25))])
