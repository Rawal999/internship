
### --- Text mode ----

# Writing

with open("output/sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n ")
    
    
# Reading
with open("output/sample.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
    
# --- BINARY MODE ---
binary_data = b"This is binary content.\nLine two."

# Writing
with open("output/sample_binary.bin", "wb") as file:
    file.write(binary_data)
    
# Reading
with open("output/sample_binary.bin", "rb") as file:
    content = file.read()
    print("\nBinary Mode Output:\n", content)