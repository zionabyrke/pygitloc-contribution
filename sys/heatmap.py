from datetime import date, timedelta
from typing import Dict
from rich.console import Console
from rich.text import Text
from intensity import intensity_level

console = Console()
COLOR_MAP = {
    0: "grey23",
    1: "green4",
    2: "green3",
    3: "green1",
    4: "green",
}

def render_heatmap(data: Dict[date, int]) -> None:
    today = date.today()
    start = today - timedelta(days=183) # 6 months
    week = []
    current = start

    console.print("\n[bold]Git Contribution[/bold]\n")
    while current <= today:
        count = data.get(current, 0)
        level = intensity_level(count)
        color = COLOR_MAP[level]

        week.append(Text("■ ", style=color))
        if current.weekday() == 6: # Sunday
            console.print(*week)
            week = []
        current += timedelta(days=1)

    if week:
        console.print(*week)
