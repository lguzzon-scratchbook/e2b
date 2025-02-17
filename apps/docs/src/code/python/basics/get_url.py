import asyncio
from os import getenv
from e2b import Session

E2B_API_KEY = getenv("E2B_API_KEY")

async def main():
  session = await Session.create(id="Nodejs", api_key=E2B_API_KEY)
  url = session.get_hostname() # $HighlightLine
  print("https://" + url)
  await session.close()

asyncio.run(main())
