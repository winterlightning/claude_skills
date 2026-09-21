# Geometry

An icon is a Python class; its primitive list is the geometry. Integer coordinates in final canvas space, positive integer radii. Every call returns `self`.

| Call | Emits |
|---|---|
| `add_line(id, (x1,y1), (x2,y2))` | one segment |
| `add_arc(id, start, end, radius_x=r, radius_y=None, large_arc=False, sweep=True)` | one elliptical arc |
| `add_bezier(id, start, (c1, c2, knot), ...)` | cubic run; knots integer, controls may be fractional |
| `add_dot(id, (x,y))` | zero-length line, paints as a stroke-wide point |
| `add_polyline(id, p1, p2, ..., closed=False)` | segments `id-1..n` grouped in one contour |
| `add_contour(id, *member_ids, closed=False)` | groups existing primitives into one path |
| `add_anchor(name, (x,y))` | named point for composition |
| `relate("connect"\|"occlude"\|"knockout", *ids)` | declared relationship |

**Contours decide how joins paint.** Members of a contour emit as one path with round joins. Loose primitives get round caps. Four loose lines make a square with eight overlapping caps; the same four in a closed contour make four clean joins. Members must be contiguous head-to-tail; closed contours must return to start.

**Arcs.** Centre is derived from endpoints and radii, never given. Pick endpoints that are true extrema of the intended circle so the centre lands on an integer point. A circle is two semicircles (or four quarters) in a closed contour, never one arc with coincident endpoints. Elliptical arcs (`radius_x != radius_y`) are allowed and often needed to hit both a width and a height. Check an arc's flags with `icon_set.validation.envelope.arc_geometry`.

**Registry.** The folder is the registry. One file per icon in the family folder, named `<icon_id>` with underscores; subclass the family base (`Sub32`, `Solo48`, `Container64`). No profile attribute exists to override. A file in the wrong folder fails discovery. Leading `_` modules are not scanned.

Element ids are descriptive (`lobe-left-outer`, not `path-3`); every failure quotes them.
