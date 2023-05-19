import os
import subprocess


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
XML_DIR = os.path.join(REPORTS_DIR, "xml")

reports = [
    "TESTS-login.xml",
]

# specifying order of testing features
# (files should be deleted after they are uploaded)
feature_pathes = [
    os.path.join(BASE_DIR, "features", "login.feature"),
]

for path in feature_pathes:
    subprocess.run(["behave", path, "--junit",
                   "--junit-directory=reports/xml"])

for filename in [os.path.join(XML_DIR, report) for report in reports]:
    subprocess.run(["junit2html",
                    filename,
                    os.path.join(
                        REPORTS_DIR, filename.partition(
                            "-")[2].partition(".xml")[0] + ".html"
                    ),
                    ])
