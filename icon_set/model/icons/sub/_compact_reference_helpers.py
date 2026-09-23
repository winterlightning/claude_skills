"""Shared construction helpers for compact, source-faithful SUB32 artwork."""


def circle(icon, name, cx, cy, radius):
    icon.add_arc(f"{name}-top", (cx - radius, cy), (cx + radius, cy), radius_x=radius)
    icon.add_arc(f"{name}-bottom", (cx + radius, cy), (cx - radius, cy), radius_x=radius)
    icon.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)


def rounded_rect(icon, name, left, top, right, bottom, radius):
    points = (
        (left + radius, top),
        (right - radius, top),
        (right, top + radius),
        (right, bottom - radius),
        (right - radius, bottom),
        (left + radius, bottom),
        (left, bottom - radius),
        (left, top + radius),
    )
    members = []
    for index, start in enumerate(points):
        end = points[(index + 1) % len(points)]
        member = f"{name}-{index}"
        members.append(member)
        if index % 2:
            icon.add_arc(member, start, end, radius_x=radius)
        else:
            icon.add_line(member, start, end)
    icon.add_contour(name, *members, closed=True)
