"""A branching revision graph beside an open panel containing a code mark."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "e3ffb6e8-3bc2-43d5-82fe-ae251b7b7f41"
SOURCE_PATH = "pictographic-primitives/_uncategorized_02/amazon web service code commit_e3ffb6e8-3bc2-43d5-82fe-ae251b7b7f41.svg"
AUTHOR = "gpt-5"


class CodeVersionControlAndBranching(Solo48):
    icon_id = "code-version-control-and-branching"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/development"
    aliases = ("code-commit", "version-control-code-panel")
    keywords = ("code", "git", "branch", "commit", "revision", "panel")

    def build(self) -> None:
        # Plan: the left graph owns a three-node vertical series and one branch
        # node leading to an upper-left arrow. The right panel is an open rounded
        # contour hosting a single continuous </>-like code stroke.
        chain_nodes = ((4, 8), (4, 22), (4, 36))
        self.add_line("chain-upper", chain_nodes[0], chain_nodes[1])
        self.add_line("chain-lower", chain_nodes[1], chain_nodes[2])
        for index, node in enumerate(chain_nodes):
            dot = f"chain-node-{index}"
            self.add_dot(dot, node)
            if index > 0:
                self.relate("connect", f"chain-{'upper' if index == 1 else 'lower'}", dot)
            if index < 2:
                self.relate("connect", f"chain-{'upper' if index == 0 else 'lower'}", dot)

        branch_node = (14, 22)
        self.add_polyline("branch-path", chain_nodes[2], (10, 28), branch_node)
        self.add_dot("branch-node", branch_node)
        self.relate("connect", "branch-path", "chain-node-2")
        self.relate("connect", "branch-path", "branch-node")

        self.add_line("branch-arrow-shaft", branch_node, (12, 14))
        self.add_line("branch-arrow-horizontal", (12, 14), (18, 14))
        self.add_line("branch-arrow-vertical", (12, 14), (12, 8))
        self.relate("connect", "branch-arrow-shaft", "branch-node")
        self.relate("connect", "branch-arrow-shaft", "branch-arrow-horizontal")
        self.relate("connect", "branch-arrow-shaft", "branch-arrow-vertical")

        self.add_line("panel-top", (38, 14), (40, 14))
        self.add_arc("panel-top-right", (40, 14), (44, 18), radius_x=4)
        self.add_line("panel-right", (44, 18), (44, 36))
        self.add_arc("panel-bottom-right", (44, 36), (40, 40), radius_x=4)
        self.add_line("panel-bottom", (40, 40), (22, 40))
        self.add_arc("panel-bottom-left", (22, 40), (18, 36), radius_x=4)
        self.add_contour(
            "code-panel",
            "panel-top",
            "panel-top-right",
            "panel-right",
            "panel-bottom-right",
            "panel-bottom",
            "panel-bottom-left",
        )

        self.add_polyline(
            "code-mark",
            (26, 22),
            (22, 27),
            (26, 31),
            (30, 20),
            (34, 27),
            (30, 31),
        )
