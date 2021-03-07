import asyncio
from kasa import SmartPlug

async def main():
    plug = SmartPlug("10.0.0.32")
    await plug.update()
    print(plug.alias + " was located")
    if plug.is_on:
        await plug.turn_off()
        print(plug.alias + " was shut off")
    else:
        await plug.turn_on()
        print(plug.alias + " was turned on")


if __name__ == "__main__":
        asyncio.run(main())