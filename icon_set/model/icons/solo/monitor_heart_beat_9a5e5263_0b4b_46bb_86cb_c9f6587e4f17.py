"""monitor-heart-beat: Smooth heart pulse; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a5e5263-0b4b-46bb-86cb-c9f6587e4f17'
SOURCE_PATH = 'icons-json/health/monitor heart beat_9a5e5263-0b4b-46bb-86cb-c9f6587e4f17.json'
AUTHOR = 'gpt-6'

class MonitorHeartBeat(Solo48):
    icon_id = 'monitor-heart-beat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('solo-ai-full-set', 'monitor-heart-beat')

    def build(self):
        # Plan: Preserve the heart and single waveform. An open shared baseline and broad central pulse avoid a cramped return along the heart wall.
        # Reference: Lucide heart-crack: original and atomic-debug geometry.

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
        path('heart',(24,10),[('C',(15,6),(21,7),(19,6)),('C',(6,17),(9,6),(6,10)),('C',(10,27),(6,21),(8,24)),('C',(24,42),(14,33),(20,39)),('C',(38,27),(28,39),(34,33)),('C',(42,17),(40,24),(42,21)),('C',(33,6),(42,10),(39,6)),('C',(24,10),(29,6),(27,7))],True)
        path('pulse',(6,27),[('L',(10,27)),('L',(16,27)),('L',(21,17)),('L',(24,30)),('L',(28,27)),('L',(38,27)),('L',(42,27))]);join('pulse','heart')
