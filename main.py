import subprocess
import os


def md_translate_walk(directory: str = "") -> None:
    root_dir = os.path.join(directory)
    for root, folders, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(file_path)
                command = f"md-translate {file_path} -F en -T ru -P deepl --new-file --overwrite --drop-original"
                subprocess.run(command.split(' '))


if __name__ == "__main__":
    md_translate_walk("help")
