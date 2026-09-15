"""vr-headset: Smooth headset profile; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '333b76cc-b37e-568d-8fc3-aa0f76f2f559'
SOURCE_PATH = 'icons-json/video-games/vr headset_333b76cc-b37e-568d-8fc3-aa0f76f2f559.json'
AUTHOR = 'gpt-6'

class VrHeadset(Solo48):
    icon_id = 'vr-headset'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('solo-ai-full-set', 'vr-headset')

    def build(self):
        # Plan: Human reference: user.svg and full_body_ref.png. Preserve the continuous neck, visor and shared strap. Every connection is split at an exact endpoint.
        # Reference: Lucide headset: original and atomic-debug geometry.

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
        path('head',(15,44),[('L',(15,37)),('C',(8,20),(11,32),(8,27)),('A',(24,4),16,16,True),('C',(35,12),(30,4),(34,8))])
        path('visor',(28,12),[('L',(35,12)),('L',(40,12)),('L',(40,24)),('L',(35,24)),('L',(28,24)),('A',(22,18),6,6,True),('A',(28,12),6,6,True)],True);join('head','visor')
        path('strap',(8,20),[('L',(22,18))]);join('strap','head');join('strap','visor')
        path('profile',(35,24),[('L',(37,32)),('L',(32,32)),('L',(32,37)),('L',(25,39)),('L',(25,44))]);join('profile','visor')
