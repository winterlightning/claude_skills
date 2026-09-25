"""Smiling Devil Bust with Curved Horns
Plan: Round devil head with two curved horns, smile and shoulders.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: human_ref/user.svg: circular face and curved shoulders; avatar ink contact.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '722cf62b-3e5b-4580-98b4-5e0213fb8c7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/demon_722cf62b-3e5b-4580-98b4-5e0213fb8c7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-devil-bust-with-curved-horns'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('devil', 'horns', 'smile', 'bust', 'face', 'creature', 'portrait')

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
        from ._base import HEAD_BODY_CENTERLINE_GAP
        circle('head',24,22,12)
        path('body',(8,44),[('A',(24,38),16,6,True),('A',(40,44),16,6,True)])
        self.relate('connect','head','body')
        for s in (-1,1):path(f'horn-{s}',(24+s*8,13),[('C',(24+s*14,4),(24+s*11,11),(24+s*13,8)),('C',(24+s*12,22),(24+s*17,15),(24+s*15,18))]);self.relate('connect',f'horn-{s}','head')
        path('smile',(21,22),[('C',(27,22),(23,25),(25,25))])
