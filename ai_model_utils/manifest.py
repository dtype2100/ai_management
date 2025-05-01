import os, json

def update_manifest(manifest_path: str, model_info: dict):
    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
    else:
        manifest = {"models": []}

    manifest["models"] = [m for m in manifest["models"] if m["name"] != model_info["name"]]
    manifest["models"].append(model_info)

    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"📝 manifest 갱신됨: {manifest_path}")
