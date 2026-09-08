# Authoring geometry

An icon is a Python class. Its primitive list is also the serializable geometry
AST, so the model and the interchange format cannot disagree.

## The authoring API

`icon_set/model/icons/base.py`. Every method returns `self`, so calls chain.

| Call | Emits |
|---|---|
| `add_line(id, (x1,y1), (x2,y2))` | one straight segment |
| `add_arc(id, start, end, radius_x=r, radius_y=r, large_arc=False, sweep=True)` | one elliptical arc |
| `add_dot(id, (x,y))` | a zero-length line: one round cap, painted stroke-wide |
| `add_polyline(id, p1, p2, …, closed=False)` | joined segments `id-1..n` grouped in a contour |
| `add_contour(id, *members, closed=False)` | groups existing primitives into one path |
| `add_anchor(name, (x,y))` | a named point for composition |
| `relate("connect"\|"occlude"\|"knockout", *members)` | a declared relationship |

Coordinates are **integers** in final canvas space. Radii are positive integers.

## Contours decide how joins paint

A contour's members are emitted as **one** `<path>`, so interior vertices paint
as round joins. Primitives outside a contour become their own path, so their
ends paint as round caps.

That difference is visible. A closed square authored as four loose lines shows
eight overlapping caps at its corners; the same four lines in a closed contour
show four clean joins.

Contour members must be contiguous head-to-tail, and a closed contour must
return to its start. The renderer refuses anything else, naming the member and
both coordinates.

`add_polyline` is the shorthand for the common case and handles this for you.

## A worked example

```python
class Heart(Sub32):                        # sub family, so SUB32, so 32x32
    icon_id = "heart"
    keyshape = Keyshape.HRECT_XL          # visible (0,2)-(32,30)
    semantic_role = "MAIN"
    semantic_kind = "noun"

    def build(self) -> None:
        self.add_arc("lobe-left-inner", (16, 8), (10, 4), radius_x=6, radius_y=4, sweep=False)
        self.add_arc("lobe-left-outer", (10, 4), (2, 12), radius_x=8, sweep=False)
        self.add_arc("shoulder-left", (2, 12), (6, 20), radius_x=10, sweep=False)
        self.add_line("side-left", (6, 20), (16, 28))
        # ... mirrored ...
        self.add_contour("outline", "lobe-left-inner", ..., closed=True)
```

Note what the class does **not** say: its profile. `Sub32` resolves that from
the family contract, and there is no attribute to override. The same is true of
`Solo48` and `Container64`. The family base also places the `center` anchor for
you, and `Container64` adds the advisory `content-top-left` and
`content-bottom-right`.

Element ids are stable and descriptive because every validator failure quotes
them back at you. `lobe-left-outer` tells you where to look; `path-3` does not.

## Arcs

An SVG arc is defined by its **endpoints plus radii**, and its centre is derived
from those. Two consequences worth internalising:

- **The centre is computed, not given.** Pick endpoints and radii so the centre
  lands where you intend. `radius_x=8` from `(10,4)` to `(2,12)` gives centre
  `(10,12)` — a clean quarter circle — but only because those endpoints are that
  circle's top and leftmost point.
- **The derivation runs through a square root**, so a mathematically exact bound
  can land ~1e-15 away. The validator carries a `numeric_epsilon` for exactly
  this. It is a floating-point guard, never a design allowance.

To find the flags for an arc you have in mind, ask:

```python
from icon_set.model.primitives import Arc, Point
from icon_set.validation.envelope import arc_geometry
for large in (False, True):
    for sweep in (False, True):
        print(large, sweep, arc_geometry(Arc("t", Point(16,8), Point(10,4), 6, 4, large, sweep)))
```

An **elliptical** arc (`radius_x != radius_y`) buys you a lot of freedom. The
`tilde` reaches its keyshape's top and bottom edges only because its crests are
half-ellipses with `rx=7, ry=8` — semicircles could not span the width and reach
the height at once.

## Registering: the folder is the registry

There is no list to append to. The registry discovers icons **by folder**: every
public module in a family's package is imported, and every class in it that
subclasses that family's base and carries an `icon_id` is built, tested and
shipped.

So a new icon is exactly one new file:

| Family | Put the module in | Subclass |
|---|---|---|
| `sub` | `icon_set/model/icons/sub/` | `Sub32` |
| `solo` | `icon_set/model/icons/solo/` | `Solo48` |
| `container` | `icon_set/model/icons/container/` | `Container64` |

Name the file after the `icon_id` with underscores for hyphens (`clipboard`
lives in `container/clipboard.py`, `film-frame` in `solo/film_frame.py`). One
file per icon. Never append a new icon to an existing family file such as
`shapes.py`; shared files are for reading, and they become unmanageable once
every icon lands in them. A module whose name starts with `_` is not scanned.

The folder and the base must agree. A `Solo48` subclass saved into `sub/` fails
discovery with both family names in the message, and nothing builds until it is
moved. This is deliberate: the folder is the family, and the family is the
profile, so a file in the wrong folder is an icon on the wrong canvas.

## Lucide references

See [intake.md](intake.md#lucide-references). Records go on the icon as
`keywords`/`aliases` and in your reply; the reference is a construction
argument, not a source to copy.
