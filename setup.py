from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Seat Availability Alert System for Add and Drop'

# Setting up
setup(
    name="addndropalert",
    version=VERSION,
    author="NeuralNine (Sarthak)",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['discord_webhook', 'selenium'],
    keywords=['python', 'ffcs', 'Add and Drop', 'VIT',],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)