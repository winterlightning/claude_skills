"""microphone-karaoke: Smooth microphone and cable; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ae391a9-9356-50c7-bd0a-64b441bf643b'
SOURCE_PATH = 'icons-json/audio/microphone karaoke_5ae391a9-9356-50c7-bd0a-64b441bf643b.json'
AUTHOR = 'gpt-6'

class MicrophoneKaraoke(Solo48):
    icon_id = 'microphone-karaoke'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('solo-ai-full-set', 'microphone-karaoke')

    def build(self):
        # Plan: Preserve the diagonal circular microphone, broad handle and cable curl, using shared head attachments.
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
        path('head',(18,15),[('A',(29,4),11,11,True),('A',(40,15),11,11,True),('A',(29,26),11,11,True),('A',(18,15),11,11,True)],True)
        path('handle',(18,15),[('L',(8,32)),('C',(12,38),(8,35),(8,38)),('L',(29,26))]);join('handle','head')
        path('cable',(12,38),[('C',(12,44),(8,38),(8,44)),('L',(28,44))]);join('cable','handle')
