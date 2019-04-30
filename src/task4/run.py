def accum(text):
    if not isinstance(text, str):
        raise Exception("Type Error")
    new_text = []
    for i, ch in enumerate(text.lower()):
        new_text.append(ch.upper() + i * ch)
    return "-".join(new_text)


def main():
    print("Start 4. task")
    print(accum("Hello x]"))

if __name__ == "__main__":
    main()
