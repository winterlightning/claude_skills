"""Sun Appearing Behind Rounded Hill
Plan: Rising sun partly hidden behind smooth hill.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Hill flattened to leave a clear sun opening; three primary rays retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9209ad15-ccc6-48e1-b297-b65ddf79ec66'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/day noon_9209ad15-ccc6-48e1-b297-b65ddf79ec66.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-appearing-behind-rounded-hill'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sun', 'hill', 'sunrise', 'landscape', 'rays', 'horizon', 'morning')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('hill',(4,40),[('C',(12,32),(6,36),(9,34)),('C',(24,30),(16,30),(20,30)),('C',(36,32),(28,30),(32,30)),('C',(44,40),(39,34),(42,36)),('L',(4,40))],True)
        path('sun',(12,32),[('A',(36,32),12,12,True)]);join('sun','hill')
        line('ray-top',(24,8),(24,12));line('ray-left',(5,19),(7,21));line('ray-right',(41,21),(43,19))
