import os
import subprocess
import sys
from typing import Any

from selenium import webdriver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
XML_DIR = os.path.join(REPORTS_DIR, "xml")

reports = [
    "TESTS-login.xml",
    "TESTS-add_job_title.xml",
    "TESTS-delete_job_title.xml",
]

# specifying order of testing features
# (files should be deleted after they are uploaded)
feature_pathes = [
    os.path.join(BASE_DIR, "features", "login.feature"),
    os.path.join(BASE_DIR, "features", "add_job_title.feature"),
    os.path.join(BASE_DIR, "features", "delete_job_title.feature"),
]


class DriverFactory:
    @staticmethod
    def get_driver(browser: str) -> Any:
        browser = browser.lower()
        browsers = {
            "chrome": webdriver.Chrome,
            "firefox": webdriver.Firefox,
            "edge": webdriver.Edge,
            "safari": webdriver.Safari,
        }
        if browser not in browsers:
            return None
        return browsers[browser]()


def run_tests() -> None:
    if len(sys.argv) > 1:
        browser = sys.argv[1]
    else:
        browser = "chrome"

    for path in feature_pathes:
        subprocess.run(
            [
                "behave",
                path,
                "--junit",
                "--junit-directory=reports/xml",
                "-D",
                f"browser={browser}",
            ]
        )

    for filename in [os.path.join(XML_DIR, report) for report in reports]:
        subprocess.run(
            [
                "junit2html",
                filename,
                os.path.join(
                    REPORTS_DIR,
                    filename.partition("-")[2].partition(".xml")[0] + ".html",
                ),
            ]
        )


if __name__ == "__main__":
    run_tests()
