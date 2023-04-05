import hashlib
import os

# Function to calculate the SHA-1 hash of a file
def calculate_hash(filepath):
    sha1 = hashlib.sha1()
    with open(filepath, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

# Function to calculate the root hash of multiple files
def calculate_root_hash(filepaths):
    root_hash = ""
    for filepath in filepaths:
        if os.path.isfile(filepath):
            file_hash = calculate_hash(filepath)
            root_hash += file_hash
    if root_hash:
        root_hash = hashlib.sha1(root_hash.encode()).hexdigest()
    return root_hash

# Scenario with four Files
L1 = 'SOCCER.txt'
L2 = 'BASKETBALL.txt'
L3 = 'CRICKET.txt'
L4 = 'FOOTBALL.txt'

# Compute the Top Hash of the four files
filepaths = [L1, L2, L3, L4]
root_hash = calculate_root_hash(filepaths)

# Print the root Hash
print("root Hash: ", root_hash)

# Change one of the files and calculate the root Hash again
os.system('echo "Modified" >> ' + L1)
root_hash_modified = calculate_root_hash(filepaths)

# New Hash value
print("New Hash value: ", root_hash_modified)

# Comparison for the top two tier Hash values
if root_hash != root_hash_modified:
    print("Some files have been modified, root Hash does not match.")
else:
    print("root Hash matches.")
