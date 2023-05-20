from behave import when


@when("I delete job with {title}")
def step_impl(context, title):
    context.title = title
    context.admin_page.delete_job_title(title)
