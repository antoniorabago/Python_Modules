#!/usr/bin/env python3

def secure_archive(file_name: str,
                   content: str,
                   action: int = 0) -> tuple[bool, str]:
    try:
        if action == "r":
            with open(file_name, "r") as f:
                content = f.read()
            return True, content
        else:
            with open(file_name, "w") as f:
                f.write(content)
            return True, "Content successfully written to file"
    except FileExistsError as e:
        return False, str(e)
    except PermissionError as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "", 0))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "", 0))
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "hola mundo", 0))
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "hola mundo", 1))


if __name__ == "__main__":
    main()
