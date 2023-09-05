import os

# Specify the URL path to your static directory
static_directory_url = 'static'  # Adjust this path as needed

# Convert the URL path to an absolute file system path
static_directory = os.path.abspath(os.path.join(os.getcwd(), static_directory_url))


# Create a list to store the file names
files = []

# Iterate through the files in the "files" directory and append them to the list
for filename in os.listdir(os.path.join(static_directory, 'files')):
    if filename.endswith('.txt'):  # You can specify the file extension you're interested in
        files.append(filename)

# Now you can access the files like files[0], files[1], etc.
print(files)
