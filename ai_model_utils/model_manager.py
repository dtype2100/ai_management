from .config_loader import load_config
from .downloader import download_model

def download_all_models(config_path="ai_models_config.yaml"):
    config = load_config(config_path)

    for model in config["models"]:
        name = model["name"]
        target_dir = model["target_dir"]
        repo_id = model["repo_id"]
        revision = model.get("revision", "main")

        download_model(repo_id, target_dir, revision, name=name)
