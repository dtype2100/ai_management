import os, yaml

def load_config(filename: str, subdir: str = "ai_config") -> dict:
    root_path = os.path.dirname(os.getcwd())
    config_path = os.path.join(root_path, subdir, filename)

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ 설정 파일 없음: {config_path}")
    
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
