"""chef-gear-biscuits-cup: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd099f5d7-fdcf-4570-9c86-6f33e85e4e5f'
SOURCE_PATH = 'pictographic-primitives/food/chef gear biscuits cup_d099f5d7-fdcf-4570-9c86-6f33e85e4e5f.svg'
AUTHOR = 'gpt-6'

class ChefGearBiscuitsCup(Solo48):
    icon_id = 'chef-gear-biscuits-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('chef', 'gear', 'biscuits', 'cup', 'food', 'solo-ai-next100')

    def build(self):
        # Plan: A wide cup holds two rounded biscuit sticks. Exact attachment nodes keep the biscuits visibly seated in the rim.
        # Reference: Lucide cup-soda original and atomic-debug construction.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        path('cup',(6,22),[('L',(14,22)),('L',(24,22)),('L',(34,22)),('L',(42,22)),('L',(42,36)),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,22))],True)
        path('left-biscuit',(14,22),[('L',(8,12)),('C',(10,6),(6,8),(8,6)),('C',(17,9),(13,6),(16,6)),('L',(24,22))]);join('left-biscuit','cup')
        path('right-biscuit',(24,22),[('L',(31,9)),('C',(38,6),(32,6),(35,6)),('C',(40,12),(40,6),(42,8)),('L',(34,22))]);join('right-biscuit','cup');join('left-biscuit','right-biscuit')
