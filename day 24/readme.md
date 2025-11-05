# File Operations in Python
A collection of Python scripts demonstrating various file operations including reading, writing, appending, and batch file processing with template replacement.  

---

## File Operations

---
## Reading from Files
```
 with open("my_file.txt") as file:  
    contents = file.read()  
    print(contents)  
   ```

- Purpose: Reads and displays the entire content of a file  
- Mode: Default read mode ('r')  
- Use Case: Viewing file contents without modification  

---

##  Writing to Files
```
with open("my_file.txt", mode="w") as file:  
    file.write("new text")  
```
- Purpose: Overwrites file with new content  
- Mode: Write mode ('w') - WARNING: Erases existing content  
- Use Case: Creating new files or completely replacing content  

---
## Appending to Files
```
with open("my_file.txt", mode="a") as file:
    file.write(" hello")
   ```
- Purpose: Adds content to the end of existing file   
- Mode: Append mode ('a')   
- Use Case: Adding to logs, updating records without losing existing data   

---
## File Paths: Absolute vs Relative

---
### Relative Paths  
Definition: Paths relative to the current working directory

### Absolute Paths
Definition: Complete path from the root directory

---

##  Important Notes

### File Mode Summary:  
- 'r' - Read (default): Opens file for reading only  
- 'w' - Write: Creates new file or overwrites existing one  
- 'a' - Append: Adds to end of file, preserves existing content  

---
## Path Selection Guide:

### Use Relative Paths when:  
- Files are within your project structure  
- Sharing code across different systems  
- Working with project-relative resources  

### Use Absolute Paths when:  
- Accessing system files outside project  
- Working with fixed system locations  
- Need guaranteed file location  

