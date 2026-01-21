from collections import defaultdict
from datetime import date
from typing import Dict, Iterable

# bucketize daily commit volume
def merge_stats(stats: Iterable[Dict[date, int]]) -> Dict[date, int]:
    merged = defaultdict(int)
    for stat in stats:
        for day, count in stat.items():
            merged[day] += count
    return dict(merged)
