import uuid

new_file = []
original_file = []

fname = "../README.md"


def generate_random_id_comment():
    random_id = uuid.uuid4()
    return f"<!-- Example ID: {random_id} --!>"


with open(fname, "r") as f:
    original_file = f.readlines()


for line in original_file:
    new_file.append(line)
    if line.strip().startswith("### "):
        new_file.append(generate_random_id_comment())

with open(fname, "w") as f:
    f.write("".join(new_file))
