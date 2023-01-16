import yaml


def load_params():
    with open('parameters/params.yaml', "r", encoding="utf-8") as yaml_file:
        params = yaml.safe_load(yaml_file)

    return params

