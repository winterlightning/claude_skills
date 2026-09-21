"""Tiered Cruise Ship on Water
Plan: Front-facing stepped ship over symmetric wave
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide ship bow silhouette.
Reduction: Reduce three decks to two wide tiers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84ebedc4-65c8-4f16-9d81-cbc3c1bea7ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cruise liner_84ebedc4-65c8-4f16-9d81-cbc3c1bea7ca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tiered-cruise-ship-on-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ship', 'cruise', 'boat', 'vessel', 'water', 'deck', 'travel')

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
        path('hull',(6,26),[('L',(24,20)),('L',(42,26)),('L',(36,42)),('C',(24,38),(32,42),(28,38)),('C',(12,42),(20,38),(16,42)),('L',(6,26))],True)
        path('decks',(12,24),[('L',(12,14)),('L',(18,14)),('L',(18,6)),('L',(30,6)),('L',(30,14)),('L',(36,14)),('L',(36,24))]);self.relate('connect','decks','hull')
        self.add_line('bow',(24,20),(24,38));self.relate('connect','bow','hull')

# Final review: Two deck tiers and wave-shaped lower hull edge replace three crowded tiers and a separate wave line.
