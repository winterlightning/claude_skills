"""hand-holding-document (redraw of the new-pipeline traced SVG).

Plan: an upright blank page standing on a flat open hand that enters from
the left; a broad thumb lies over the page's lower-left corner. SQUARE,
centerline box (6,6)-(42,42).
- document: one open rounded-rectangle contour (x 12..35, y 6..32, corner
  r 2) that starts where the thumb's top edge crosses its left wall (12,30),
  runs round the top and right, and lands on the hand at (35,32). Its bottom
  edge is the hand's top edge (the page stands in the palm).
- hand: one open contour. The wrist's top edge (6,33) bends tangentially
  into the thumb's top edge (direction (3,-4)); the thumb is a capsule 10
  wide on centerlines with a semicircular tip r 5 about (22,25); its
  underside drops to the page bottom at (23,32); the grip line runs right
  under the page to (37,32), the fingertips curl round a r 5 semicircle
  about (37,37), and the palm underside runs back to the wrist at (6,42).
Extremes: x=6 wrist, y=6 page top, x=42 fingertips, y=42 palm/wrist.
The single-stroke palm and fingertip bump stand in for the fingers (dropped:
they merge at 48 px).

Metric issues (hand-holding-document_metrics.json):
- stroke-width (info, trace 2.77 fitted): fixed, redrawn at stroke 4; every
  gap re-budgeted (thumb 10 wide, tip >= 8 from the page's right wall, grip
  line to palm 10, wrist 9 wide).
- no-head (warn): not applicable, not repaired. The subject is a hand only,
  not a figure, so there is no head to trace; adding one would change the
  subject. No mark_human_figure call for the same reason.
- junctions e0/e1 at the thumb and at the page's bottom-right: kept as exact
  shared nodes (12,30) and (35,32) inside one hand/document connect.
- clearance e0/e1 (7.44 ink, ok) and hole (15.6, ok): preserved; the page
  opening stays >= 8 on centerlines round the thumb tip.
Reference: Lucide `hand-helping` / `hand-coins` (open wrist edges, palm
curve under the held object) and `file` (upright page, corner r 2). The hand
is deliberately asymmetric (it enters from the left).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1a5b8e57-e476-5e0e-a43f-45bc8105f4e5"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1257-hand-holding-document/hand-holding-document_raw.svg"
AUTHOR = "claude-opus-5-5"

# Document: upright rounded rectangle; its bottom edge is the hand's top edge.
DOC_L, DOC_T, DOC_R, DOC_B, DOC_RAD = 12, 6, 35, 32, 2
# Thumb: capsule along direction (3,-4), tip radius 5 about TIP_C, so its
# edges sit 10 apart and leave the tip at -/+(4,3).
TIP_C, TIP_R = (22, 25), 5
THUMB_DIR = (3, -4)
GRIP = (12, 30)            # thumb top edge crosses the document's left wall
THUMB_FOOT = (23, 32)      # thumb underside lands on the document bottom
WRIST_TOP = (6, 33)        # hand top edge leaves the canvas box horizontally
PAD_C, PAD_R = (37, 37), 5  # fingertips curl round the document's bottom-right
WRIST_LOW = (6, 42)        # palm underside end


class HandHoldingDocumentRedraw(Solo48):
    icon_id = "hand-holding-document-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "documents"
    aliases = ("hand-holding-paper", "document-in-hand")
    keywords = ("document", "paper", "page", "file", "hand", "holding", "give", "submit", "contract")

    def build(self) -> None:
        cx, cy = TIP_C
        dx, dy = THUMB_DIR
        tip_top = (cx - 4, cy - 3)
        tip_low = (cx + 4, cy + 3)
        pad_top = (PAD_C[0], PAD_C[1] - PAD_R)
        pad_low = (PAD_C[0], PAD_C[1] + PAD_R)

        # Hand: wrist top -> thumb top -> tip -> underside -> document bottom -> fingertips -> palm.
        gx, gy = GRIP
        wx, wy = WRIST_TOP
        self.add_bezier("wrist-top", WRIST_TOP, ((wx + 3, wy), (gx - 0.7 * dx, gy - 0.7 * dy), GRIP))
        self.add_line("thumb-top", GRIP, tip_top)
        self.add_arc("thumb-tip", tip_top, tip_low, radius_x=TIP_R, sweep=True)
        self.add_line("thumb-under", tip_low, THUMB_FOOT)
        doc_foot = (DOC_R, DOC_B)
        self.add_line("grip-left", THUMB_FOOT, doc_foot)
        self.add_line("grip-right", doc_foot, pad_top)
        self.add_arc("fingertips", pad_top, pad_low, radius_x=PAD_R, sweep=True)
        px, py = pad_low
        lx, ly = WRIST_LOW
        self.add_bezier("palm", pad_low, ((px - 8, py), (lx + 12, ly), WRIST_LOW))
        self.add_contour("hand", "wrist-top", "thumb-top", "thumb-tip", "thumb-under",
                         "grip-left", "grip-right", "fingertips", "palm")

        # Document: open contour from the grip, round the top, down onto the grip line.
        r = DOC_RAD
        self.add_line("doc-left", GRIP, (DOC_L, DOC_T + r))
        self.add_arc("doc-tl", (DOC_L, DOC_T + r), (DOC_L + r, DOC_T), radius_x=r, sweep=True)
        self.add_line("doc-top", (DOC_L + r, DOC_T), (DOC_R - r, DOC_T))
        self.add_arc("doc-tr", (DOC_R - r, DOC_T), (DOC_R, DOC_T + r), radius_x=r, sweep=True)
        self.add_line("doc-right", (DOC_R, DOC_T + r), (DOC_R, DOC_B))
        self.add_contour("document", "doc-left", "doc-tl", "doc-top", "doc-tr", "doc-right")

        self.relate("connect", "hand", "document")
