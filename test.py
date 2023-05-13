import os
import subprocess


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
XML_DIR = os.path.join(REPORTS_DIR, "xml")

reports = [
    "TESTS-upload_file.xml",
    "TESTS-get_file_metadata.xml",
    "TESTS-delete_file.xml",
]

# specifying order of testing features
# (files should be deleted after they are uploaded)
feature_pathes = [
    os.path.join(BASE_DIR, "features", "upload_file.feature"),
    os.path.join(BASE_DIR, "features", "get_file_metadata.feature"),
    os.path.join(BASE_DIR, "features", "delete_file.feature")
]

for path in feature_pathes:
    subprocess.run(["behave", path, "--junit", "--junit-directory=reports/xml"])

for filename in [os.path.join(XML_DIR, report) for report in reports]:
    subprocess.run(["junit2html",
                     filename,
                     os.path.join(
                        REPORTS_DIR, filename.partition("-")[2].partition(".xml")[0] + ".html"
                      ),
                    ])
