#!/usr/bin/env python3

def secure_archive(file_name: str,
                   action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as f:
                content = f.read()
            return True, content
        else:
            with open(file_name, "w") as f:
                f.write(content)
            return True, "Content successfully written to file"
    except OSError as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('/not/existing/file')}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('/etc/master.passwd')}\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive('ancient_fragment.txt')}\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive('new_file.txt', 'write','Text to write in file')}")


if __name__ == "__main__":
    main()
