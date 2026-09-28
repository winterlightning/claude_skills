"""Revision of mobile-phone-control-play. Enlarged the play control and moved the lower band to retain a clean opening and equal screen margins.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""mobile-phone-control-play: Balanced phone and play mark; earlier revisions preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd0012287-f904-4bd1-be94-369aca27d22a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-control-play/20260927T074149Z-thuan-mac-1/reference/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.svg'
AUTHOR = 'gpt-6'

class MobilePhoneControlPlay(Solo48):
    icon_id = 'mobile-phone-control-play'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('solo-ai-full-set', 'mobile-phone-control-play')

    def build(self):
        # Plan: Keep the inset play triangle and lower phone band; ensure the triangle opening and margins remain clear.
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
        path('phone',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,36)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,36)),('L',(8,8)),('A',(12,4),4,4,True)],True)
        line('band',(8,36),(40,36));join('band','phone');poly('play',(17,13),(31,20),(17,27),closed=True)
