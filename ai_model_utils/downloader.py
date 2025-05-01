from huggingface_hub import snapshot_download
import os
from datetime import datetime
from .manifest import update_manifest

def download_model(repo_id: str, local_dir: str, revision: str = "main", name: str = None, manifest_path: str = "ai_model_manifest/ai_model_manifest.json"):
    root_path = os.path.dirname(os.getcwd())
    local_dir = os.path.join(root_path, local_dir)
    manifest_path = os.path.join(root_path, manifest_path)    
    os.makedirs(local_dir, exist_ok=True)

    if os.path.exists(local_dir) and os.listdir(local_dir):
        print(f"⏩ 이미 다운로드됨: {local_dir}")
        return

    print(f"📥 {repo_id} 다운로드 중 → {local_dir}")
    snapshot_download(
        repo_id=repo_id,
        revision=revision,
        local_dir=local_dir,
    )
    print(f"✅ 다운로드 완료")

    model_info = {
        "name": name or repo_id.split("/")[-1],
        "repo_id": repo_id,
        "revision": revision,
        "path": local_dir,
        "downloaded_at": datetime.now().isoformat()
    }

    update_manifest(manifest_path, model_info)
