### pyparity v6 1/05/20
### py parity takes folder inputs and clones files to a remote drive

# Invoke mover
from dirsync import sync
# Folder sync locations
class LOCATION():
    # Directory variables
    source_folder = []
    destination_folder = []
    parity_folders = []
    
    # Directory to be copied, add to list.
    def source_directory(self):
        sourcefolder = input("Select Source Directory: ")
        self.source_folder.append(sourcefolder)
    # Directory to be copied to, add to list.
    def destination_directory(self):
        destinationfolder = input("Select Destination Directory: ")
        self.destination_folder.append(destinationfolder)
    # Add both directories to a single string
    def concatenate_folders(self):
        self.parity_folders.append(LOCATION.source_folder)
        self.parity_folders.append(LOCATION.destination_folder)
    # Dump results to console
    def print_result_folders_source(self):
        print("You have selected the source directory: "+ self.source_folder[0])
    def print_result_folders_destination(self):
        print("You have selected the destination directory: "+ self.destination_folder[0])

#

class SYNC():
    # Sync variables
    fl_source = LOCATION.folder_locations.source_directory()
    fl_dest = folder_locations.destination_directory()
    def user_sync(self):
#       sync(folder_locations.source_directory, folder_locations.destination_directory,'sync',verbose=True,content=True,purge=True,create=True)
        sync(fl_source[0,0],fl_dest[0,0],'sync',verbose=True,content=True,purge=True,create=True)            
        
# Class variables
folder_locations = LOCATION()
sync_files = SYNC()
#fl_source = folder_locations.source_directory
#fl_dest = folder_locations.destination_directory
# Call class for user input on directories, then print to console.
folder_locations.source_directory()
folder_locations.destination_directory()
folder_locations.print_result_folders_source()
folder_locations.print_result_folders_destination()
# Call class for syncing folders
sync_files.user_sync()


