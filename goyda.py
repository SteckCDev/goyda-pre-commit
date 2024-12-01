import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Final


BASE_DIR: Final[Path] = Path(__file__).parent
RELATIVE_SOUND_PATH: Final[Path] = BASE_DIR / "resources" / "goyda.wav"
SOUND_PATH: Final[str] = os.path.abspath(RELATIVE_SOUND_PATH)


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
        print(f"Goyda failed to be yelled: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
