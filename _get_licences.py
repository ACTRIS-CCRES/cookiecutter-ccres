import requests
import os

URL = "https://api.github.com/licenses"

LICENSE_TEMPLATE = "./LICENSE"
LICENSES_DIR = "./LICENSES"
ARG = "license"


def fetch_licenses_from_gh():
    licences = requests.get(URL).json()
    text_licenses = {}
    for licence in licences:
        res = requests.get(licence["url"]).json()
        name = res["name"]
        text_licenses[name] = res["body"]
    return text_licenses


def main():
    text_licenses = fetch_licenses_from_gh()

    os.makedirs(LICENSES_DIR, exist_ok=True)

    jinja_template = ""
    first_if = True
    for name, body in text_licenses.items():
        filename = name.lower().replace(" ", "_").replace('"', "")

        with open(os.path.join(LICENSES_DIR, filename), "w") as f:
            f.write(body)

        escaped_name = name.replace('"', '\\"')
        if first_if == True:
            cookie_cutter_str = f'if cookiecutter.{ARG} == "{escaped_name}"'
            first_if = False
        else:
            cookie_cutter_str = f'elif cookiecutter.{ARG} == "{escaped_name}"'

        jinja_template += "{% " + cookie_cutter_str + " -%}\n"
        jinja_template += '{% include "' + os.path.join(LICENSES_DIR, filename) + '" %}\n'
    jinja_template += "{% endif %}"

    with open(LICENSE_TEMPLATE, "w") as f:
        f.write(jinja_template)


if __name__ == "__main__":
    main()
