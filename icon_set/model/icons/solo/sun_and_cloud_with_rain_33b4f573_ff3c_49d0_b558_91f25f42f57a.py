"""Sun and Cloud with Rain
Plan: Cloud obscuring upper-right sun with three diagonal rain strokes.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide cloud-rain: rounded cloud and separate rain series.
Reduction: Sun rays omitted; circular sun arc behind cloud and three diagonal rain strokes retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33b4f573-ff3c-49d0-b558-91f25f42f57a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cloud sun rain_33b4f573-ff3c-49d0-b558-91f25f42f57a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-and-cloud-with-rain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sun', 'cloud', 'rain', 'weather', 'showers', 'rays', 'sky')

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
        path('cloud',(14,32),[('A',(6,24),8,8,True),('A',(14,16),8,8,True),('C',(22,16),(14,8),(20,8)),('C',(32,26),(30,16),(32,20)),('C',(38,28),(38,26),(38,28)),('C',(32,32),(38,31),(35,32)),('L',(14,32))],True)
        path('sun',(22,16),[('A',(32,6),10,10,True),('A',(42,16),10,10,True),('A',(32,26),10,10,True)]);join('sun','cloud')
        for x in (16,26,36):line(f'rain-{x}',(x,40),(x-2,42))
