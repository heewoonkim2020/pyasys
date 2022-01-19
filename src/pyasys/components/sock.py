from . import MIDDLEWARE

def get_process(self, process_name, import_name, process_intel, device_propre):
    return MIDDLEWARE.IGNORE_DIR.append({
        "name": [process_name],
        "import_name": [import_name],
        "processes": [process_intel, device_propre],
        "val_render_data": [
            [
                {
                    "return_controller": (
                        (0, 0, 0, 0),
                        (1, 1, 1, 1),
                        (2, 2, 2, 2),
                        (3, 3, 3, 3),
                        (4, 4, 4, 4),
                        (5, 5, 5, 5),
                        (6, 6, 6, 6),
                        (7, 7, 7, 7)
                    ),
                    "sort": [],
                    "ref_chunks": [
                        [0, 0, 0, 1],
                        # Render chunks on MIDDLEWARE
                        [MIDDLEWARE.GITCONFIG]
                    ]
                }
            ]
        ]
    })

if not __name__ == "__main__":
    # Camera: socket
    processes = get_process()