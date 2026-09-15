"""chef-gear-cookie-bowl: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47c59a46-f46e-420a-b3f5-7db2c1a091f0'
SOURCE_PATH = 'icons-json/food/chef gear cookie bowl_47c59a46-f46e-420a-b3f5-7db2c1a091f0.json'
AUTHOR = 'gpt-6'

class ChefGearCookieBowl(Solo48):
    icon_id = 'chef-gear-cookie-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chef', 'gear', 'cookie', 'bowl', 'food', 'solo-ai-next100')

    def build(self):
        # Plan: A bitten cookie rises from a broad shallow bowl. One readable bite replaces the crowded cluster of small scallops.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        path('bowl',(6,25),[('L',(10,25)),('L',(38,25)),('L',(42,25)),('C',(34,36),(41,30),(37,34)),('L',(34,42)),('L',(14,42)),('L',(14,36)),('C',(6,25),(11,34),(7,30))],True)
        path('cookie',(10,25),[('C',(26,6),(8,12),(18,6)),('C',(38,17),(25,13),(31,17)),('L',(38,25))]);join('cookie','bowl')
