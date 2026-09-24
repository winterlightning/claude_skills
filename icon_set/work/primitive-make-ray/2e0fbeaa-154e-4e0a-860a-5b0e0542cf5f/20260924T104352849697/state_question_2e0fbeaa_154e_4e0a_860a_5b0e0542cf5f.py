from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "2e0fbeaa-154e-4e0a-860a-5b0e0542cf5f"
SOURCE_PATH = "icon_set/work/todo-references/state question_2e0fbeaa-154e-4e0a-860a-5b0e0542cf5f.svg"
AUTHOR = "gpt-6"
class StateQuestion(Solo48):
    """A circular help badge containing a question mark."""
    icon_id = "state-question"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbol"
    aliases = ("help", "question circle")
    keywords = ("question", "support", "unknown")
    def build(self):
        # Circle owns a compact circular hook and detached dot; x-axis24.
        # Radius20 envelope gives visible radial radius22 around (24,24).
        axis,r=24,20
        self.add_arc("ring-top",(axis-r,24),(axis+r,24),radius_x=r)
        self.add_arc("ring-bottom",(axis+r,24),(axis-r,24),radius_x=r)
        self.add_contour("ring","ring-top","ring-bottom",closed=True)
        hook_r=6
        self.add_arc("hook-top",(axis-hook_r,20),(axis+hook_r,20),radius_x=hook_r)
        self.add_arc("hook-return",(axis+hook_r,20),(axis,26),radius_x=hook_r)
        self.add_contour("hook","hook-top","hook-return")
        self.add_dot("point",(axis,35))
