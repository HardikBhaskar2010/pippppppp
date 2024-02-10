import os
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directory to monitor
monitor_dir = "c:\\Users\\SESA457837\\Downloads"  # Update with your directory path

# File extensions and their corresponding new names
file_types = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileRenamingHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key, value in file_types.items():
            time.sleep(1)

            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Detected new file " + file_name)

                old_file_path = monitor_dir + '\\' + file_name
                new_file_name = key + str(random.randint(0, 999)) + extension
                new_file_path = monitor_dir + '\\' + new_file_name

                os.rename(old_file_path, new_file_path)
                print("Renamed " + file_name + " to " + new_file_name)

event_handler = FileRenamingHandler()
observer = Observer()
observer.schedule(event_handler, monitor_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
