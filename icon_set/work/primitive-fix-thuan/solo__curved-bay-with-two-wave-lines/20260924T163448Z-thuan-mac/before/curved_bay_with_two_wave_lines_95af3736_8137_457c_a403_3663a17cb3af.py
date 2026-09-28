'curved-bay-with-two-wave-lines. Plan: Coast curves into inlet with two interior wave lines. Keyshape: HRECT_M, exact SOLO48 bounds. Construction: Lucide wind: smooth separate curves. Reduction: Opened the coast at the upper right; reduced the wave amplitudes and shortened the upper wave.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95af3736-8137-457c-a403-3663a17cb3af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bay_95af3736-8137-457c-a403-3663a17cb3af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-bay-with-two-wave-lines'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bay', 'coast', 'shoreline', 'waves', 'water', 'sea', 'inlet')

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
        path('coast',(44,10),[('C',(40,14),(42,10),(40,12)),('L',(40,22)),('L',(32,22)),('C',(24,14),(28,22),(28,14)),('L',(12,10)),('L',(8,10)),('A',(4,14),4,4,False),('L',(4,24)),('C',(18,38),(4,32),(10,38)),('L',(30,38)),('C',(44,24),(38,38),(44,32)),],False)
        path('wave1',(13,20),[('C',(16,20),(14,19),(15,21))]);path('wave2',(16,29),[('C',(26,29),(19,28),(23,30))])
