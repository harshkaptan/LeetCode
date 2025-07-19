from typing import List

class Solution:
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    """
    Removes all sub-folders from a list of folders.

    Args:
      folder: A list of folder paths.

    Returns:
      A list of the folders after removing all sub-folders.
    """
    folder.sort()
    
    if not folder:
      return []
      
    result = [folder[0]]
    
    for i in range(1, len(folder)):
      # Check if the current folder is a sub-folder of the last added valid folder.
      # A sub-folder must start with the parent's path followed by a '/'.
      if not folder[i].startswith(result[-1] + '/'):
        result.append(folder[i])
        
    return result