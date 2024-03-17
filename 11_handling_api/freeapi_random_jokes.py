import requests


def fetch_random_jokes_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"

    response = requests.get(url)
    # print(response)
    object = response.json()
    # print(data)
    if object["success"] and "data" in object:
        # data = object["data"]
        joke = object["data"]["content"]
        return joke

    else:
        raise Exception("Failed to fetch jokes..")


def main():
    try:
        joke = fetch_random_jokes_freeapi()
        print(f"Joke: {joke}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
