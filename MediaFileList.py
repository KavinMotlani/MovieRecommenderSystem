import os
from os.path import expanduser

# Returns the names of files which are movies
def get_raw_file_list():
	
	mediaFiles = []
	# Gets the home directory for starting file traversal
	home = os.path.expanduser("~")
	
	movieFileFormats = [".mkv" , ".flv", ".vob" , ".avi" , ".mp4" , ".mov" , ".mpg" , ".wmv" , ".mpeg" , ".vob" , ".mpg" ]  # Non exhaustive list of video file formats
	# Traversing the whlole file system to find files
	for root, dirs, files in os.walk(home, topdown=False):
	    for filename in files:
	    	# Getting file size of the file
	        path = os.path.join(root, filename)
        	try:
        		filesize = os.stat(path).st_size 	# in bytes
	        	filesize = filesize/1000000			# in MB
	        except:
	        	continue
	        # Check if the file is of video format and is big enough to be a movie file
	        for extension in movieFileFormats:
	        	if(filename.lower().endswith(extension)):
	        		if(filesize>300):			# Filesize should be greater than 300 MB
	        			mediaFiles.append(filename)	# add the filename to the list of movies
	        			break

	return mediaFiles


movieFiles = get_raw_file_list()
print movieFiles

