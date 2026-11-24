from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="dummy" # ollama不需要真实key，随便填字符串
)

resp = client.chat.completions.create(
    model="happyai",
    messages=[{"role": "user", "content": "10-4等于多少 /think"}]
)
print(resp.choices[0].message.content)

# import requests

# def amap_geocode(address: str, key: str):
#     url = "https://restapi.amap.com/v3/geocode/geo"
#     params = {
#         "address": address,
#         "key": key,
#         "output": "json"
#     }
#     resp = requests.get(url, params=params, timeout=10)
#     res = resp.json()
#     if res.get("status") != "1":
#         return None
#     geocode = res["geocodes"][0]
#     return {
#         "province": geocode["province"],
#         "city": geocode["city"],
#         "district": geocode["district"],  # 这里拿到：吴江区
#         "adcode": geocode["adcode"],
#         "formatted_address": geocode["formatted_address"]
#     }

# if __name__ == "__main__":
#     addr = "苏州市北局22号苏州人民商场主楼1F西侧户外商铺"
#     # 替换成你自己申请的key
#     ret = amap_geocode(addr, key="38078da53bb0c6a0a0166489fc6d9484")
#     print(ret)
