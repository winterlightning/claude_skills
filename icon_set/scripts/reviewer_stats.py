"""Reviewer dashboard numbers from each catalog icon's current decision.

Activity and current status share one source, so the activity for a period is
exactly the part of today's status that was decided in that period.
"""
from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

OUTCOMES = {'approve': 'approved', 'pending': 'disapproved', 'disapprove': 'disapproved', 'rejected': 'rejected'}


def current_decisions(connection, catalog):
    """Current (status, actor, decided_at) per catalog icon, exactly as the icon review screen shows it."""
    rows = connection.execute('SELECT icon, svg_sha256, status, updated_by, updated_at FROM reviews ORDER BY updated_at').fetchall()
    decisions = {key: ('ready', None, None) for key in catalog}
    for key, sha, status, actor, stamp in rows:
        if key in catalog and catalog[key]['svg_sha256'] == sha:
            decisions[key] = ('ready' if status == 're-generated' else status, actor, stamp)
    for key, sha, status, actor, stamp in rows:
        if key in catalog and status == 'rejected':
            decisions[key] = ('rejected', actor, stamp)
    for key, sha, actor, stamp in connection.execute('SELECT icon,svg_sha256,created_by,created_at FROM split_requests WHERE active=1'):
        if key in catalog and catalog[key]['svg_sha256'] == sha:
            decisions[key] = ('rejected', actor, stamp)
    return decisions


def current_reviews(connection, catalog):
    """Statuses plus who approved, disapproved and rejected, for the icon review API."""
    decisions = current_decisions(connection, catalog)
    by = lambda wanted: {key: actor for key, (status, actor, _) in decisions.items() if status in wanted and actor}
    return ({key: status for key, (status, _, _) in decisions.items()},
            by({'approve'}), by({'pending', 'disapprove'}), by({'rejected'}))


def blank_counts():
    return dict(total=0, approved=0, disapproved=0, rejected=0, ready=0)


def add(group, outcome):
    group[outcome] += 1
    group['total'] += 1


def current_status(connection, catalog, reviewer='', decisions=None):
    """Icons per current decision, by family and by the reviewer who made it."""
    decisions = current_decisions(connection, catalog) if decisions is None else decisions
    totals, families, reviewers = blank_counts(), {}, {}
    for key, (status, actor, _) in decisions.items():
        outcome = OUTCOMES.get(status, 'ready')
        actor = actor if outcome != 'ready' and actor else ''
        if reviewer and actor != reviewer:
            continue
        add(totals, outcome)
        add(families.setdefault(catalog[key].get('family') or 'other', blank_counts()), outcome)
        if actor:
            add(reviewers.setdefault(actor, blank_counts()), outcome)
    return dict(totals=totals,
                families=[dict(family=name, **counts) for name, counts in sorted(families.items())],
                reviewers=[dict(reviewer=name, **counts) for name, counts in
                           sorted(reviewers.items(), key=lambda item: (-item[1]['total'], item[0]))])


def parse_stamp(stamp):
    try:
        when = datetime.fromisoformat(stamp.replace('Z', '+00:00'))
    except (ValueError, TypeError, AttributeError):
        return None
    return when.replace(tzinfo=timezone.utc) if when.tzinfo is None else when


def reviewer_stats(connection, params, users, catalog, now=None):
    """Count each icon's current decision on the local day it was made.

    An icon counts once, for the reviewer whose decision it currently holds.
    Decisions later replaced, regenerated or removed from the catalog are not counted,
    so an all-time period equals the current status.
    """
    zone_name = params.get('timezone', ['Asia/Ho_Chi_Minh'])[0]
    try:
        zone = ZoneInfo(zone_name)
    except (ZoneInfoNotFoundError, ValueError):
        raise ValueError('Choose a valid time zone.') from None
    family = params.get('family', [''])[0]
    if family and family not in {icon.get('family') for icon in catalog.values()}:
        raise ValueError('Choose a known family.')
    # Filter by family like Icon review does, so both screens show the same numbers.
    catalog = {key: icon for key, icon in catalog.items() if not family or icon.get('family') == family}
    decisions = current_decisions(connection, catalog)
    decided = []
    for key, (status, actor, stamp) in decisions.items():
        outcome = OUTCOMES.get(status)
        when = parse_stamp(stamp) if outcome else None
        if when:
            decided.append((when.astimezone(zone).date(), actor or '', key, outcome))
    today = (now or datetime.now(timezone.utc)).astimezone(zone).date()
    first_day = min((day for day, *_ in decided), default=today)
    try:
        end = date.fromisoformat(params.get('end', [today.isoformat()])[0])
        default_start = min(first_day, end) if params.get('period') == ['all'] else end - timedelta(days=6)
        start = date.fromisoformat(params.get('start', [default_start.isoformat()])[0])
    except (ValueError, OverflowError):
        raise ValueError('Choose valid start and end dates.') from None
    if not 0 <= (end - start).days < 366 or end == date.max:
        raise ValueError('Choose a date range between 1 and 366 days.')
    reviewer = params.get('reviewer', [''])[0]
    # Keep former reviewers available while they still own a current decision.
    reviewers = sorted(set(users) | {actor for _, actor, _, _ in decided if actor})
    if reviewer and reviewer not in reviewers:
        raise ValueError('Choose a known reviewer.')
    daily = {}
    for offset in range((end - start).days + 1):
        day = (start + timedelta(days=offset)).isoformat()
        daily[day] = dict(date=day, **empty_counts())
    by_reviewer = {user: dict(reviewer=user, active_days=0, **empty_counts())
                   for user in reviewers if not reviewer or reviewer == user}
    reviewer_daily = {(day, user): dict(date=day, reviewer=user, **empty_counts())
                      for day in daily for user in by_reviewer}
    totals, active_days = empty_counts(), set()
    for local_day, actor, _, outcome in decided:
        day = local_day.isoformat()
        if day not in daily or (reviewer and actor != reviewer):
            continue
        groups = [totals, daily[day]]
        if actor:
            groups += [by_reviewer[actor], reviewer_daily[(day, actor)]]
            active_days.add((actor, day))
        for group in groups:
            add(group, outcome)
    for actor, _ in active_days:
        by_reviewer[actor]['active_days'] += 1
    return dict(start=start.isoformat(), end=end.isoformat(), timezone=zone_name,
                reviewer=reviewer, family=family, available_reviewers=reviewers, totals=totals,
                unique_icons=totals['total'], daily=list(daily.values()),
                reviewer_daily=list(reviewer_daily.values()),
                reviewers=sorted(by_reviewer.values(), key=lambda row: (-row['total'], row['reviewer'])),
                history_since=datetime.combine(first_day, time.min, zone).isoformat() if decided else None,
                current=current_status(connection, catalog, reviewer, decisions),
                counting="Each icon's current decision, on the day it was made, for the reviewer who made it.")


def empty_counts():
    return dict(total=0, approved=0, disapproved=0, rejected=0)
