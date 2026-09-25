"""Egg in Egg Cup.

Plan: Mirrored egg curves join a shallow bowl at rim endpoints. Centerline bounds (8,4)-(40,44). Drop the tiny rear-rim wedges only.
Construction: Lucide egg: paired smooth shoulders and an upright egg silhouette. Supplied reference owns the shallow cup and visible front rim.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef39387f-49aa-432d-8652-29f06f702f1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/egg 1_ef39387f-49aa-432d-8652-29f06f702f1c.svg'
AUTHOR = "gpt-6"

class Batch02Icon9(Solo48):
    icon_id = 'egg-in-egg-cup-ef39387f'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('egg-in-egg-cup',)
    keywords = ('egg', 'in', 'egg', 'cup')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for i, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{i}"
                if kind == "L": self.add_line(member, here, end)
                elif kind == "A": self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == "C": self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        axis=24
        path("egg",(12,29),[("C",(axis,4),(10,18),(20,4)),("C",(36,29),(28,4),(38,18))])
        path("cup",(8,28),[("C",(12,29),(9,28),(10,29)),("C",(axis,32),(16,31),(20,32)),("C",(36,29),(28,32),(32,31)),("C",(40,28),(38,29),(39,28)),("C",(axis,44),(40,38),(34,44)),("C",(8,28),(14,44),(8,38))],True)
        self.relate("connect","egg","cup")
