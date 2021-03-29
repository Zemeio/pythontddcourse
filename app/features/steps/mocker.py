from unittest.mock import patch


def patch_(context, path, *args, **kwargs):
    patched = patch(path, *args, **kwargs)
    context.patches.append(patched)
    return patched.start()
