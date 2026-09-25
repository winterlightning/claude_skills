"""Grandmother with Grandchild.
Plan: Grandmother at right in a flared garment beside a smaller child and rightmost cane. Adult head r4 bottom12 to garment neck20; child r3 bottom23 to torso31. Extrema (8,4)-(40,44).
Reference: human_ref/full_body_ref.png: circular head and simple flared dress; Lucide person-standing supports child joints.
Reduction: Bun and neckline detail omitted; dress, cane and smaller child retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a8b2e9d-c6ea-4644-97ea-81d212599726'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/family/family grandmother_6a8b2e9d-c6ea-4644-97ea-81d212599726.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'grandmother-grandchild-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "family"
    aliases = ()
    keywords = ('grandmother', 'with', 'grandchild')

    def build(self):

        for name,x,y,r in (('adult',26,8,4),('child',12,20,3)):
            self.add_arc(f'{name}-head-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(f'{name}-head-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(f'{name}-head',f'{name}-head-a',f'{name}-head-b',closed=True)
        self.add_polyline('adult-torso',(26,20),(20,34),(24,34),(32,34),(32,30),(26,20))
        for i,x in enumerate((24,32)):
            self.add_line(f'adult-leg-{i}',(x,34),(x,44))
            self.relate('connect',f'adult-leg-{i}','adult-torso')
        self.add_line('child-torso',(12,31),(12,38))
        self.add_polyline('child-legs',(8,44),(12,38),(16,44));self.relate('connect','child-torso','child-legs')
        self.add_line('cane-stem',(40,30),(40,44))
        self.add_arc('cane-hook',(32,30),(40,30),radius_x=4)
        self.relate('connect','cane-stem','cane-hook')
        self.relate('connect','adult-torso','cane-hook')
        for name in ('adult','child'):self.mark_human_figure(name,head=f'{name}-head',torso='adult-torso-1' if name=='adult' else 'child-torso',torso_junction='start')
