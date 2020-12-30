import setuptools

setuptools.setup(
    name="SubFucker",
    version="1.0.2",
    author="Scorpion Shiled",
    author_email="support@scorpion-shield.com",
    auther_website ="https://www.scorpion-shield.com/",
    description= "SubFucker is simple tool designed to help bughunters with enumerating subdomain status codes",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url="https://github.com/TheXerr0r/SubFucker",
    py_modules=['SubFucker'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'colorama==0.3.9',
        'requests==2.25.0',
        'tabulate==0.8.7'
    ],
    entry_points={
        'console_scripts': [
            'subfucker = SubFucker:main',
        ],
    }
    ,
    zip_safe=False,
)
