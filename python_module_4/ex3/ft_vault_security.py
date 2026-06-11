# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/02 18:40:17 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/03 06:17:33 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Cyber Archives Security ===\n")


def secure_archive(filename: str, choice: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if choice == "r":
            with open(f"{filename}", 'r') as opened_file:
                content = opened_file.read()
        elif choice == "w":
            with open(f"{filename}", "w") as write_file:
                write_file.write(content)
            return (True, "Content successfully written to file")
    except Exception as e:
        return (False, f"{e}")
    return (True, content)


if __name__ == "__main__":
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"), "\n")
    print("Using 'secure_archive' to read from an inaccessible")
    print(secure_archive("/etc/master.passwd"), '\n')
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"), "\n")
    print("Using 'secure_archive' to write previous content to a new file")
    print(secure_archive("fun.txt", "w", "test succeed"))
