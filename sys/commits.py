from collections import defaultdict, OrderedDict
from dulwich.repo import Repo
from dulwich.walk import Walker
from datetime import datetime, timezone, date, timedelta
from dateutil.relativedelta import relativedelta

def read_commit_dates(repo_path="C://Users//Renz//Documents"):
    '''
    Returns a list of datetime.date objects for all commits in the repo
    '''
    repo = Repo(repo_path)
    walker = Walker(repo.object_store, [repo.head()])
    today = date.today()
    cutoff = today - relativedelta(months=6)
    dates = []

    for entry in walker:
        commit = entry.commit
        dt = datetime.fromtimestamp(
            commit.commit_time, timezone.utc
        ).date()

        if dt >= cutoff:
            dates.append(dt)
    return dates

def aggregate_by_day(commit_dates):
    '''
    Input: list[date]
    Output: dict[date] -> int
    '''
    counts = defaultdict(int)
    for d in commit_dates:
        counts[d] += 1

    return dict(counts)



def group_weeks_by_month(weeks):
    '''
    Groups week columns by the month they belong to
    Uses the Monday of each week as the canonical date
    '''
    months = OrderedDict()
    for week in weeks:
        month_key = week[0].strftime("%Y-%m")
        if month_key not in months:
            months[month_key] = []
        months[month_key].append(week)

    return months


def start_of_week(d):
    return d - timedelta(days=d.weekday())


def build_calendar_grid(contribs):
    '''
    Output:
    {
      "weeks": [
         [date, date, date, date, date, date, date],
         ...
      ]
    }
    '''
    if not contribs:
        return []

    first_day = min(contribs)
    last_day = max(contribs)
    start = start_of_week(first_day)
    end = start_of_week(last_day) + timedelta(days=6)
    weeks = []
    current = start

    while current <= end:
        week = [current + timedelta(days=i) for i in range(7)]
        weeks.append(week)
        current += timedelta(days=7)

    return weeks