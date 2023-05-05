import chardet

# Open the file in binary mode
with open('C:/Users/rodri/Documents/Proyecto-2/tutores.csv', 'rb') as f:
    # do something with the file
    # Read the first few lines to get a sample
    sample = f.read(1000)

# Detect the encoding of the sample
result = chardet.detect(sample)

# Print the encoding
print(result['encoding'])