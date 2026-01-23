from commits import read_commit_dates, aggregate_by_day, build_calendar_grid
from heatmap import render_terminal


commits = read_commit_dates(".")
daily = aggregate_by_day(commits)
weeks = build_calendar_grid(daily)

render_terminal(weeks, daily)
