import requests
import numpy as np
import asyncio
import time
import random

class TransformerEmuleting():
    transformers_unique_key = (
        "asqwdskacmasdladjasd",
        "1zx3de1d1wead1sd123d",
        "hjb12h3v1gh2d12u12vh",
        "vb12jh3dy7as12vghev1",
        "1h2vd6fasv12ywev1123",
        "sdc1278gb12b1e2uy12e",
    )
    url = "/"
        
    def generate_dga_data(self):
        return np.random.sample(6, low=1, high =2)
        # return [np.random.rand for _ in range(6)]

    def get_random_unique_key(self):
        return random.choice(self.transformers_unique_key)

    async def run(self):
        while True:
            data = {
                "dga_data":self.generate_dga_data,
                "key":self.get_random_unique_key()
            }
            # req = requests.post(self.url, data = data)
            time.sleep(np.random.sample())
            print(data)

    def as_run(self):
        asyncio.run(self.run())

if __name__ == '__main__':
    TransformerEmuleting().as_run()
    
