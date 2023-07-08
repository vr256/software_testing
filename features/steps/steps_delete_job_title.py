from typing import Any

from behave import when


@when("I delete job with {title}")
def _(context: Any, title: str) -> None:
    context.title = title
    context.admin_page.delete_job_title(title)
