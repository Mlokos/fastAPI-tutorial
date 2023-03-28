from time import sleep


async def async_add(a: int, b: int):
    sleep(1)
    return a + b


def sync_add(a: int, b: int):
    sleep(1)
    return a + b


if __name__ == "__main__":
    print(sync_add(1, 2))
    print("finished sync function")
    print(async_add(1, 2))
    print("finished async function")
