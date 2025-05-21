# RA---Seaqueue-Qian-Cheng

## Multi-Spectral Image (MSI) Segmentation:

The objective of this project is to analyze multispectral data using advanced models like YOLO11 or Segment Anything Model(SAM). By segmenting multispectral images using such models, we can accurately assess crop health, identifying areas that are healthy, water-deficient, or lacking essential nutrients.​

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="0192_rgb.png" alt="0192_rgb" width="48%" height="48%" style="margin-right: 10px;"/>
  <img src="0192_seg.png" alt="0192_seg" width="48%" height="48%"/>
</div>

Multispectral imaging (MSI) is a powerful technique that captures detailed spectral information across numerous wavelengths, enabling the identification and differentiation of materials based on their chemical compositions. In agriculture, MSI serves as a unique signature to assess crop health by detecting specific spectral reflectance patterns associated with various plant conditions. For instance, changes in a plant's Chlorophyll due to stress or disease produce distinct spectral signatures, which can be detected through multispectral imaging.

In summary, integrating multispectral imaging with state-of-the-art models enhances our ability to monitor and manage crop health effectively, leading to more informed agricultural practices and improved crop yields.

## HPC running command

- login to HPC with your account
- cd to /work/NASASpaceResearch/seaqueue/yolo/util
- In terminal $: sbatch hpc_run.sh
- Inside hpc_run: choose the command to train or predict

## Dataset

- login to HPC with your account
- cd to /work/NASASpaceResearch/hyperspectral_images
- Under the folder "blueberry_fileds", there are all the multispetral images (285) in .tif files.
- Under the folder "blueberry_labeled_1", there are 50 annotated images via Roboflow in YOLO11 style.
