"""Daily reviewer throughput from immutable activity, independent of today's catalog."""
from datetime import date, datetime, time, timedelta, timezone
import json
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def review_outcome(action, details):
    if action == 'reject_combination':
        return 'rejected'
    status = details.get('status')
    if action in ('feedback', 'feedback_edit'):
        # Feedback on an already rejected icon is a comment, not another rejection.
        return 'disapproved' if status in ('pending', 'disapprove') else None
    if action == 'review':
        return {'approve': 'approved', 'pending': 'disapproved',
                'disapprove': 'disapproved', 'rejected': 'rejected'}.get(status)
    return None


def empty_counts():
    return dict(total=0, approved=0, disapproved=0, rejected=0)


def reviewer_stats(connection, params, users, now=None):
    """Count the last decision for each (local day, reviewer, icon).

    Repeated clicks and changed decisions within a day count once; reviews on
    later days count as fresh work. Never reconstruct history from mutable rows.
    """
    zone_name = params.get('timezone', ['Asia/Ho_Chi_Minh'])[0]
    try:
        zone = ZoneInfo(zone_name)
    except (ZoneInfoNotFoundError, ValueError):
        raise ValueError('Choose a valid time zone.') from None
    today = (now or datetime.now(timezone.utc)).astimezone(zone).date()
    try:
        end = date.fromisoformat(params.get('end', [today.isoformat()])[0])
        start = date.fromisoformat(params.get('start', [(end - timedelta(days=6)).isoformat()])[0])
    except (ValueError, OverflowError):
        raise ValueError('Choose valid start and end dates.') from None
    if not 0 <= (end - start).days < 366 or end == date.max:
        raise ValueError('Choose a date range between 1 and 366 days.')
    reviewer = params.get('reviewer', [''])[0]
    # Keep former reviewers available when their activity still exists.
    reviewers = sorted(set(users) | {row[0] for row in connection.execute(
        "SELECT DISTINCT username FROM activity_log WHERE action IN ('review','feedback','feedback_edit','reject_combination')") if row[0]})
    if reviewer and reviewer not in reviewers:
        raise ValueError('Choose a known reviewer.')
    try:
        lower = datetime.combine(start, time.min, zone).astimezone(timezone.utc).isoformat()
        upper = datetime.combine(end + timedelta(days=1), time.min, zone).astimezone(timezone.utc).isoformat()
    except OverflowError:
        raise ValueError('Choose dates within the supported calendar range.') from None
    rows = connection.execute('''SELECT id, username, action, icon, details, created_at
        FROM activity_log WHERE action IN ('review','feedback','feedback_edit','reject_combination')
        AND julianday(created_at) >= julianday(?) AND julianday(created_at) < julianday(?)
        AND (? = '' OR username = ?) ORDER BY julianday(created_at), id''',
        (lower, upper, reviewer, reviewer))
    decisions = {}
    for _, actor, action, icon, raw, stamp in rows:
        if not actor or not icon:
            continue
        try:
            details = json.loads(raw)
            if not isinstance(details, dict):
                continue
            outcome = review_outcome(action, details)
            when = datetime.fromisoformat(stamp.replace('Z', '+00:00'))
            if when.tzinfo is None:
                when = when.replace(tzinfo=timezone.utc)
            day = when.astimezone(zone).date().isoformat()
        except (ValueError, TypeError):
            continue
        if outcome:
            decisions[(day, actor, icon)] = outcome
    daily = {}
    for offset in range((end - start).days + 1):
        day = (start + timedelta(days=offset)).isoformat()
        daily[day] = dict(date=day, **empty_counts())
    by_reviewer = {user: dict(reviewer=user, active_days=0, **empty_counts())
                   for user in reviewers if not reviewer or reviewer == user}
    reviewer_daily = {(day, user): dict(date=day, reviewer=user, **empty_counts())
                      for day in daily for user in by_reviewer}
    totals, active_days, unique_icons = empty_counts(), set(), set()
    for (day, actor, icon), outcome in decisions.items():
        for group in (totals, daily[day], by_reviewer[actor], reviewer_daily[(day, actor)]):
            group[outcome] += 1
            group['total'] += 1
        active_days.add((actor, day))
        unique_icons.add(icon)
    for actor, _ in active_days:
        by_reviewer[actor]['active_days'] += 1
    first_record = connection.execute('SELECT MIN(created_at) FROM activity_log').fetchone()[0]
    return dict(start=start.isoformat(), end=end.isoformat(), timezone=zone_name,
                reviewer=reviewer, available_reviewers=reviewers, totals=totals,
                unique_icons=len(unique_icons), daily=list(daily.values()),
                reviewer_daily=list(reviewer_daily.values()),
                reviewers=sorted(by_reviewer.values(), key=lambda row: (-row['total'], row['reviewer'])),
                history_since=first_record,
                counting='Latest decision per icon, reviewer and day. Repeat reviews on another day count again.')
