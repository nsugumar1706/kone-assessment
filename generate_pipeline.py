import yaml
from pathlib import Path

def load_blueprint(file_path="blueprint.yml"):
    with open(file_path) as f:
        return yaml.safe_load(f)

def get_template_path(stage, name):
    return f"templates/{stage}/{name}.yml"

def append_template(output, template_file):
    with open(template_file) as src:
        output.write(f"\n# Begin {template_file}\n")
        output.write(src.read())
        output.write(f"\n# End {template_file}\n")

def generate_pipeline():
    blueprint = load_blueprint()
    output_file = Path(".gitlab-ci.yml")
    with output_file.open("w") as output:
        # Get blueprint values
        lang = blueprint['project']['language']
        build_tool = blueprint['project']['build_tool']
        deploy_type = blueprint['project']['deployment']['type']
        quality = blueprint['project']['quality']

        # Add Lint
        if quality.get("lint"):
            append_template(output, get_template_path("lint", lang))

        # Add Test
        if quality.get("test"):
            append_template(output, get_template_path("test", lang))

        # Add Build
        append_template(output, get_template_path("build", build_tool))

        # Add Deploy
        append_template(output, get_template_path("deploy", deploy_type))

        # Add Common: versioning, etc.
        append_template(output, get_template_path("common", "versioning"))

if __name__ == "__main__":
    generate_pipeline()

