import requests


def fetch_random_jokes_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"

    response = requests.get(url)
    # print(response)
    object = response.json()
    # print(data)
    if object["success"] and "data" in object:
        data = object["data"]
        # print(data)
        data_count = len(data["data"])
        for index in range(0, data_count):
            joke = str(object["data"]["data"][index]["content"])
            # print("\n")
            print(joke, end=" \n\n")

    else:
        raise Exception("Failed to fetch jokes..")


def main():
    try:
        joke = fetch_random_jokes_freeapi()
        print(f"Jokes: {joke}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
