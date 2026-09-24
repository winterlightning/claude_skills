'coffee-cup-with-falling-sugar-cubes. Plan: Broad cup with left loop and two falling sugar cubes. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Lucide coffee: handle connected to cup; square repeated sugar. Reduction: Omit small rim marks, retain two square cubes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21a74246-6bc9-4eeb-abee-faaebe33d167'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon corretto_21a74246-6bc9-4eeb-abee-faaebe33d167.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'coffee-cup-with-falling-sugar-cubes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('coffee', 'cup', 'sugar', 'cubes', 'drink', 'handle', 'beverage')

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
        rect('sugar-left',18,6,8,8);rect('sugar-right',34,13,8,8)
        path('cup',(16,30),[('L',(42,30)),('A',(29,42),13,12,True),('A',(16,30),13,12,True)],True)
        path('handle',(16,30),[('L',(12,30)),('A',(6,36),6,6,False),('A',(12,42),6,6,False),('L',(20,42))]);self.relate('connect','cup','handle')
