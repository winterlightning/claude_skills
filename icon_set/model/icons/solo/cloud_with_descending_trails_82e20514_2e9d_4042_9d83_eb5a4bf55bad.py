'cloud-with-descending-trails. Plan: Open asymmetric cloud and three trails, middle broken. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide cloud: coherent lobe contour. Reduction: Shortened outside trails to keep them separate from the cloud; retained broken central trail.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82e20514-2e9d-4042-9d83-eb5a4bf55bad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon cloudtrail 2_82e20514-2e9d-4042-9d83-eb5a4bf55bad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-with-descending-trails'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cloud', 'trail', 'stream', 'vertical', 'computing', 'flow', 'weather')

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
        path('cloud',(10,26),[('C',(4,18),(6,25),(4,22)),('C',(18,8),(4,10),(10,8)),('C',(32,14),(26,8),(30,10)),('C',(44,20),(40,12),(44,16)),('C',(38,26),(44,24),(42,26))])
        for x in (14,34):self.add_line(f'trail-{x}',(x,34),(x,40))
        self.add_line('middle-top',(24,22),(24,28));self.add_line('middle-bottom',(24,36),(24,40))
