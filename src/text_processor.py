def clean_text(text):
    lines = text.splitlines()

    clean_lines = []

    for line in lines:
        line = line.strip()

        if line:
            clean_lines.append(line)

    return "\n".join(clean_lines)


if __name__ == "__main__":
    example = """
        Este es un documento.


        Tiene espacios innecesarios.


        Y varios saltos de línea.
    """

    result = clean_text(example)

    print(result)