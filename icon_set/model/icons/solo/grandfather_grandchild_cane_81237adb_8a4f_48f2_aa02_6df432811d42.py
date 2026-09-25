"""Grandfather and Grandchild.
Plan: Older adult at left holds a cane beside a shorter child. Shared human circles and detached torso gaps: adult r4 bottom12 to neck20; child r3 bottom23 to neck31. Extrema (8,4)-(40,44).
Reference: human_ref/full_body_ref.png: circular heads, upright torso and simple legs. Lucide person-standing supports the shared junctions.
Reduction: Hairline and outlined garments omitted; cane and relative stature carry the family scene. The adult has a slightly asymmetric stance beside the cane.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81237adb-8a4f-48f2-aa02-6df432811d42'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/family/family grandfather_81237adb-8a4f-48f2-aa02-6df432811d42.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'grandfather-grandchild-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "family"
    aliases = ()
    keywords = ('grandfather', 'and', 'grandchild')

    def build(self):

        for name,x,y,r,neck in (('adult',20,8,4,20),('child',36,20,3,31)):
            self.add_arc(f'{name}-head-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(f'{name}-head-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(f'{name}-head',f'{name}-head-a',f'{name}-head-b',closed=True)
            hip=34 if name=='adult' else 38
            if name=='adult':self.add_polyline(f'{name}-torso',(x,neck),(x,24),(x,hip))
            else:self.add_line(f'{name}-torso',(x,neck),(x,hip))
            self.add_polyline(f'{name}-legs',(x-3 if name=='adult' else x-4,44),(x,hip),(x+4,44))
            self.relate('connect',f'{name}-torso',f'{name}-legs')
            self.mark_human_figure(name,head=f'{name}-head',torso=f'{name}-torso-1' if name=='adult' else f'{name}-torso',torso_junction='start')
        self.add_line('cane-stem',(8,44),(8,28))
        self.add_arc('cane-hook',(8,28),(12,28),radius_x=2)
        self.add_contour('cane','cane-stem','cane-hook')
        self.add_line('arm',(20,24),(12,28))
        self.relate('connect','arm','adult-torso');self.relate('connect','arm','cane')
