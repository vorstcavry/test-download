import launch
import platform

if platform.system() == "Windows":
    if not launch.is_installed("gdown"):
        launch.run_pip("install gdown", "requirements for Downloader")

    if not launch.is_installed("wget"):
        launch.run_pip("install wget", "requirements for Downloader")
