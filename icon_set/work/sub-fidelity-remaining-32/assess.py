"""Visual review notes: size recommendations remain provisional until redrawn."""
import json
from pathlib import Path
W=Path(__file__).resolve().parent
notes=[
('spacing-trial','Restore the two eyes below the sloping eyebrows and the original thin, open frown. Check eyebrow-to-eye and eye-to-mouth clearances inside the circle.'),
('try-32','Restore the off-centre inner loop, its right-hand connection, and the longer outer sweep. This is chiefly a curve/proportion repair.'),
('spacing-trial','Restore the speech bubble and tail around the bitcoin glyph. Both vertical currency bars and both bowls must remain readable inside the bubble.'),
('try-32','Restore the relative sizes and near-tangent placement of the two bubbles. The current small ring is too small and too far from the large one; check its opening at 4px stroke.'),
('spacing-trial','Restore the magnifying-glass circle and handle around the three-face cube. Test the three face openings and cube-to-circle clearance.'),
('spacing-trial','Restore the interrupted document outline, its short internal marks and the rising slash. Preserve the source gaps rather than drawing a generic full rectangle.'),
('try-32','Restore the broken heart behind the descending slash, including the source openings. Start at 32; check the separation of the slash and interrupted outline.'),
('spacing-trial','Restore the SIM-card outline and clipped corner around the divided inner capsule. Check the nested border gaps.'),
('try-32','Preserve the source single crossbar and its curved, open outer form. Correct the contour and bar length without increasing the canvas first.'),
('try-32','Same source as the other euro version: restore the curved contour rather than its current flat top and bottom. Trial at 32.'),
('spacing-trial','Restore the speech bubble and tail around HI, preserving letter spacing and placement with shared glyphs. Test the inner text against the bubble.'),
('spacing-trial','Restore the outer rounded panel, the original shorter tracks and their round knobs. Test knob openings, row spacing and panel clearance.'),
('spacing-trial','Restore the rounded card around the horizontal key, keeping the two downward teeth and round bow. Test the teeth and bow inside the card.'),
('try-32','Restore the wavy image border around the mountain and small dot. Trial at 32 with the source asymmetric peak and short right slope intact.'),
('spacing-trial','Restore the circle around the nanobot, keeping the central dot and both curved lower appendages. Check all nested openings.'),
('spacing-trial','Restore the enclosing circle around the right-facing triangle and chevron. Test the triangle opening and separation between the two symbols.'),
('spacing-trial','Restore the circle around O and the smaller lowered 2. Preserve the subscript placement; test the two shared glyphs and circular border together.'),
('spacing-trial','Restore the rectangular speech bubble and tail around the padlock. Keep its shackle and central keyhole; test the nested openings.'),
('spacing-trial','Restore the long rounded password field around two crosses and an underscore. Preserve its horizontal proportions; check the three marks and border gaps.'),
('try-32','Restore the tall rounded outer shape and lower horizontal divider around the two short bars. Start at 32 without elongating the bars.'),
('spacing-trial','Restore the circle around the source-shaped pound sign. Preserve its curved lower foot and single crossbar using the appropriate shared glyph form.'),
('spacing-trial','Restore the enclosing circle around the left-facing chevron and triangle. Keep their original order; test the triangle opening and spacing.'),
('spacing-trial','Restore the circle around both left arrowheads and the curved return shaft. Keep the detached first chevron and the shaft attached only to the second.'),
('spacing-trial','Restore the enclosing circle and both diagonal prohibition segments. Preserve the tilted organic head and curving tail; check their nearby gaps.'),
('try-32','Restore the speech bubble and lower-right tail around two short unequal lines. Keep the line lengths and original positions; trial at 32.'),
('try-32','Restore three heart-shaped leaves, their meeting lines and the curved stem. A round-topped clover outline does not match this source; trial at 32.'),
('spacing-trial','Restore the enclosing circle around T and M, including their spacing and source proportions. Check the M opening and border clearance.'),
('try-32','Restore the magnifying-glass circle and lower-right handle around the unequal vertical lines. Keep the lines short and at their original relative heights.'),
('spacing-trial','Restore the enclosing circle and the minus mark to the right of the bust. Check the head opening, head-to-shoulder gap and minus placement.'),
('spacing-trial','Restore the circle around U and V. Preserve their source positions using shared glyphs; test the V opening and border gaps.'),
('spacing-trial','Restore the rounded card and its small lower-right mark beneath the two wireless arcs. Test the two arc gaps and arc-to-card spacing at 32 first.'),
('try-32','Restore the circle around the one-bar yuan sign. The simple internal structure is a good candidate for a 32px redraw; keep only the source single bar.'),
]
rows=json.loads((W/'inventory.json').read_text())
assert len(notes)==len(rows)==32
out=[]
for r,(priority,note) in zip(rows,notes):
 out.append(dict(icon=r['icon'],review='original and current enlarged comparison inspected',current_canvas=[32,32],size_trial=priority,note=note,validated_size=None))
(W/'size-review.json').write_text(json.dumps(out,indent=2))
print('32 visual assessments saved; no size certified without a redraw and validation.')
