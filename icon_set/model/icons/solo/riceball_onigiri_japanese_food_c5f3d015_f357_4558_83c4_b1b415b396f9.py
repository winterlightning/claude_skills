"""riceball-onigiri-japanese-food: Rounded rice ball with centered wrap; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c5f3d015-f357-4558-83c4-b1b415b396f9'
SOURCE_PATH = 'icons-json/video-games/riceball onigiri japanese food_c5f3d015-f357-4558-83c4-b1b415b396f9.json'
AUTHOR = 'gpt-6'

class RiceballOnigiriJapaneseFood(Solo48):
    icon_id = 'riceball-onigiri-japanese-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('solo-ai-full-set', 'riceball-onigiri-japanese-food')

    def build(self):
        # Plan: Preserve the triangular rice ball and dark-wrap outline; give the wrap clear room below the shoulders.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        path('rice',(24,8),[('C',(32,15),(28,8),(30,12)),('L',(41,28)),('C',(44,34),(43,31),(44,32)),('C',(38,40),(44,38),(42,40)),('L',(30,40)),('L',(18,40)),('L',(10,40)),('C',(4,34),(6,40),(4,38)),('C',(7,28),(4,32),(5,31)),('L',(16,15)),('C',(24,8),(18,12),(20,8))],True)
        path('wrap',(18,40),[('L',(18,28)),('L',(30,28)),('L',(30,40))]);join('wrap','rice')
