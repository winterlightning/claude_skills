"""Symmetric supported gymnast, circular head and minimal body from human_ref. VRECT_L tall supports. Head center (24,8), radius4, torso junction(24,20): exact 4 ink gap.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e406d94-3472-495a-b48a-7dc0d21a13ed'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/gymnastics acrobatic hanging person_3e406d94-3472-495a-b48a-7dc0d21a13ed.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'gymnast-supported-on-horizontal-bar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "primitives-generate"
    aliases = ('Gymnast on Horizontal Bar',)
    keywords = ('gymnast', 'supported', 'on', 'horizontal', 'bar')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        circle('head',24,8,4)
        line('post-left',(8,4),(8,20))
        line('post-left-lower',(8,20),(8,44))
        line('post-right',(40,4),(40,20))
        line('post-right-lower',(40,20),(40,44))
        line('bar-left',(8,20),(24,20))
        line('bar-right',(24,20),(40,20))
        line('torso',(24,20),(24,32))
        line('leg-left',(24,32),(16,44))
        line('leg-right',(24,32),(32,44))
        join('post-left','post-left-lower','bar-left')
        join('post-right','post-right-lower','bar-right')
        join('bar-left','bar-right','torso')
        join('torso','leg-left','leg-right')
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
