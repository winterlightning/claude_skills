"""Three distinct curved hooks form a triangular webhook mark, with open gaps that preserve the reference's three-part topology at 48 pixels."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "e6758494-42bf-4f9d-b4a8-0893ebe568ab"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__webhook-triangle/20260926T171117Z-thuan-mac-1/reference/web hook_e6758494-42bf-4f9d-b4a8-0893ebe568ab.svg"
AUTHOR = "gpt-6"
class WebhookTriangle(Solo48):
    icon_id="webhook-triangle"
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="programing"
    aliases=()
    keywords=("webhook", "hook", "api", "integration", "callback", "event")
    def build(self):
        # Three open rounded hooks occupy the vertices of the reference triangle.
        self.add_arc("upper-hook",(14,16),(34,16),radius_x=10,sweep=True)
        self.add_line("upper-left-tail",(14,16),(14,22))
        self.add_line("upper-right-tail",(34,16),(34,22))
        self.add_arc("lower-left-hook",(6,36),(18,36),radius_x=6,sweep=False)
        self.add_line("lower-left-tail",(18,36),(22,36))
        self.add_arc("lower-right-hook",(36,30),(36,42),radius_x=6,sweep=True)
