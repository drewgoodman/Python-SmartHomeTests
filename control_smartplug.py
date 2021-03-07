import asyncio
from kasa import SmartPlug

async def main():
    try:
        plug = SmartPlug("10.0.0.32")
        await plug.update()
        print(f"{plug.alias} was located")
        if plug.is_on:
            await plug.turn_off()
            print(f"{plug.alias}  was shut off")
        else:
            await plug.turn_on()
            print(f"{plug.alias}  was turned on")
    except:
        print("Could not find a Smart Device at that address.")


if __name__ == "__main__":
        asyncio.run(main())