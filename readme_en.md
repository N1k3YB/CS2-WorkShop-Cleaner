[Сменить на Русский](https://github.com/N1k3YB/CS2-WorkShop-Cleaner/blob/main/readme.md)

# CS2 Map Cleanup Script

This script is designed to conveniently delete unnecessary folders with maps in Counter-Strike 2 (CS2). It automatically finds folders with files `publish_data.txt `, extracts the names of the maps and displays them in a user-friendly graphical interface (GUI). You can easily select the cards that are no longer needed and delete them along with the contents.

## Important warning ⚠️
Before using this script, make sure that **you have unsubscribed from the cards that you plan to delete**! Otherwise, the Steam client may download these maps again at the next CS2 update.

> Please note: even after deleting the cards, this process may repeat when updating CS2, if they are still listed in your subscriptions.

---

## Functionality
- **Scan**: The script automatically scans the folders in the directory where it is running for the presence of a file `publish_data.txt `.
- **Extracting the name of the card**: Finds and outputs the name of the card from each file `publish_data.txt `.
- **Selection of cards to delete**: Allows you to select cards to delete through the interface with checkboxes.
- **Delete**: Deletes the selected folders along with the contents.

## Installation and launch

Using:  
Run the script. A graphical interface will appear with the heading "CS2 WSC".
The window will display a list of found folders containing the file publish_data.txt , along with the name of the map.
Select the folders to delete:
Click on the desired maps to highlight them for deletion.
Click on the "Удалить выбранные папки" button.
Confirm the deletion in the pop-up window. The selected folders will be deleted along with the contents.

The path for the script:  
SteamLibrary\steamapps\workshop\content\730\  
  
When you run the script in a folder, the interface will show folders with maps (in the form of their IDs) and the names of the maps. Mark the unnecessary cards and confirm the deletion.

## Note
The script deletes folders irreversibly, so carefully check which cards you choose to delete. Deleted maps can be downloaded again at the next CS2 update if they are listed in Steam Workshop subscriptions.
