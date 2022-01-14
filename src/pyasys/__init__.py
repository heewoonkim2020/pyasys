"""
The official Pyasys Python library!

Please check README.md for more information on how to set up Pyasys for your next project.
"""

class Pyasys:
    def __init__(self, import_name, author):
        """
        Sets up a basic project class where project data can be stored.
        
        :param import_name: The __name__ of the import structure.
        """
        # Setup
        self.setup_project(project_automation=True, author=author, import_dir=import_name)
    
    def setup_project(self, project_automation, author, import_dir):
        # Prepare for project
        self.project_automation = project_automation