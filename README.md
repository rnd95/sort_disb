# sort_disb
This program is designed to sort files in a specific directory structure.
Here's a breakdown of what it does:

Logging Configuration: Sets up logging to write debug and error messages to a file named sorting_logs.log.

Folder Detection: Lists all subfolders (district folders) in the current directory.

Processing District Folders:

For each district folder, it attempts to:
Find ZIP files within the district folder.
Unpack each ZIP file into a temporary folder within the district folder.
Iterate over bank folders (from 'T00_P01' to 'T99_P01') within the unpacked content.
For each bank folder, it:
Creates an output folder structure (SORTED/{bank_code}/{SheetType}) if it doesn't exist.
Copies the contents of the bank folder to the corresponding output folder.
Cleanup: Removes the temporary folder (temp_folder) after processing all ZIP files in a district folder.

Error Handling: Logs any errors that occur during the process.
