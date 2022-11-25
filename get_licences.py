import requests

URL = "https://api.github.com/licenses"
OUTPUT_FILE = "LICENSE.cookiecutter"
ARG = "licence"


def main():
    licences = requests.get(URL).json()
    text_licenses = {}
    for licence in licences:
        print(licence)
        res = requests.get(licence["url"]).json()
        print(res)
        name = res["name"]
        text_licenses[name] = res["body"]

    with open(OUTPUT_FILE, "w") as f:
        first_if = True
        f.write(f"# {list(text_licenses.keys())}\n")
        for name, body in text_licenses.items():
            if first_if == True:
                cookie_cutter_str = f'if cookiecutter.{ARG} == "{name}"'
                first_if = False
            else:
                cookie_cutter_str = f'elif cookiecutter.{ARG} == "{name}"'
            f.write("{% " + cookie_cutter_str + " -%}\n")
            f.write(body)
            f.write("\n")
        f.write("{% endif %}")


if __name__ == "__main__":
    main()
