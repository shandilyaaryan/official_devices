import re
import os
import json
import github

# GitHub Token
try:
    GH_TOKEN = os.environ.get("GH_TOKEN")
    if not GH_TOKEN:
        raise Exception("GH_TOKEN is missing.")
except Exception as e:
    print(f"Error: {str(e)}")
    exit(1)

# Constants
START_COMMENT = "<!--START_SECTION:devices-->"
END_COMMENT = "<!--END_SECTION:devices-->"
RE_PATTERN = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
jsonDir = "builds"

# Dictionary to store devices by brands
BRAND_DEVICES = {}

# Function: Generate README update
def generate_new_readme(devices, readme):
    replace_readme = f"{START_COMMENT}\n{devices}\n{END_COMMENT}"
    return re.sub(RE_PATTERN, replace_readme, readme)

# Function: Get all filenames
def get_all_filenames():
    return [f.replace(".json", "") for f in os.listdir(jsonDir) if f.endswith(".json")]

# Function: Get device info from JSON
def get_info(filename):
    try:
        with open(f"{jsonDir}/{filename}.json") as device_file:
            data = json.loads(device_file.read())
            # Extracting data from the response array
            response = data.get("response", [{}])[0]
            oem = response.get("oem", "Unknown OEM")
            device_name = response.get("device", "Unknown Device")
            maintainer = response.get("maintainer", "Unknown Maintainer")
            return {
                "codename": filename,  # Filename as codename
                "oem": oem,
                "device": device_name,
                "maintainer": maintainer,
            }
    except json.JSONDecodeError:
        print(f"Invalid JSON in file: {filename}.json")
    except Exception as e:
        print(f"Error reading {filename}.json: {str(e)}")
    return None

# Function: Add to brand-specific devices
def check_and_add_device(filename):
    info = get_info(filename)
    if not info:  # Skip if unable to get device info
        return
    text = f"{info['device']} ({info['codename']}) supported by {info['maintainer']}"
    brand = info["oem"]
    if brand not in BRAND_DEVICES:
        BRAND_DEVICES[brand] = []
    BRAND_DEVICES[brand].append(text)

# Function: Format devices by brand
def format_devices_by_brands():
    formatted_text = ""
    for brand, devices in sorted(BRAND_DEVICES.items()):
        formatted_text += f"## {brand} Devices\n"
        formatted_text += "```\n"
        formatted_text += "\n".join(sorted(devices))
        formatted_text += "\n```\n\n"
    return formatted_text.strip()

# Function: Update devices section
def update_devices():
    for filename in get_all_filenames():
        check_and_add_device(filename)
    return format_devices_by_brands()

# Main Execution: Update README
try:
    g = github.Github(GH_TOKEN)
    committer = github.InputGitAuthor("Projectpixelstarbot", "projectpixelstar@gmail.com")
    repo = g.get_repo("Project-PixelStar/official_devices")
    commit_message = "Pixelstar: Update devices readme [BOT]"
    contents = repo.get_readme()
    readme = contents.decoded_content.decode()
    device_update = update_devices()
    new_readme = generate_new_readme(device_update, readme)
    if new_readme != readme:
        repo.update_file(
            path=contents.path,
            message=commit_message,
            content=new_readme,
            sha=contents.sha,
            branch="14",
            committer=committer,
        )
        print("README updated successfully.")
    else:
        print("Nothing to change in devices readme.")
except Exception as e:
    print(f"Exception Occurred: {str(e)}")
