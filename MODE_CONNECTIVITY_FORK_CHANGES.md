# Fork Changes For Mode-Connectivity

This checkout is consumed by the parent repository as a git submodule. At the time this note was added, the working tree was clean and pinned at commit `5f4b6ff` on `main`.

## Comparison Basis

This repository has both `origin` and `upstream` remotes configured locally. The original upstream history is preserved through commit `ef40098`, and all later commits in this fork are fork-specific changes for this repository. Those fork-specific changes are intended to be kept as a single squashed fork layer on top of that base.

## What Changed In This Fork

- `src/datasets.py`
  CIFAR dataset loading was made more cluster-friendly by:
  - honoring `TFDS_DATA_DIR`
  - passing `data_dir=...` into `tfds.load(...)`
  - disabling GCS fallback with `try_gcs=False`
  - moving `torch` / `torchvision` imports inside the ImageNet helper instead of importing them globally
- `src/cifar10_vgg_run.py`
  W&B initialization was made configurable instead of hardcoding project/entity values.
  The script now accepts `--wandb-project` and `--wandb-entity`, and also falls back to `WANDB_PROJECT` / `WANDB_ENTITY` environment variables.
- `src/cifar10_vgg_ste.py`
  The same W&B configurability was added here as in `src/cifar10_vgg_run.py`.
- `src/mnist_mlp_run.py`
  A temporary fork-added shim existed and was later removed in the currently pinned commit, so it is not part of the retained fork surface anymore.

## Main Places To Inspect

- `src/datasets.py`
  All retained data-path and TFDS behavior differences live here.
- `src/cifar10_vgg_run.py`
  W&B configuration changes for the VGG training entrypoint.
- `src/cifar10_vgg_ste.py`
  W&B configuration changes for the VGG straight-through estimator workflow.

## Scope Of The Squashed Fork Layer

The single fork-layer commit on top of `ef40098` is expected to cover the retained changes summarized above, rather than preserve the intermediate fork-only commit history.
