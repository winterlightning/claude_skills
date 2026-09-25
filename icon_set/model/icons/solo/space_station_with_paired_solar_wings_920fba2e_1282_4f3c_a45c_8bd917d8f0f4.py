"""Space Station with Paired Solar Wings
Plan: Central station and raised module with symmetric paneled solar wings.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide satellite: shared attachments between core and panels.
Reduction: Wing divisions simplified to three horizontal cells."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '920fba2e-1282-4f3c-a45c-8bd917d8f0f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/space station_920fba2e-1282-4f3c-a45c-8bd917d8f0f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'space-station-with-paired-solar-wings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('space station', 'solar panels', 'spacecraft', 'module', 'orbit', 'structure')

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
        for x in (4,36):
         rect(f'wing-{x}',x,12,8,28)
         for y in (22,31):self.add_line(f'row-{x}-{y}',(x,y),(x+8,y));self.relate('connect',f'row-{x}-{y}',f'wing-{x}')
        rect('core',20,24,8,16);rect('upper',20,8,8,8)
        self.add_line('spine',(24,16),(24,24));self.relate('connect','spine','upper');self.relate('connect','spine','core')
        for x in (12,28):self.add_line(f'link-{x}',(x,32),(x+8,32))
        self.relate('connect','link-12','wing-4');self.relate('connect','link-12','core');self.relate('connect','link-28','core');self.relate('connect','link-28','wing-36')
