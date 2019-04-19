from setuptools import setup, find_packages

print(find_packages())

setup(
    name="horn",
    version="0.1",
    author="Andrey Komendantyan",
    author_email="komendantyan@gmail.com",
    url="https://github.com/komendantyan/horn",
    tests_require=["pytest"],
    packages=["horn"],
    description="NotImplemented",
    long_description="NotImplemented",
    # license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7"
    ],
    python_requires=">=3.7",
)
