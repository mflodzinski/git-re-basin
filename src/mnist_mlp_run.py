"""Compatibility shim for scripts that import `mnist_mlp_run`.

The current vendored checkout only includes `mnist_mlp_train.py`, but several
upstream scripts still import `mnist_mlp_run`. Re-export the training helpers
so those scripts can run unchanged.
"""

from mnist_mlp_train import *  # noqa: F401,F403
