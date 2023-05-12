from urllib.request import urlopen

url = "http://62.182.86.140/main/1397000/b0ea76adb31508c00e6b9cf6988b1620/Philip%2520E.%2520Tetlock%252C%2520Dan%2520Gardner%2520-%2520Superforecasting_%2520The%2520Art%2520and%2520Science%2520of%2520Prediction-Crown%2520%25282015%2529.epub"
save_as = "file.epub"


def main():
    # Download from URL
    with urlopen(url) as file:
        content = file.read()

    # Save to file
    with open(save_as, 'wb') as download:
        download.write(content)


if __name__ == "__main__":
    main()
