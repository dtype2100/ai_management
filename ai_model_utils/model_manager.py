import os
import yaml
from huggingface_hub import snapshot_download
from pathlib import Path

def download_model(repo_id, revision="main", target_dir=None):
    """
    Hugging Face 모델을 다운로드하고 YAML 파일에 경로를 추가합니다.
    
    Args:
        repo_id (str): Hugging Face 모델 ID
        revision (str): 모델 버전
        target_dir (str): 다운로드할 디렉토리 경로
    """
    if target_dir is None:
        target_dir = f"ai_model_dir/hf/{repo_id.split('/')[-1]}"
    
    # 모델 다운로드
    snapshot_download(
        repo_id=repo_id,
        revision=revision,
        local_dir=target_dir,
        local_dir_use_symlinks=False
    )
    
    # YAML 파일 경로
    yaml_path = "ai_config/load_embedding_config.yaml"
    
    # YAML 파일이 존재하지 않으면 생성
    if not os.path.exists(yaml_path):
        config = {"models": []}
    else:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            if config is None:
                config = {"models": []}
    
    # 모델 정보 추가
    model_info = {
        "name": repo_id.split('/')[-1],
        "target_dir": target_dir
    }
    
    # 이미 존재하는 모델인지 확인
    exists = False
    for model in config["models"]:
        if model["name"] == model_info["name"]:
            model["target_dir"] = model_info["target_dir"]
            exists = True
            break
    
    if not exists:
        config["models"].append(model_info)
    
    # YAML 파일 저장
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)
    
    print(f"모델이 {target_dir}에 다운로드되었고, {yaml_path}에 경로가 추가되었습니다.")

def download_all_models(config_path="ai_config/ai_models_config.yaml"):
    """
    설정 파일에 있는 모든 모델을 다운로드합니다.
    
    Args:
        config_path (str): 모델 설정 파일 경로
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    for model in config["models"]:
        try:
            download_model(
                repo_id=model["repo_id"],
                revision=model.get("revision", "main"),
                target_dir=model["target_dir"]
            )
        except Exception as e:
            print(f"모델 {model['repo_id']} 다운로드 중 오류 발생: {str(e)}")
            continue

if __name__ == "__main__":
    # 예시: 단일 모델 다운로드
    # download_model("kakaocorp/kanana-nano-2.1b-embedding")
    
    # 예시: 모든 모델 다운로드
    download_all_models()
