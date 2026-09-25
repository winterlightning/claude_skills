'upholstered-seat-with-rounded-arms. Plan: Rounded sofa back over arms and seat; symmetric paired legs. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide sofa: shared arm and cushion attachments. Reduction: Simplify upholstered seams; keep back, thick arms, seat and legs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90825dee-e89b-4c78-8159-2db11221eb76'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/couch_90825dee-e89b-4c78-8159-2db11221eb76.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upholstered-seat-with-rounded-arms'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('seat', 'sofa', 'armchair', 'furniture', 'cushion', 'living', 'upholstery')

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
        path('back',(8,24),[('L',(8,12)),('A',(12,8),4,4,True),('L',(36,8)),('A',(40,12),4,4,True),('L',(40,24))])
        path('seat',(4,24),[('L',(4,36)),('L',(44,36)),('L',(44,24))])
        for x in (8,40):
         self.add_line(f'arm-{x}',(x-4,24),(x+4,24));self.relate('connect','back',f'arm-{x}');self.relate('connect','seat',f'arm-{x}')
        self.add_line('cushion',(12,24),(36,24))
        for x in (12,36):self.relate('connect','cushion',f'arm-{8 if x==12 else 40}')
        for x in (8,40):
         self.add_line(f'leg-{x}',(x,36),(x,40));self.relate('connect','seat',f'leg-{x}')
