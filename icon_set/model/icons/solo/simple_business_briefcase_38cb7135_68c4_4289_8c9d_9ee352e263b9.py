"""Briefcase.

Plan: Shared radius4 corners; handle endpoints split the body top. Centerline bounds (4,8)-(44,40).
Construction: Lucide briefcase-business: tangent rounded case and handle; omit its flap to retain the supplied blank front.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38cb7135-68c4-4289-8c9d-9ee352e263b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/case_38cb7135-68c4-4289-8c9d-9ee352e263b9.svg'
AUTHOR = 'gpt-6'

class Batch02Icon0(Solo48):
    icon_id = 'simple-business-briefcase-38cb7135'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('simple-business-briefcase',)
    keywords = ('simple', 'business', 'briefcase', 'sub icon')

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
        path("body",(8,16),[("L",(16,16)),("L",(32,16)),("L",(40,16)),("A",(44,20),4,4,True),("L",(44,36)),("A",(40,40),4,4,True),("L",(8,40)),("A",(4,36),4,4,True),("L",(4,20)),("A",(8,16),4,4,True)],True)
        path("handle",(16,16),[("L",(16,12)),("A",(20,8),4,4,True),("L",(28,8)),("A",(32,12),4,4,True),("L",(32,16))])
        self.relate("connect","body","handle")


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('e756308e-0744-49f8-9b09-d1933550ea61', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/briefcase_e756308e-0744-49f8-9b09-d1933550ea61.svg')]
