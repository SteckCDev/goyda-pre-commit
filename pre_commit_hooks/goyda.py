import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Final


BASE_DIR: Final[Path] = Path(__file__).parent
SOUND_PATH: Final[str] = str(BASE_DIR / "resources" / "goyda.wav")


def main() -> None:
    try:
        match platform.system():
            case "Darwin":
                subprocess.run(["afplay", SOUND_PATH], check=True)
            case "Linux":
                subprocess.run(["paplay", SOUND_PATH], check=True)
            case "Windows":
                import winsound
                winsound.PlaySound(SOUND_PATH, winsound.SND_FILENAME | winsound.SND_ASYNC)
            case _:
                raise OSError("This operating system isn't supported")
    except Exception as e:
        print(f"Failed to play sound: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
