from rich.console import Console
from rich.text import Text
from commits import group_weeks_by_month


def render_terminal(weeks, contribs):
    console = Console()
    months = group_weeks_by_month(weeks)

    day_labels = ["Mon", "", "Wed", "", "Fri", "", ""]
    console.print("\nGit Contributions (Last 6 Months)\n")

    # month header
    header = "     "
    for month, month_weeks in months.items():
        label = month_weeks[0][0].strftime("%b %Y")
        width = len(month_weeks) * 4
        header += label.center(width)
    console.print(header)

    # rows
    for day_index in range(7):
        row = Text(f"{day_labels[day_index]:>4} ")

        for month_weeks in months.values():
            for week in month_weeks:
                d = week[day_index]
                count = contribs.get(d, 0)
                cell = f"{count:>3} "
                row.append(cell)
        console.print(row)
