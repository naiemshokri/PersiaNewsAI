from rich.console import Console
from rich.panel import Panel

console = Console()


def show_dashboard(
    feeds,
    collected,
    published,
    duplicates,
    errors
):

    console.clear()

    text = f"""
Feeds        : {feeds}

Collected    : {collected}

Published    : {published}

Duplicates   : {duplicates}

Errors       : {errors}
"""

    console.print(
        Panel(
            text,
            title="PersiaNews AI",
            expand=False
        )
    )


def log_event(message):

    console.print(
        message
    )
