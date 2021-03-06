import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pomodoro-Dev3XoR",
    version="0.8.5",
    author="Dev3XoR",
    author_email="devexor@protonmail.com",
    description="Pomodoro clock and timer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dev3XOR/pomodoro/",
    license_file="LICENSE",
    package_dir={"": "src"},
    packages=["pomodoro"],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="~=3.6",
    install_requires=[
        "playsound",
        "plyer",
    ],
    entry_points={
        "console_scripts": [
            "pomodoro-clock=pomodoro:main",
        ],
    },
)
