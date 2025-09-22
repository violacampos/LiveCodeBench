import orjson
from tqdm import tqdm

def stringify_keys(obj):
    if isinstance(obj, dict):
        return {str(k): stringify_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [stringify_keys(i) for i in obj]
    else:
        return obj
    
    
def write_to_json(data:dict, output_path:str):
    data = stringify_keys(data)
    with open(output_path, "wb") as f:
        f.write(b"[")  # Start of JSON array
        for i, item in enumerate(tqdm(data, desc="Writing results")):
            if i > 0:
                f.write(b",")
            f.write(orjson.dumps(item))
        f.write(b"]")  # End of JSON array