import requests
from tqdm import tqdm
from requests_threads import AsyncSession
import warnings
warnings.filterwarnings("ignore")

url = input('Введите адрес сайта: ')

session = AsyncSession(n=1000)

async def _main():
    rs = []
    for _ in tqdm(range(1000)):
        rs.append(await session.get(url))

session.run(_main)
