from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hand-gesture-control",
    version="1.0.0",
    author="Dinh Yen Binh",
    author_email="binh.vd01500@sinhvien.hoasen.edu.vn",
    description="Hệ thống điều khiển bằng cử chỉ tay sử dụng Computer Vision",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python==4.8.1.78",
        "numpy==1.26.4",
        "pyautogui>=0.9.54",
    ],
    entry_points={
        "console_scripts": [
            "hand-gesture-control=main:main",
        ],
    },
)
