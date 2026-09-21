# Symbol construction

Decide what the drawing is made of before placing points, and encode it as shared Python parameters so a later repair moves the right thing. Plan size matches drawing size: one line for a slash, an ownership sketch for a building.

**Vocabulary.** A *stroke* is one pen-down run (may be several primitives; use a contour when it must paint as one path). A *typed shape* is parameters (a rounded rect is w, h, r). A *pattern* is a repeat with count, step and radii (spiral, wave, zigzag, ring). A *definition* owns geometry; an *instance* owns origin and id prefix. A *series* owns count and step. *Symmetry* stores an axis and derives the mirror. A *connection* is two members sharing one integer point, declared with `relate("connect", ...)`; the declaration never moves geometry.

**Emission.** Circle = two semicircles or four quarters in a closed contour. Oval = elliptical arcs. Rect/square = closed polyline or lines and arcs. Capsule ends are true semicircles, radius half the short centerline dimension. Rounded rect has an independent corner radius that must fit its edges. Spiral, wave = tangent arc sections. Zigzag, star = polyline. Do not fabricate API methods; if a feature cannot be represented faithfully, record it.

**Ownership.** Each closed loop and detached run is a node. Enclosed detail belongs to the enclosing loop's composite; an attached external part (mug handle) is a sibling under the common owner. Repeat until one root. The closest common owner controls the relationship between siblings: the mug owns body/handle, the root owns mug/steam clearance. Fix a root gap at the root, not by moving a handle endpoint. Composites do not change family routing; apply reference triage first.

**Symmetry.** Only where the subject supports it; state what mirrors and what does not. `x_right = 2*axis_x - x_left`. A shape crossing the axis is stored once. Mirroring curves reverses sweep if endpoint order is kept; verify continuity and bulge instead of flipping flags until it looks right.

**Series and groups.** `origin_i = origin_0 + i*step`; recompute all on change; choose a step that centres an even count on integers. Rings: derive from centre and angle, then pick integer geometry that keeps the regularity; do not jitter members. Related groups share only what the subject shares (bars share width and baseline, not height).

**Nodes and joins.** Name nodes for role (`roof_apex`, `body_handle_top`) and compute them from owner parameters; never store the same coordinate twice. Emitted coordinates are integers; a fractional midpoint means revise the span. A point on a curved receiver must lie exactly on the arc. When a stroke joins mid-run, split the receiver at that point so both expose the endpoint, then declare only the actual contact pairs. A crossing is not a join. Two closed shapes may not touch under a `connect`; give them clearance or redesign as one outline. A zero-width gap is not an opening.

**Layout.** Choose keyshape before points; author to the centerline box (visible inset 2). If upright does not fit, rotate the whole logical subject together and re-solve integers; do not rotate directional symbols. If nothing fits, keep the findings, describe attempts, flag Exception in the gallery.

**Procedure.** Inspect and reduce; identify runs and loops; assign shapes; build ownership; record constraints in the module docstring; solve the family layout; emit with unique ids and shared points; validate and repair at the owner; inspect both themes and report.

**Repair at the owner.** Two objects crowd: common parent. Detail crowds its enclosure: the enclosure. Dense row: series step/count. Every window too dense: the definition. Unbalanced pair: the axis. Handle detaches after widening: shared nodes. Spiral collides: pattern params. Tight gap inside one stroke: that stroke. No layout fits: report. Never break repeat equality, drift the axis, slide a join off its receiver, or squeeze an opening shut to pass a local check. Two parts of one contour can still crowd each other; inspect holes, wedges and necks.

**Before reporting:** coordinates and radii legal; envelope satisfied; contours contiguous and closed; shared nodes still shared and declarations match real contacts; repeats and symmetry survived repairs; readable at native size both themes; report matches the actual candidate.
