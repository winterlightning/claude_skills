"""Binoculars with Large Front Lenses.

Plan: HRECT centerlines (4,8)-(44,40); matched tapered barrels, radius-7 front lenses, radius-5 eyepiece caps and a high bridge.
Construction references: Lucide binoculars: mirrored barrels and shared bridge; supplied source owns the large circular front lenses.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '0b4295f2-6501-477e-8a02-cfc25042f30e'
SOURCE_PATH = 'pictographic-primitives/business/binoculars_0b4295f2-6501-477e-8a02-cfc25042f30e.svg'
SOURCE_ICON_IDS = ('0b4295f2-6501-477e-8a02-cfc25042f30e',)
SOURCE_PATHS = ('pictographic-primitives/business/binoculars_0b4295f2-6501-477e-8a02-cfc25042f30e.svg',)
AUTHOR = 'gpt-6'


class BinocularsWithLargeFrontLenses(Solo48):
    icon_id = 'binoculars-with-large-front-lenses'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('binoculars', 'with', 'large', 'front', 'lenses')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        axis,lens_offset,lens_radius=24,13,7
        for side in (-1,1):
            x=lambda offset:axis+side*offset
            k=f"barrel-{side}"
            # Reflection reverses sweep while retaining the same contour traversal.
            path(k,(x(20),33),[("C",(x(16),13),(x(20),24),(x(16),20)),("A",(x(6),13),5,5,side<0),("L",(x(6),16)),("L",(x(6),33))])
            # Cardinal lens endpoints coincide with the barrel walls.
            path(f"lens-{side}",(x(20),33),[("A",(x(6),33),lens_radius,lens_radius,True),("A",(x(20),33),lens_radius,lens_radius,True)],True)
            self.relate("connect",k,f"lens-{side}")
        self.add_line("bridge",(18,16),(30,16))
        for side in (-1,1): self.relate("connect","bridge",f"barrel-{side}")
