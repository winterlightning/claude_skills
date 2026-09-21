'cloud-raining-three-hearts. Plan: Open lower cloud above three hearts in a triangular rain arrangement. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Lucide cloud: smooth lobe silhouette. Reduction: Kept three heart drops, adjusted their triangular spacing, and simplified the cloud lobes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '195089c0-03ce-4628-baa5-28ba2428e9e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/love cloud_195089c0-03ce-4628-baa5-28ba2428e9e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-raining-three-hearts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cloud', 'hearts', 'rain', 'love', 'drops', 'weather', 'affection')

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
        path('cloud',(10,24),[('C',(6,16),(6,24),(6,20)),('C',(16,12),(6,12),(10,10)),('C',(24,6),(16,8),(20,6)),('C',(34,12),(30,6),(34,8)),('C',(42,18),(40,10),(42,14)),('C',(38,24),(42,22),(40,24))])
        for i,(x,y) in enumerate([(24,21),(12,34),(36,34)]):
         path(f'heart-{i}',(x,y+8),[('L',(x-4,y+4)),('C',(x,y),(x-8,y-2),(x-2,y-2)),('C',(x+4,y+4),(x+2,y-2),(x+8,y-2)),('L',(x,y+8))],True)
