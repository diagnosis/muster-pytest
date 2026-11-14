import random
import uuid

ADJ = ["brisk", "sunny", "quiet", "amber", "swift", "rustic", "clever", "stormy"]
NOUN = ["otter", "falcon", "cedar", "harbor", "lark", "meadow", "pebble", "summit"]
HOST = "test.dev"


def unique_identity() -> tuple[str, str]:
    f_name = random.choice(ADJ)
    l_name = random.choice(NOUN)
    tag = uuid.uuid4().hex[:6]
    name = f"{f_name.capitalize()} {l_name.capitalize()} {tag}"
    email = f"{f_name}.{l_name}.{tag}@{HOST}"
    return name, email
