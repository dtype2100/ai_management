import os
import shutil

def delete_model(path: str):
    """
    지정한 로컬 모델 경로를 완전히 삭제합니다.

    Args:
        path (str): 삭제할 디렉토리 경로
    """
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"🗑 삭제 완료: {path}")
    else:
        print(f"⚠️ 경로 없음: {path}")
