"""explosion-sound-effect-text: Balanced explosion burst; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5f2ba451-650e-406e-a2e4-faf0686c7ce1'
SOURCE_PATH = 'pictographic-primitives/video-games/explosion sound effect text_5f2ba451-650e-406e-a2e4-faf0686c7ce1.svg'
AUTHOR = 'gpt-6'

class ExplosionSoundEffectText(Solo48):
    icon_id = 'explosion-sound-effect-text'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('solo-ai-full-set', 'explosion-sound-effect-text')

    def build(self):
        # Plan: Preserve the rising pointed blast and low baseline. Broader asymmetrical rays keep their identity without cramped slivers.
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
        path('burst',(14,42),[('L',(6,24)),('L',(17,29)),('L',(15,13)),('L',(24,22)),('L',(28,6)),('L',(33,24)),('L',(42,19)),('L',(35,34)),('L',(31,42))])
        path('base',(10,42),[('L',(14,42)),('L',(31,42)),('L',(38,42))]);join('base','burst')
